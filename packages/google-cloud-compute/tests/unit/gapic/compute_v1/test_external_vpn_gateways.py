# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule
from requests import Response
from requests.sessions import Session

from google import auth
from google.api_core import client_options
from google.api_core import exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.compute_v1.services.external_vpn_gateways import (
    ExternalVpnGatewaysClient,
)
from google.cloud.compute_v1.services.external_vpn_gateways import pagers
from google.cloud.compute_v1.services.external_vpn_gateways import transports
from google.cloud.compute_v1.types import compute
from google.oauth2 import service_account


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert ExternalVpnGatewaysClient._get_default_mtls_endpoint(None) is None
    assert (
        ExternalVpnGatewaysClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ExternalVpnGatewaysClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ExternalVpnGatewaysClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ExternalVpnGatewaysClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ExternalVpnGatewaysClient._get_default_mtls_endpoint(non_googleapi)
        == non_googleapi
    )


@pytest.mark.parametrize("client_class", [ExternalVpnGatewaysClient,])
def test_external_vpn_gateways_client_from_service_account_info(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "compute.googleapis.com:443"


@pytest.mark.parametrize("client_class", [ExternalVpnGatewaysClient,])
def test_external_vpn_gateways_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "compute.googleapis.com:443"


def test_external_vpn_gateways_client_get_transport_class():
    transport = ExternalVpnGatewaysClient.get_transport_class()
    available_transports = [
        transports.ExternalVpnGatewaysRestTransport,
    ]
    assert transport in available_transports

    transport = ExternalVpnGatewaysClient.get_transport_class("rest")
    assert transport == transports.ExternalVpnGatewaysRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(ExternalVpnGatewaysClient, transports.ExternalVpnGatewaysRestTransport, "rest"),],
)
@mock.patch.object(
    ExternalVpnGatewaysClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ExternalVpnGatewaysClient),
)
def test_external_vpn_gateways_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(ExternalVpnGatewaysClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(ExternalVpnGatewaysClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            ExternalVpnGatewaysClient,
            transports.ExternalVpnGatewaysRestTransport,
            "rest",
            "true",
        ),
        (
            ExternalVpnGatewaysClient,
            transports.ExternalVpnGatewaysRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    ExternalVpnGatewaysClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ExternalVpnGatewaysClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_external_vpn_gateways_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class()
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class()
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(ExternalVpnGatewaysClient, transports.ExternalVpnGatewaysRestTransport, "rest"),],
)
def test_external_vpn_gateways_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [(ExternalVpnGatewaysClient, transports.ExternalVpnGatewaysRestTransport, "rest"),],
)
def test_external_vpn_gateways_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_delete_rest(
    transport: str = "rest", request_type=compute.DeleteExternalVpnGatewayRequest
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            error=compute.Error(errors=[compute.Errors(code="code_value")]),
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id="id_value",
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id="target_id_value",
            target_link="target_link_value",
            user="user_value",
            warnings=[compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)],
            zone="zone_value",
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.delete(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.error == compute.Error(errors=[compute.Errors(code="code_value")])
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == "id_value"
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == "target_id_value"
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.warnings == [
        compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)
    ]
    assert response.zone == "zone_value"


def test_delete_rest_from_dict():
    test_delete_rest(request_type=dict)


def test_delete_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete(
            project="project_value", external_vpn_gateway="external_vpn_gateway_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)

        assert "external_vpn_gateway_value" in http_call[1] + str(body)


def test_delete_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete(
            compute.DeleteExternalVpnGatewayRequest(),
            project="project_value",
            external_vpn_gateway="external_vpn_gateway_value",
        )


def test_get_rest(
    transport: str = "rest", request_type=compute.GetExternalVpnGatewayRequest
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ExternalVpnGateway(
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            id="id_value",
            interfaces=[compute.ExternalVpnGatewayInterface(id=205)],
            kind="kind_value",
            label_fingerprint="label_fingerprint_value",
            labels={"key_value": "value_value"},
            name="name_value",
            redundancy_type=compute.ExternalVpnGateway.RedundancyType.FOUR_IPS_REDUNDANCY,
            self_link="self_link_value",
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.ExternalVpnGateway.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.get(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, compute.ExternalVpnGateway)
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.id == "id_value"
    assert response.interfaces == [compute.ExternalVpnGatewayInterface(id=205)]
    assert response.kind == "kind_value"
    assert response.label_fingerprint == "label_fingerprint_value"
    assert response.labels == {"key_value": "value_value"}
    assert response.name == "name_value"
    assert (
        response.redundancy_type
        == compute.ExternalVpnGateway.RedundancyType.FOUR_IPS_REDUNDANCY
    )
    assert response.self_link == "self_link_value"


def test_get_rest_from_dict():
    test_get_rest(request_type=dict)


def test_get_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ExternalVpnGateway()

        # Wrap the value into a proper Response obj
        json_return_value = compute.ExternalVpnGateway.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get(
            project="project_value", external_vpn_gateway="external_vpn_gateway_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)

        assert "external_vpn_gateway_value" in http_call[1] + str(body)


def test_get_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get(
            compute.GetExternalVpnGatewayRequest(),
            project="project_value",
            external_vpn_gateway="external_vpn_gateway_value",
        )


def test_insert_rest(
    transport: str = "rest", request_type=compute.InsertExternalVpnGatewayRequest
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            error=compute.Error(errors=[compute.Errors(code="code_value")]),
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id="id_value",
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id="target_id_value",
            target_link="target_link_value",
            user="user_value",
            warnings=[compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)],
            zone="zone_value",
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.insert(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.error == compute.Error(errors=[compute.Errors(code="code_value")])
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == "id_value"
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == "target_id_value"
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.warnings == [
        compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)
    ]
    assert response.zone == "zone_value"


def test_insert_rest_from_dict():
    test_insert_rest(request_type=dict)


def test_insert_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        external_vpn_gateway_resource = compute.ExternalVpnGateway(
            creation_timestamp="creation_timestamp_value"
        )

        client.insert(
            project="project_value",
            external_vpn_gateway_resource=external_vpn_gateway_resource,
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)

        assert compute.ExternalVpnGateway.to_json(
            external_vpn_gateway_resource,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        ) in http_call[1] + str(body)


def test_insert_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.insert(
            compute.InsertExternalVpnGatewayRequest(),
            project="project_value",
            external_vpn_gateway_resource=compute.ExternalVpnGateway(
                creation_timestamp="creation_timestamp_value"
            ),
        )


def test_list_rest(
    transport: str = "rest", request_type=compute.ListExternalVpnGatewaysRequest
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ExternalVpnGatewayList(
            etag="etag_value",
            id="id_value",
            items=[
                compute.ExternalVpnGateway(
                    creation_timestamp="creation_timestamp_value"
                )
            ],
            kind="kind_value",
            next_page_token="next_page_token_value",
            self_link="self_link_value",
            warning=compute.Warning(code=compute.Warning.Code.CLEANUP_FAILED),
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.ExternalVpnGatewayList.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.list(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, pagers.ListPager)
    assert response.etag == "etag_value"
    assert response.id == "id_value"
    assert response.items == [
        compute.ExternalVpnGateway(creation_timestamp="creation_timestamp_value")
    ]
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"
    assert response.self_link == "self_link_value"
    assert response.warning == compute.Warning(code=compute.Warning.Code.CLEANUP_FAILED)


def test_list_rest_from_dict():
    test_list_rest(request_type=dict)


def test_list_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.ExternalVpnGatewayList()

        # Wrap the value into a proper Response obj
        json_return_value = compute.ExternalVpnGatewayList.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list(project="project_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)


def test_list_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list(
            compute.ListExternalVpnGatewaysRequest(), project="project_value",
        )


def test_list_pager():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Set the response as a series of pages

        response = (
            compute.ExternalVpnGatewayList(
                items=[
                    compute.ExternalVpnGateway(),
                    compute.ExternalVpnGateway(),
                    compute.ExternalVpnGateway(),
                ],
                next_page_token="abc",
            ),
            compute.ExternalVpnGatewayList(items=[], next_page_token="def",),
            compute.ExternalVpnGatewayList(
                items=[compute.ExternalVpnGateway(),], next_page_token="ghi",
            ),
            compute.ExternalVpnGatewayList(
                items=[compute.ExternalVpnGateway(), compute.ExternalVpnGateway(),],
            ),
        )

        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(compute.ExternalVpnGatewayList.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        metadata = ()
        pager = client.list(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6

        assert all(isinstance(i, compute.ExternalVpnGateway) for i in results)

        pages = list(client.list(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_set_labels_rest(
    transport: str = "rest", request_type=compute.SetLabelsExternalVpnGatewayRequest
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            error=compute.Error(errors=[compute.Errors(code="code_value")]),
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id="id_value",
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id="target_id_value",
            target_link="target_link_value",
            user="user_value",
            warnings=[compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)],
            zone="zone_value",
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.set_labels(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, compute.Operation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.error == compute.Error(errors=[compute.Errors(code="code_value")])
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == "id_value"
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == "target_id_value"
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.warnings == [
        compute.Warnings(code=compute.Warnings.Code.CLEANUP_FAILED)
    ]
    assert response.zone == "zone_value"


def test_set_labels_rest_from_dict():
    test_set_labels_rest(request_type=dict)


def test_set_labels_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # Wrap the value into a proper Response obj
        json_return_value = compute.Operation.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        global_set_labels_request_resource = compute.GlobalSetLabelsRequest(
            label_fingerprint="label_fingerprint_value"
        )

        client.set_labels(
            project="project_value",
            resource="resource_value",
            global_set_labels_request_resource=global_set_labels_request_resource,
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)

        assert "resource_value" in http_call[1] + str(body)

        assert compute.GlobalSetLabelsRequest.to_json(
            global_set_labels_request_resource,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        ) in http_call[1] + str(body)


def test_set_labels_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_labels(
            compute.SetLabelsExternalVpnGatewayRequest(),
            project="project_value",
            resource="resource_value",
            global_set_labels_request_resource=compute.GlobalSetLabelsRequest(
                label_fingerprint="label_fingerprint_value"
            ),
        )


def test_test_iam_permissions_rest(
    transport: str = "rest",
    request_type=compute.TestIamPermissionsExternalVpnGatewayRequest,
):
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.TestPermissionsResponse(
            permissions=["permissions_value"],
        )
        # Wrap the value into a proper Response obj
        json_return_value = compute.TestPermissionsResponse.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        response = client.test_iam_permissions(request)

    # Establish that the response is the type that we expect.

    assert isinstance(response, compute.TestPermissionsResponse)
    assert response.permissions == ["permissions_value"]


def test_test_iam_permissions_rest_from_dict():
    test_test_iam_permissions_rest(request_type=dict)


def test_test_iam_permissions_rest_flattened():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.TestPermissionsResponse()

        # Wrap the value into a proper Response obj
        json_return_value = compute.TestPermissionsResponse.to_json(return_value)
        response_value = Response()
        response_value.status_code = 200
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        test_permissions_request_resource = compute.TestPermissionsRequest(
            permissions=["permissions_value"]
        )

        client.test_iam_permissions(
            project="project_value",
            resource="resource_value",
            test_permissions_request_resource=test_permissions_request_resource,
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, http_call, http_params = req.mock_calls[0]
        body = http_params.get("data")

        assert "project_value" in http_call[1] + str(body)

        assert "resource_value" in http_call[1] + str(body)

        assert compute.TestPermissionsRequest.to_json(
            test_permissions_request_resource,
            including_default_value_fields=False,
            use_integers_for_enums=False,
        ) in http_call[1] + str(body)


def test_test_iam_permissions_rest_flattened_error():
    client = ExternalVpnGatewaysClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.test_iam_permissions(
            compute.TestIamPermissionsExternalVpnGatewayRequest(),
            project="project_value",
            resource="resource_value",
            test_permissions_request_resource=compute.TestPermissionsRequest(
                permissions=["permissions_value"]
            ),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.ExternalVpnGatewaysRestTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ExternalVpnGatewaysClient(
            credentials=credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.ExternalVpnGatewaysRestTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ExternalVpnGatewaysClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.ExternalVpnGatewaysRestTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ExternalVpnGatewaysClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ExternalVpnGatewaysRestTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = ExternalVpnGatewaysClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class", [transports.ExternalVpnGatewaysRestTransport,]
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_external_vpn_gateways_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.ExternalVpnGatewaysTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_external_vpn_gateways_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.compute_v1.services.external_vpn_gateways.transports.ExternalVpnGatewaysTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.ExternalVpnGatewaysTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "delete",
        "get",
        "insert",
        "list",
        "set_labels",
        "test_iam_permissions",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())


def test_external_vpn_gateways_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        auth, "load_credentials_from_file"
    ) as load_creds, mock.patch(
        "google.cloud.compute_v1.services.external_vpn_gateways.transports.ExternalVpnGatewaysTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.ExternalVpnGatewaysTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id="octopus",
        )


def test_external_vpn_gateways_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(auth, "default") as adc, mock.patch(
        "google.cloud.compute_v1.services.external_vpn_gateways.transports.ExternalVpnGatewaysTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.ExternalVpnGatewaysTransport()
        adc.assert_called_once()


def test_external_vpn_gateways_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        ExternalVpnGatewaysClient()
        adc.assert_called_once_with(
            scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id=None,
        )


def test_external_vpn_gateways_http_transport_client_cert_source_for_mtls():
    cred = credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.ExternalVpnGatewaysRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


def test_external_vpn_gateways_host_no_port():
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com"
        ),
    )
    assert client.transport._host == "compute.googleapis.com:443"


def test_external_vpn_gateways_host_with_port():
    client = ExternalVpnGatewaysClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com:8000"
        ),
    )
    assert client.transport._host == "compute.googleapis.com:8000"


def test_common_billing_account_path():
    billing_account = "squid"

    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = ExternalVpnGatewaysClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = ExternalVpnGatewaysClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = ExternalVpnGatewaysClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"

    expected = "folders/{folder}".format(folder=folder,)
    actual = ExternalVpnGatewaysClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = ExternalVpnGatewaysClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = ExternalVpnGatewaysClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"

    expected = "organizations/{organization}".format(organization=organization,)
    actual = ExternalVpnGatewaysClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = ExternalVpnGatewaysClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = ExternalVpnGatewaysClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"

    expected = "projects/{project}".format(project=project,)
    actual = ExternalVpnGatewaysClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = ExternalVpnGatewaysClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = ExternalVpnGatewaysClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"

    expected = "projects/{project}/locations/{location}".format(
        project=project, location=location,
    )
    actual = ExternalVpnGatewaysClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = ExternalVpnGatewaysClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = ExternalVpnGatewaysClient.parse_common_location_path(path)
    assert expected == actual


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.ExternalVpnGatewaysTransport, "_prep_wrapped_messages"
    ) as prep:
        client = ExternalVpnGatewaysClient(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.ExternalVpnGatewaysTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = ExternalVpnGatewaysClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
