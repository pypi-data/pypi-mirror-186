"""Simple Base for ASGI Apps."""

import inspect
import logging
from functools import partial
from typing import Any, Awaitable, Callable, ClassVar, Dict, List, Optional, Set, Type, Union, cast

from http_router import PrefixedRoute
from http_router import Router as HTTPRouter
from http_router.types import TMethods, TPath

from . import ASGIConnectionClosed, ASGIError, ASGIMethodNotAllowed, ASGINotFound, asgi_logger
from .middleware import BaseMiddeware, LifespanMiddleware, StaticFilesMiddleware, parse_response
from .request import Request
from .response import Response, ResponseError
from .typing import DecoratedCallable, F, Receive, Scope, Send
from .utils import iscoroutinefunction, to_awaitable

HTTP_METHODS = {
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "DELETE",
    "CONNECT",
    "OPTIONS",
    "TRACE",
    "PATCH",
}


class Router(HTTPRouter):
    """Rebind router errors."""

    NotFound: ClassVar[Type[Exception]] = ASGINotFound
    RouterError: ClassVar[Type[Exception]] = ASGIError
    MethodNotAllowed: ClassVar[Type[Exception]] = ASGIMethodNotAllowed


class HTTPView:
    """Class-based view pattern for handling HTTP method dispatching.

    .. code-block:: python

        @app.route('/custom')
        class CustomEndpoint(HTTPView):

            async def get(self, request):
                return 'Hello from GET'

            async def post(self, request):
                return 'Hello from POST'

        # ...
        async def test_my_endpoint(client):
            response = await client.get('/custom')
            assert await response.text() == 'Hello from GET'

            response = await client.post('/custom')
            assert await response.text() == 'Hello from POST'

            response = await client.put('/custom')
            assert response.status_code == 405

    """

    def __new__(cls, request: Request, **opts):
        """Init the class and call it."""
        self = super().__new__(cls)
        return self(request, **opts)

    @classmethod
    def __route__(
        cls,
        router: Router,
        *paths: str,
        methods: Optional[TMethods] = None,
        **params,
    ) -> Type["HTTPView"]:
        """Bind the class view to the given router."""
        view_methods = dict(inspect.getmembers(cls, inspect.isfunction))
        methods = methods or [m for m in HTTP_METHODS if m.lower() in view_methods]
        return router.bind(cls, *paths, methods=methods, **params)

    def __call__(self, request: Request, **opts) -> Awaitable:
        """Dispatch the given request by HTTP method."""
        method = getattr(self, request.method.lower())
        return method(request, **opts)


class AppInternalMiddleware(BaseMiddeware):
    """Process responses."""

    scopes = {"http"}

    async def __process__(self, scope: Scope, receive: Receive, send: Send):
        """Send ASGI messages."""
        response = await self.app(scope, receive, send)
        await response(scope, receive, send)


class App:
    """A helper to build ASGI Applications.

    Features:

    * Routing
    * ASGI-Tools :class:`Request`, :class:`Response`
    * Exception management
    * Static files
    * Lifespan events
    * Simplest middlewares

    :param debug: Enable debug mode (more logging, raise unhandled exceptions)
    :type debug: bool, False

    :param logger: Custom logger for the application
    :type logger: logging.Logger

    :param static_url_prefix: A prefix for static files
    :type static_url_prefix: str, "/static"

    :param static_folders: A list of folders to look static files
    :type static_folders: list[str]

    :param trim_last_slash: Consider "/path" and "/path/" as the same
    :type trim_last_slash: bool, False

    """

    exception_handlers: Dict[
        Union[int, Type[BaseException]],
        Callable[[Request, BaseException], Awaitable],
    ]

    def __init__(
        self,
        *,
        debug: bool = False,
        logger: logging.Logger = asgi_logger,
        static_url_prefix: str = "/static",
        static_folders: Union[str, List[str], None] = None,
        trim_last_slash: bool = False,
    ):
        """Initialize router and lifespan middleware."""

        # Register base exception handlers
        self.exception_handlers = {
            ASGIConnectionClosed: to_awaitable(lambda _, __: None)
        }

        # Setup routing
        self.router = router = Router(
            trim_last_slash=trim_last_slash, validator=callable, converter=to_awaitable
        )

        # Setup logging
        self.logger = logger

        async def process(request: Request, _: Receive, __: Send) -> Optional[Response]:
            """Find and call a callback, parse a response, handle exceptions."""
            scope = request.scope
            path = f"{ scope.get('root_path', '') }{ scope['path'] }"
            try:
                match = router(path, scope.get("method", "GET"))
            except ASGINotFound as exc:
                raise ResponseError.NOT_FOUND() from exc
            except ASGIMethodNotAllowed as exc:
                raise ResponseError.METHOD_NOT_ALLOWED() from exc

            scope["path_params"] = {} if match.params is None else match.params
            response = await match.target(request)  # type: ignore
            if response is None and request["type"] == "websocket":
                return None

            return parse_response(response)

        self.__internal__ = AppInternalMiddleware(process)  # type: ignore
        self.__process__ = self.__internal__.app

        # Setup lifespan
        self.lifespan = LifespanMiddleware(
            self.__internal__, ignore_errors=not debug, logger=self.logger
        )

        # Enable middleware for static files
        if static_folders and static_url_prefix:
            md = StaticFilesMiddleware.setup(
                folders=static_folders, url_prefix=static_url_prefix
            )
            self.middleware(md)

        # Debug mode
        self.debug = debug

        # Handle unknown exceptions
        if not debug:

            async def handle_unknown_exception(
                _: Request, exc: BaseException
            ) -> Response:
                self.logger.exception(exc)
                return ResponseError.INTERNAL_SERVER_ERROR()

            self.exception_handlers[Exception] = handle_unknown_exception

        self.internal_middlewares: List = []

    def __route__(self, router: Router, *prefixes: str, **_) -> "App":
        """Mount self as a nested application."""
        for prefix in prefixes:
            route = RouteApp(prefix, set(), target=self)
            router.dynamic.insert(0, route)
        return self

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Convert the given scope into a request and process."""
        scope["app"] = self
        request = Request(scope, receive, send)
        try:
            await self.lifespan(request, receive, send)
        # Handle exceptions
        except BaseException as exc:  # noqa
            response = await self.handle_exc(request, exc)
            if response is ...:
                raise

            await parse_response(response)(scope, receive, send)

    async def handle_exc(self, request: Request, exc: BaseException) -> Any:
        """Look for a handler for the given exception."""
        if isinstance(exc, Response) and exc.status_code in self.exception_handlers:
            return await self.exception_handlers[exc.status_code](request, exc)

        for etype in type(exc).mro():
            if etype in self.exception_handlers:
                return await self.exception_handlers[etype](request, exc)

        return exc if isinstance(exc, Response) else ...

    def middleware(self, md: F, insert_first: bool = False) -> F:
        """Register a middleware."""
        # Register as a simple middleware
        if iscoroutinefunction(md):

            if md not in self.internal_middlewares:
                if insert_first:
                    self.internal_middlewares.insert(0, md)
                else:
                    self.internal_middlewares.append(md)

            app = self.__process__
            for imd in reversed(self.internal_middlewares):
                app = partial(imd, app)

            self.__internal__.bind(app)

        else:
            self.lifespan.bind(md(self.lifespan.app))

        return md

    def route(
        self, *paths: TPath, methods: Optional[TMethods] = None, **opts
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        """Register a route."""
        return self.router.route(*paths, methods=methods, **opts)

    def on_startup(self, fn: Callable) -> None:
        """Register a startup handler."""
        return self.lifespan.on_startup(fn)

    def on_shutdown(self, fn: Callable) -> None:
        """Register a shutdown handler."""
        return self.lifespan.on_shutdown(fn)

    def on_error(
        self, etype: Union[int, Type[BaseException]]
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        """Register an exception handler.

        .. code-block::

            @app.on_error(TimeoutError)
            async def timeout(request, error):
                return 'Something bad happens'

            @app.on_error(404)
            async def page_not_found(request, error):
                return render_template('page_not_found.html'), 404

        """

        def recorder(handler: F) -> F:
            self.exception_handlers[etype] = to_awaitable(handler)
            return handler

        return recorder


class RouteApp(PrefixedRoute):
    """Custom route to submount an application."""

    def __init__(self, path: str, methods: Set, target: App):
        """Create app callable."""
        path = path.rstrip("/")

        def app(request: Request):
            subrequest = request.__copy__(path=request.path[len(path) :])
            receive = cast(Receive, request.receive)
            send = cast(Send, request.send)
            return target.__internal__.app(subrequest, receive, send)

        super().__init__(path, methods, app)
