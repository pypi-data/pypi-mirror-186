import asyncio
import enum
import os
import datetime

from typing import List, Any, Callable, Optional
from dataclasses import dataclass
from packaging import specifiers, version as packaging_version

from context_helper import Context

from graphql_api import GraphQLAPI, field
from graphql_api.remote import GraphQLRemoteObject, GraphQLRemoteExecutor
from graphql_api.utils import to_camel_case

from graphql_http_server import GraphQLHTTPServer


class ServiceState(enum.Enum):
    UNKNOWN = "UNKNOWN"
    CONFIG_ERROR = "CONFIG_ERROR"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    OK = "OK"


@dataclass
class ServiceConnection:
    name: str
    api_version_specifier: Optional[str] = None
    api_url: str = None
    service_directory_url: Optional[str] = None
    http_method: str = "POST"
    raise_error: bool = True
    stub: Any = None
    state: ServiceState = ServiceState.UNKNOWN

    remote_name: Optional[str] = None
    remote_api_version: Optional[str] = None
    remote_service: 'ServiceDirectory' = None
    remote_service_api: GraphQLRemoteObject = None

    @classmethod
    def graphql_exclude_fields(cls) -> List[str]:
        return ['stub', 'remote_service', 'remote_service_api']

    def __post_init__(self):
        if self.stub:
            if hasattr(self.stub, "api_version"):
                stub_api_version = getattr(self.stub, "api_version")
                stub_api_version = packaging_version.Version(stub_api_version)
                if not self.api_version_specifier:
                    self.api_version_specifier = \
                        f"~={stub_api_version.major}.{stub_api_version.minor}"

        if self.api_url and self.stub:
            self.remote_service_api = GraphQLRemoteObject(
                executor=GraphQLRemoteExecutor(
                    name=to_camel_case(self.name, title=True),
                    url=self.api_url,
                    http_method=self.http_method
                ),
                api=GraphQLAPI(root=self.stub)
            )

    async def async_connect(
            self,
            logs: List = None,
            timeout: int = 5
    ) -> bool:

        if logs is None:
            logs = []

        if not self.api_url:
            self.state = ServiceState.CONFIG_ERROR
            logs.append(f"[{datetime.datetime.utcnow()}] ERROR: Missing URL"
                        f" for service {self.name}")

            if self.raise_error:
                raise TypeError(f"Missing URL for service {self.name}")
            return False

        if not self.stub:
            self.state = ServiceState.CONFIG_ERROR
            logs.append(f"[{datetime.datetime.utcnow()}] ERROR: Missing stub"
                        f" for service {self.name}")

            if self.raise_error:
                raise TypeError(f"Missing stub for service {self.name}")
            return False

        name = to_camel_case(self.name, title=True) + "Service"

        logs.append(
            f"[{datetime.datetime.utcnow()}] "
            f"connecting to {name} {self.api_url}"
        )

        if self.service_directory_url:

            # Attempt to connect to a Service Directory
            logs.append(
                f"[{datetime.datetime.utcnow()}]  Connecting to Service "
                f"Directory for {name} {self.service_directory_url}"
            )

            # noinspection PyTypeChecker
            self.remote_service: ServiceDirectory = GraphQLRemoteObject(
                executor=GraphQLRemoteExecutor(
                    name=name,
                    url=self.service_directory_url,
                    http_method=self.http_method,
                    http_timeout=timeout
                ),
                api=GraphQLAPI(root=ServiceDirectory)
            )

            a = datetime.datetime.now()

            try:
                uptime = await self.remote_service.call_async("uptime")
            except Exception as err:
                logs.append(
                    f"[{datetime.datetime.utcnow()}] ERROR: Unable to connect "
                    f"to {name}, timed out after "
                    f"{timeout} seconds, error {err}"
                )
                self.state = ServiceState.CONNECTION_ERROR

                if self.raise_error:
                    raise ConnectionError(
                        f"Unable to connect to {name}, timed out after "
                        f"{timeout} seconds, error {err}"
                    )
                return False

            b = datetime.datetime.now()

            self.remote_name = await self.remote_service.call_async("name")
            self.remote_api_version = await \
                self.remote_service.call_async("api_version")

            delta = b - a
            logs.append(f"[{datetime.datetime.utcnow()}] {name} "
                        f"Response time {delta} Uptime {uptime}")

            if self.api_version_specifier:
                try:
                    specifier = specifiers.Specifier(
                        self.api_version_specifier
                    )
                except specifiers.InvalidSpecifier as err:
                    logs.append(
                        f"[{datetime.datetime.utcnow()}] "
                        f"ERROR: {name} malformed api version specifier "
                        f"{self.api_version_specifier}"
                    )
                    self.state = ServiceState.VALIDATION_ERROR
                    if self.raise_error:
                        raise err
                    return False

                try:
                    service_version = packaging_version.Version(
                        self.remote_api_version
                    )
                except packaging_version.InvalidVersion as err:
                    logs.append(
                        f"[{datetime.datetime.utcnow()}] "
                        f"ERROR: {name} malformed api version found "
                        f"{self.remote_api_version}"
                    )
                    self.state = ServiceState.VALIDATION_ERROR
                    if self.raise_error:
                        raise err
                    return False

                if not specifier.contains(service_version):
                    logs.append(
                        f"[{datetime.datetime.utcnow()}] ERROR: Api version "
                        f"mismatch, found {self.remote_api_version}, "
                        f"required {self.api_version_specifier}"
                    )
                    self.state = ServiceState.VALIDATION_ERROR
                    if self.raise_error:
                        raise TypeError(
                            f"[{datetime.datetime.utcnow()}] {name} api "
                            f"version mismatch at {self.api_url}, expecting "
                            f"version {self.api_version_specifier} but "
                            f"{self.api_url} identified as {self.remote_name} "
                            f"version {self.remote_api_version}."
                        )
                    return False
                else:
                    logs.append(
                        f"[{datetime.datetime.utcnow()}] {name} api version "
                        f"match {self.remote_api_version} is valid for "
                        f"{self.api_version_specifier}"
                    )

        executor = GraphQLRemoteExecutor(
            name=name,
            url=self.api_url,
            http_method=self.http_method,
            http_timeout=timeout
        )

        try:
            response = await executor.execute_async("query { __typename }")
        except Exception as err:
            logs.append(
                f"[{datetime.datetime.utcnow()}] ERROR: {name} API error "
                f"from {self.api_url}, {err}"
            )
            self.state = ServiceState.CONNECTION_ERROR
            if self.raise_error:
                raise err
            return False
        else:
            if response.errors:
                logs.append(
                    f"[{datetime.datetime.utcnow()}] ERROR: {name} API "
                    f"Response error from {self.api_url}, {response.errors}"
                )
                self.state = ServiceState.CONNECTION_ERROR
                if self.raise_error:
                    raise ConnectionError(
                        f"[{datetime.datetime.utcnow()}] ERROR: {name} API "
                        f"Response error from {self.api_url}, "
                        f"{response.errors}"
                    )
                return False

        self.state = ServiceState.OK
        logs.append(
            f"[{datetime.datetime.utcnow()}] ServiceState = OK "
            f"for {name} {self.api_url}"
        )
        return True


class ServiceDirectory:
    """
    The Service Directory is a sidecar to a service that advertises
    the service and creates and maintains connections to other services.

    The Service Directory GraphQL API is accessible at '/service'
    """

    def __init__(
            self,
            name: str,
            stub: Any = None,
            api_version: str = None,
            connections: List[ServiceConnection] = None
    ):
        if not connections:
            connections = []

        self._connections = connections

        if stub is not None:
            if api_version is not None:
                raise AttributeError(
                    "api_version and stub should not both be specified. If a "
                    "stub is provided, the api_version is taken from the stub."
                )
            if hasattr(stub, "api_version"):
                api_version = getattr(stub, "api_version")
            else:
                raise TypeError(f"Invalid stub {stub}")

        if api_version:
            packaging_version.Version(api_version)
        else:
            raise AttributeError(f"api_version for {name} not specified.")

        self._name = name
        self._api_version = api_version
        self._started_at = datetime.datetime.now()
        self._has_checked_connections = False
        self._logs = []

        fp = os.path.dirname(
            os.path.realpath(__file__)) + '/service_directory_default.graphql'
        with open(fp, 'r') as default_query:
            default_query = default_query.read()

        self.http_server = GraphQLHTTPServer.from_api(
            api=GraphQLAPI(root=ServiceDirectory),
            serve_graphiql=True,
            allow_cors=True,
            root_value=self,
            graphiql_default_query=default_query
        )

    def check_connections(self, timeout: int = 5):
        if not self._has_checked_connections and self._connections:
            self._has_checked_connections = True

            async def _check_connections(timeout: int = 5):
                dependencies = []
                for service in self._connections:
                    dependencies.append(
                        service.async_connect(
                            logs=self._logs,
                            timeout=timeout
                        )
                    )
                await asyncio.gather(*dependencies)

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                loop.create_task(_check_connections(timeout=timeout))
            else:
                asyncio.run(_check_connections(timeout=timeout))

    def _with_services(
            self,
            f: Callable = None,
            path: str = None,
            check_connections_on_startup: bool = True,
            check_connections_on_first_request: bool = True,
            timeout: int = 5
    ):

        if check_connections_on_startup:
            self.check_connections(timeout=timeout)

        def with_context(request):
            if check_connections_on_first_request:
                self.check_connections(timeout=timeout)

            if request.path == f"{path}":
                # Expose the service management HTTP server
                return self.http_server.dispatch(request=request)

            with Context(services=self):
                return f(request=request)

        return with_context

    def with_services(
            self,
            f: Callable = None,
            path: str = "/service",
            check_connections_on_startup: bool = True,
            check_connections_on_first_request: bool = True,
            timeout: int = 5
    ):
        """
        Decorator to expose services in the context for this function.
        """

        f = f if callable(f) else None

        conn_on_startup = check_connections_on_startup
        conn_on_first_request = check_connections_on_first_request

        if f:
            return self._with_services(
                f=f,
                path=path,
                check_connections_on_startup=conn_on_startup,
                check_connections_on_first_request=conn_on_first_request,
                timeout=timeout
            )
        else:
            return lambda _f: self._with_services(
                f=_f,
                path=path,
                check_connections_on_startup=conn_on_startup,
                check_connections_on_first_request=conn_on_first_request,
                timeout=timeout
            )

    def __getattr__(self, service_name):
        if self._connections:
            for service in self._connections:
                if service.name == service_name:
                    if service.state == ServiceState.CONNECTION_ERROR:
                        service.async_connect()
                    return service.remote_service_api

        raise KeyError(f"Service '{service_name}' is not available.")

    def __getitem__(self, item):
        return self.__getattr__(item)

    @field
    def name(self) -> str:
        return self._name

    @field
    def api_version(self) -> str:
        return self._api_version

    @field
    def started_at(self) -> str:
        return self._started_at.strftime('%Y-%m-%d %H:%M:%S')

    @field
    def uptime(self) -> str:
        uptime = datetime.datetime.now() - self._started_at
        return str(uptime)

    @field
    def dependencies(self) -> List[ServiceConnection]:
        """
        All the Services this service is dependent on.
        :return:
        """
        return self._connections or []

    @field
    def logs(self) -> List[str]:
        return self._logs
