import threading
import time
import urllib
from datetime import datetime

import pytest
from context_helper import ctx
from graphql_api import field
from requests import request, ConnectTimeout, ReadTimeout
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request

from graphql_http_server import GraphQLHTTPServer


def is_graphql_api_installed():
    try:
        import graphql_api
        assert graphql_api
    except ImportError:
        return False

    return True


def available(url, method="GET"):
    try:
        response = request(method, url, timeout=5, verify=False)
    except (ConnectionError, ConnectTimeout, ReadTimeout):
        return False

    if response.status_code == 400 or response.status_code == 200:
        return True

    return False


class TestApplication:

    def test_dispatch(self, schema):
        server = GraphQLHTTPServer(schema=schema)

        builder = EnvironBuilder(method='GET', query_string="query={hello}")

        request = Request(builder.get_environ())
        response = server.dispatch(request=request)

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"world"}}'

    def test_app(self, schema):
        server = GraphQLHTTPServer(schema=schema)
        response = server.client().get('/?query={hello}')

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"world"}}'

    def test_graphiql(self, schema):
        server = GraphQLHTTPServer(schema=schema)
        response = server.client().get('/', headers={"Accept": "text/html"})

        assert response.status_code == 200
        assert b'GraphiQL' in response.data

    def test_no_graphiql(self, schema):
        server = GraphQLHTTPServer(schema=schema, serve_graphiql=False)
        response = server.client().get('/', headers={"Accept": "text/html"})

        assert response.status_code == 200

    def test_run_app_graphiql(self, schema):
        server = GraphQLHTTPServer(schema=schema)

        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()

        time.sleep(0.5)

        req = urllib.request.Request(
            "http://localhost:5000",
            headers={"Accept": "text/html"}
        )
        response = urllib.request.urlopen(req).read()

        assert b'GraphiQL' in response

    @pytest.mark.skipif(
        not is_graphql_api_installed(),
        reason="GraphQL-API is not installed"
    )
    def test_graphql_api(self):
        from graphql_api import GraphQLAPI

        api = GraphQLAPI()

        @api.type(root=True)
        class RootQueryType:

            @api.field
            def hello(self, name: str) -> str:
                return f"hey {name}"

        server = GraphQLHTTPServer.from_api(api=api)

        response = server.client().get('/?query={hello(name:"rob")}')

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"hey rob"}}'

    utc_time_api_url = \
        "https://europe-west2-parob-297412.cloudfunctions.net/utc_time"

    # noinspection DuplicatedCode,PyUnusedLocal
    @pytest.mark.skipif(
        not available(utc_time_api_url),
        reason=f"The UTCTime API '{utc_time_api_url}' is unavailable"
    )
    @pytest.mark.skipif(
        not is_graphql_api_installed(),
        reason="GraphQL-API is not installed"
    )
    def test_service_directory(self):
        from graphql_api import GraphQLAPI
        from graphql_http_server.service_directory import ServiceDirectory, \
            ServiceConnection

        class UTCTimeServiceStub:

            @field
            def now(self) -> str:
                pass

        connections = [ServiceConnection(
            name="utc_time",
            api_url=self.utc_time_api_url,
            stub=UTCTimeServiceStub
        )]

        service_directory = ServiceDirectory(
            name="gateway",
            api_version="0.0.1",
            connections=connections
        )

        api = GraphQLAPI()

        @api.type(root=True)
        class RootQueryType:

            @api.field
            def hello(self, name: str) -> str:
                utc_time: UTCTimeServiceStub = ctx.services["utc_time"]

                return f"hey {name}, the time is {utc_time.now()}"

        server = GraphQLHTTPServer.from_api(api=api)

        @service_directory.with_services
        def main(request):
            return server.dispatch(request=request)

        client = server.client(main=main)

        response = client.get('/service?query={logs}')

        assert response.status_code == 200
        assert "ServiceState = OK" in response.text

        response = client.get('/?query={hello(name:"rob")}')

        assert response.status_code == 200
        assert "rob" in response.text
        assert datetime.today().strftime('%Y-%m-%d') in response.text
