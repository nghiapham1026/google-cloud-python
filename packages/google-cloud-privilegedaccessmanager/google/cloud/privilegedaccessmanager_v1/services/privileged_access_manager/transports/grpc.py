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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers, operations_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import grpc  # type: ignore

from google.cloud.privilegedaccessmanager_v1.types import privilegedaccessmanager

from .base import DEFAULT_CLIENT_INFO, PrivilegedAccessManagerTransport


class PrivilegedAccessManagerGrpcTransport(PrivilegedAccessManagerTransport):
    """gRPC backend transport for PrivilegedAccessManager.

    This API allows customers to manage temporary, request based
    privileged access to their resources.

    It defines the following resource model:

    -  A collection of ``Entitlement`` resources. An entitlement allows
       configuring (among other things):

       -  Some kind of privileged access that users can request.
       -  A set of users called *requesters* who can request this
          access.
       -  A maximum duration for which the access can be requested.
       -  An optional approval workflow which must be satisfied before
          access is granted.

    -  A collection of ``Grant`` resources. A grant is a request by a
       requester to get the privileged access specified in an
       entitlement for some duration.

       After the approval workflow as specified in the entitlement is
       satisfied, the specified access is given to the requester. The
       access is automatically taken back after the requested duration
       is over.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "privilegedaccessmanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]] = None,
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
                 The hostname to connect to (default: 'privilegedaccessmanager.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if a ``channel`` instance is provided.
            channel (Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]]):
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
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, grpc.Channel):
            # Ignore credentials if a channel was passed.
            credentials = False
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

    @classmethod
    def create_channel(
        cls,
        host: str = "privilegedaccessmanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def check_onboarding_status(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CheckOnboardingStatusRequest],
        privilegedaccessmanager.CheckOnboardingStatusResponse,
    ]:
        r"""Return a callable for the check onboarding status method over gRPC.

        CheckOnboardingStatus reports the onboarding status
        for a project/folder/organization. Any findings reported
        by this API need to be fixed before PAM can be used on
        the resource.

        Returns:
            Callable[[~.CheckOnboardingStatusRequest],
                    ~.CheckOnboardingStatusResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "check_onboarding_status" not in self._stubs:
            self._stubs["check_onboarding_status"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/CheckOnboardingStatus",
                request_serializer=privilegedaccessmanager.CheckOnboardingStatusRequest.serialize,
                response_deserializer=privilegedaccessmanager.CheckOnboardingStatusResponse.deserialize,
            )
        return self._stubs["check_onboarding_status"]

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListEntitlementsRequest],
        privilegedaccessmanager.ListEntitlementsResponse,
    ]:
        r"""Return a callable for the list entitlements method over gRPC.

        Lists entitlements in a given
        project/folder/organization and location.

        Returns:
            Callable[[~.ListEntitlementsRequest],
                    ~.ListEntitlementsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entitlements" not in self._stubs:
            self._stubs["list_entitlements"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/ListEntitlements",
                request_serializer=privilegedaccessmanager.ListEntitlementsRequest.serialize,
                response_deserializer=privilegedaccessmanager.ListEntitlementsResponse.deserialize,
            )
        return self._stubs["list_entitlements"]

    @property
    def search_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchEntitlementsRequest],
        privilegedaccessmanager.SearchEntitlementsResponse,
    ]:
        r"""Return a callable for the search entitlements method over gRPC.

        ``SearchEntitlements`` returns entitlements on which the caller
        has the specified access.

        Returns:
            Callable[[~.SearchEntitlementsRequest],
                    ~.SearchEntitlementsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_entitlements" not in self._stubs:
            self._stubs["search_entitlements"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/SearchEntitlements",
                request_serializer=privilegedaccessmanager.SearchEntitlementsRequest.serialize,
                response_deserializer=privilegedaccessmanager.SearchEntitlementsResponse.deserialize,
            )
        return self._stubs["search_entitlements"]

    @property
    def get_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetEntitlementRequest],
        privilegedaccessmanager.Entitlement,
    ]:
        r"""Return a callable for the get entitlement method over gRPC.

        Gets details of a single entitlement.

        Returns:
            Callable[[~.GetEntitlementRequest],
                    ~.Entitlement]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entitlement" not in self._stubs:
            self._stubs["get_entitlement"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/GetEntitlement",
                request_serializer=privilegedaccessmanager.GetEntitlementRequest.serialize,
                response_deserializer=privilegedaccessmanager.Entitlement.deserialize,
            )
        return self._stubs["get_entitlement"]

    @property
    def create_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateEntitlementRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create entitlement method over gRPC.

        Creates a new entitlement in a given
        project/folder/organization and location.

        Returns:
            Callable[[~.CreateEntitlementRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entitlement" not in self._stubs:
            self._stubs["create_entitlement"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/CreateEntitlement",
                request_serializer=privilegedaccessmanager.CreateEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_entitlement"]

    @property
    def delete_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DeleteEntitlementRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete entitlement method over gRPC.

        Deletes a single entitlement. This method can only be
        called when there are no in-progress
        (ACTIVE/ACTIVATING/REVOKING) grants under the
        entitlement.

        Returns:
            Callable[[~.DeleteEntitlementRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entitlement" not in self._stubs:
            self._stubs["delete_entitlement"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/DeleteEntitlement",
                request_serializer=privilegedaccessmanager.DeleteEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_entitlement"]

    @property
    def update_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.UpdateEntitlementRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update entitlement method over gRPC.

        Updates the entitlement specified in the request. Updated fields
        in the entitlement need to be specified in an update mask. The
        changes made to an entitlement are applicable only on future
        grants of the entitlement. However, if new approvers are added
        or existing approvers are removed from the approval workflow,
        the changes are effective on existing grants.

        The following fields are not supported for updates:

        -  All immutable fields
        -  Entitlement name
        -  Resource name
        -  Resource type
        -  Adding an approval workflow in an entitlement which
           previously had no approval workflow.
        -  Deleting the approval workflow from an entitlement.
        -  Adding or deleting a step in the approval workflow (only one
           step is supported)

        Note that updates are allowed on the list of approvers in an
        approval workflow step.

        Returns:
            Callable[[~.UpdateEntitlementRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entitlement" not in self._stubs:
            self._stubs["update_entitlement"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/UpdateEntitlement",
                request_serializer=privilegedaccessmanager.UpdateEntitlementRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_entitlement"]

    @property
    def list_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListGrantsRequest],
        privilegedaccessmanager.ListGrantsResponse,
    ]:
        r"""Return a callable for the list grants method over gRPC.

        Lists grants for a given entitlement.

        Returns:
            Callable[[~.ListGrantsRequest],
                    ~.ListGrantsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_grants" not in self._stubs:
            self._stubs["list_grants"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/ListGrants",
                request_serializer=privilegedaccessmanager.ListGrantsRequest.serialize,
                response_deserializer=privilegedaccessmanager.ListGrantsResponse.deserialize,
            )
        return self._stubs["list_grants"]

    @property
    def search_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchGrantsRequest],
        privilegedaccessmanager.SearchGrantsResponse,
    ]:
        r"""Return a callable for the search grants method over gRPC.

        ``SearchGrants`` returns grants that are related to the calling
        user in the specified way.

        Returns:
            Callable[[~.SearchGrantsRequest],
                    ~.SearchGrantsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_grants" not in self._stubs:
            self._stubs["search_grants"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/SearchGrants",
                request_serializer=privilegedaccessmanager.SearchGrantsRequest.serialize,
                response_deserializer=privilegedaccessmanager.SearchGrantsResponse.deserialize,
            )
        return self._stubs["search_grants"]

    @property
    def get_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetGrantRequest], privilegedaccessmanager.Grant
    ]:
        r"""Return a callable for the get grant method over gRPC.

        Get details of a single grant.

        Returns:
            Callable[[~.GetGrantRequest],
                    ~.Grant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_grant" not in self._stubs:
            self._stubs["get_grant"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/GetGrant",
                request_serializer=privilegedaccessmanager.GetGrantRequest.serialize,
                response_deserializer=privilegedaccessmanager.Grant.deserialize,
            )
        return self._stubs["get_grant"]

    @property
    def create_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateGrantRequest], privilegedaccessmanager.Grant
    ]:
        r"""Return a callable for the create grant method over gRPC.

        Creates a new grant in a given project and location.

        Returns:
            Callable[[~.CreateGrantRequest],
                    ~.Grant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_grant" not in self._stubs:
            self._stubs["create_grant"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/CreateGrant",
                request_serializer=privilegedaccessmanager.CreateGrantRequest.serialize,
                response_deserializer=privilegedaccessmanager.Grant.deserialize,
            )
        return self._stubs["create_grant"]

    @property
    def approve_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ApproveGrantRequest], privilegedaccessmanager.Grant
    ]:
        r"""Return a callable for the approve grant method over gRPC.

        ``ApproveGrant`` is used to approve a grant. This method can
        only be called on a grant when it's in the ``APPROVAL_AWAITED``
        state. This operation can't be undone.

        Returns:
            Callable[[~.ApproveGrantRequest],
                    ~.Grant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "approve_grant" not in self._stubs:
            self._stubs["approve_grant"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/ApproveGrant",
                request_serializer=privilegedaccessmanager.ApproveGrantRequest.serialize,
                response_deserializer=privilegedaccessmanager.Grant.deserialize,
            )
        return self._stubs["approve_grant"]

    @property
    def deny_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DenyGrantRequest], privilegedaccessmanager.Grant
    ]:
        r"""Return a callable for the deny grant method over gRPC.

        ``DenyGrant`` is used to deny a grant. This method can only be
        called on a grant when it's in the ``APPROVAL_AWAITED`` state.
        This operation can't be undone.

        Returns:
            Callable[[~.DenyGrantRequest],
                    ~.Grant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deny_grant" not in self._stubs:
            self._stubs["deny_grant"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/DenyGrant",
                request_serializer=privilegedaccessmanager.DenyGrantRequest.serialize,
                response_deserializer=privilegedaccessmanager.Grant.deserialize,
            )
        return self._stubs["deny_grant"]

    @property
    def revoke_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.RevokeGrantRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the revoke grant method over gRPC.

        ``RevokeGrant`` is used to immediately revoke access for a
        grant. This method can be called when the grant is in a
        non-terminal state.

        Returns:
            Callable[[~.RevokeGrantRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revoke_grant" not in self._stubs:
            self._stubs["revoke_grant"] = self.grpc_channel.unary_unary(
                "/google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager/RevokeGrant",
                request_serializer=privilegedaccessmanager.RevokeGrantRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["revoke_grant"]

    def close(self):
        self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

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

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse
    ]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("PrivilegedAccessManagerGrpcTransport",)
