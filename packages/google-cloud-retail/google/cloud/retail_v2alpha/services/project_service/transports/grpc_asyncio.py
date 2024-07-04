# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.retail_v2alpha.types import project
from google.cloud.retail_v2alpha.types import project as gcr_project
from google.cloud.retail_v2alpha.types import project_service

from .base import DEFAULT_CLIENT_INFO, ProjectServiceTransport
from .grpc import ProjectServiceGrpcTransport


class ProjectServiceGrpcAsyncIOTransport(ProjectServiceTransport):
    """gRPC AsyncIO backend transport for ProjectService.

    Service for settings at Project level.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def get_project(
        self,
    ) -> Callable[[project_service.GetProjectRequest], Awaitable[project.Project]]:
        r"""Return a callable for the get project method over gRPC.

        Gets the project.

        Throws ``NOT_FOUND`` if the project wasn't initialized for the
        Retail API service.

        Returns:
            Callable[[~.GetProjectRequest],
                    Awaitable[~.Project]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_project" not in self._stubs:
            self._stubs["get_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/GetProject",
                request_serializer=project_service.GetProjectRequest.serialize,
                response_deserializer=project.Project.deserialize,
            )
        return self._stubs["get_project"]

    @property
    def accept_terms(
        self,
    ) -> Callable[[project_service.AcceptTermsRequest], Awaitable[gcr_project.Project]]:
        r"""Return a callable for the accept terms method over gRPC.

        Accepts service terms for this project.
        By making requests to this API, you agree to the terms
        of service linked below.
        https://cloud.google.com/retail/data-use-terms

        Returns:
            Callable[[~.AcceptTermsRequest],
                    Awaitable[~.Project]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "accept_terms" not in self._stubs:
            self._stubs["accept_terms"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/AcceptTerms",
                request_serializer=project_service.AcceptTermsRequest.serialize,
                response_deserializer=gcr_project.Project.deserialize,
            )
        return self._stubs["accept_terms"]

    @property
    def enroll_solution(
        self,
    ) -> Callable[
        [project_service.EnrollSolutionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the enroll solution method over gRPC.

        The method enrolls a solution of type [Retail
        Search][google.cloud.retail.v2alpha.SolutionType.SOLUTION_TYPE_SEARCH]
        into a project.

        The [Recommendations AI solution
        type][google.cloud.retail.v2alpha.SolutionType.SOLUTION_TYPE_RECOMMENDATION]
        is enrolled by default when your project enables Retail API, so
        you don't need to call the enrollSolution method for
        recommendations.

        Returns:
            Callable[[~.EnrollSolutionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enroll_solution" not in self._stubs:
            self._stubs["enroll_solution"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/EnrollSolution",
                request_serializer=project_service.EnrollSolutionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["enroll_solution"]

    @property
    def list_enrolled_solutions(
        self,
    ) -> Callable[
        [project_service.ListEnrolledSolutionsRequest],
        Awaitable[project_service.ListEnrolledSolutionsResponse],
    ]:
        r"""Return a callable for the list enrolled solutions method over gRPC.

        Lists all the retail API solutions the project has
        enrolled.

        Returns:
            Callable[[~.ListEnrolledSolutionsRequest],
                    Awaitable[~.ListEnrolledSolutionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_enrolled_solutions" not in self._stubs:
            self._stubs["list_enrolled_solutions"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/ListEnrolledSolutions",
                request_serializer=project_service.ListEnrolledSolutionsRequest.serialize,
                response_deserializer=project_service.ListEnrolledSolutionsResponse.deserialize,
            )
        return self._stubs["list_enrolled_solutions"]

    @property
    def get_logging_config(
        self,
    ) -> Callable[
        [project_service.GetLoggingConfigRequest], Awaitable[project.LoggingConfig]
    ]:
        r"""Return a callable for the get logging config method over gRPC.

        Gets the
        [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig] of
        the requested project.

        Returns:
            Callable[[~.GetLoggingConfigRequest],
                    Awaitable[~.LoggingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_logging_config" not in self._stubs:
            self._stubs["get_logging_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/GetLoggingConfig",
                request_serializer=project_service.GetLoggingConfigRequest.serialize,
                response_deserializer=project.LoggingConfig.deserialize,
            )
        return self._stubs["get_logging_config"]

    @property
    def update_logging_config(
        self,
    ) -> Callable[
        [project_service.UpdateLoggingConfigRequest], Awaitable[project.LoggingConfig]
    ]:
        r"""Return a callable for the update logging config method over gRPC.

        Updates the
        [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig] of
        the requested project.

        Returns:
            Callable[[~.UpdateLoggingConfigRequest],
                    Awaitable[~.LoggingConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_logging_config" not in self._stubs:
            self._stubs["update_logging_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/UpdateLoggingConfig",
                request_serializer=project_service.UpdateLoggingConfigRequest.serialize,
                response_deserializer=project.LoggingConfig.deserialize,
            )
        return self._stubs["update_logging_config"]

    @property
    def get_alert_config(
        self,
    ) -> Callable[
        [project_service.GetAlertConfigRequest], Awaitable[project.AlertConfig]
    ]:
        r"""Return a callable for the get alert config method over gRPC.

        Get the [AlertConfig][google.cloud.retail.v2alpha.AlertConfig]
        of the requested project.

        Returns:
            Callable[[~.GetAlertConfigRequest],
                    Awaitable[~.AlertConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_alert_config" not in self._stubs:
            self._stubs["get_alert_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/GetAlertConfig",
                request_serializer=project_service.GetAlertConfigRequest.serialize,
                response_deserializer=project.AlertConfig.deserialize,
            )
        return self._stubs["get_alert_config"]

    @property
    def update_alert_config(
        self,
    ) -> Callable[
        [project_service.UpdateAlertConfigRequest], Awaitable[project.AlertConfig]
    ]:
        r"""Return a callable for the update alert config method over gRPC.

        Update the alert config of the requested project.

        Returns:
            Callable[[~.UpdateAlertConfigRequest],
                    Awaitable[~.AlertConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_alert_config" not in self._stubs:
            self._stubs["update_alert_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.retail.v2alpha.ProjectService/UpdateAlertConfig",
                request_serializer=project_service.UpdateAlertConfigRequest.serialize,
                response_deserializer=project.AlertConfig.deserialize,
            )
        return self._stubs["update_alert_config"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_project: gapic_v1.method_async.wrap_method(
                self.get_project,
                default_timeout=None,
                client_info=client_info,
            ),
            self.accept_terms: gapic_v1.method_async.wrap_method(
                self.accept_terms,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enroll_solution: gapic_v1.method_async.wrap_method(
                self.enroll_solution,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_enrolled_solutions: gapic_v1.method_async.wrap_method(
                self.list_enrolled_solutions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_logging_config: gapic_v1.method_async.wrap_method(
                self.get_logging_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_logging_config: gapic_v1.method_async.wrap_method(
                self.update_logging_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_alert_config: gapic_v1.method_async.wrap_method(
                self.get_alert_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_alert_config: gapic_v1.method_async.wrap_method(
                self.update_alert_config,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        return self.grpc_channel.close()

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]


__all__ = ("ProjectServiceGrpcAsyncIOTransport",)
