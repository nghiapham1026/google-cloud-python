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
from collections import OrderedDict
import functools
import os
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)
import warnings

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import extended_operation, gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.compute_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

from google.api_core import extended_operation  # type: ignore

from google.cloud.compute_v1.services.target_ssl_proxies import pagers
from google.cloud.compute_v1.types import compute

from .transports.base import DEFAULT_CLIENT_INFO, TargetSslProxiesTransport
from .transports.rest import TargetSslProxiesRestTransport


class TargetSslProxiesClientMeta(type):
    """Metaclass for the TargetSslProxies client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[TargetSslProxiesTransport]]
    _transport_registry["rest"] = TargetSslProxiesRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[TargetSslProxiesTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class TargetSslProxiesClient(metaclass=TargetSslProxiesClientMeta):
    """The TargetSslProxies API."""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "compute.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    _DEFAULT_ENDPOINT_TEMPLATE = "compute.{UNIVERSE_DOMAIN}"
    _DEFAULT_UNIVERSE = "googleapis.com"

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TargetSslProxiesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TargetSslProxiesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> TargetSslProxiesTransport:
        """Returns the transport used by the client instance.

        Returns:
            TargetSslProxiesTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Deprecated. Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """

        warnings.warn(
            "get_mtls_endpoint_and_cert_source is deprecated. Use the api_endpoint property instead.",
            DeprecationWarning,
        )
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    @staticmethod
    def _read_environment_variables():
        """Returns the environment variables used by the client.

        Returns:
            Tuple[bool, str, str]: returns the GOOGLE_API_USE_CLIENT_CERTIFICATE,
            GOOGLE_API_USE_MTLS_ENDPOINT, and GOOGLE_CLOUD_UNIVERSE_DOMAIN environment variables.

        Raises:
            ValueError: If GOOGLE_API_USE_CLIENT_CERTIFICATE is not
                any of ["true", "false"].
            google.auth.exceptions.MutualTLSChannelError: If GOOGLE_API_USE_MTLS_ENDPOINT
                is not any of ["auto", "never", "always"].
        """
        use_client_cert = os.getenv(
            "GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"
        ).lower()
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto").lower()
        universe_domain_env = os.getenv("GOOGLE_CLOUD_UNIVERSE_DOMAIN")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )
        return use_client_cert == "true", use_mtls_endpoint, universe_domain_env

    @staticmethod
    def _get_client_cert_source(provided_cert_source, use_cert_flag):
        """Return the client cert source to be used by the client.

        Args:
            provided_cert_source (bytes): The client certificate source provided.
            use_cert_flag (bool): A flag indicating whether to use the client certificate.

        Returns:
            bytes or None: The client cert source to be used by the client.
        """
        client_cert_source = None
        if use_cert_flag:
            if provided_cert_source:
                client_cert_source = provided_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()
        return client_cert_source

    @staticmethod
    def _get_api_endpoint(
        api_override, client_cert_source, universe_domain, use_mtls_endpoint
    ):
        """Return the API endpoint used by the client.

        Args:
            api_override (str): The API endpoint override. If specified, this is always
                the return value of this function and the other arguments are not used.
            client_cert_source (bytes): The client certificate source used by the client.
            universe_domain (str): The universe domain used by the client.
            use_mtls_endpoint (str): How to use the mTLS endpoint, which depends also on the other parameters.
                Possible values are "always", "auto", or "never".

        Returns:
            str: The API endpoint to be used by the client.
        """
        if api_override is not None:
            api_endpoint = api_override
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            _default_universe = TargetSslProxiesClient._DEFAULT_UNIVERSE
            if universe_domain != _default_universe:
                raise MutualTLSChannelError(
                    f"mTLS is not supported in any universe other than {_default_universe}."
                )
            api_endpoint = TargetSslProxiesClient.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = TargetSslProxiesClient._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=universe_domain
            )
        return api_endpoint

    @staticmethod
    def _get_universe_domain(
        client_universe_domain: Optional[str], universe_domain_env: Optional[str]
    ) -> str:
        """Return the universe domain used by the client.

        Args:
            client_universe_domain (Optional[str]): The universe domain configured via the client options.
            universe_domain_env (Optional[str]): The universe domain configured via the "GOOGLE_CLOUD_UNIVERSE_DOMAIN" environment variable.

        Returns:
            str: The universe domain to be used by the client.

        Raises:
            ValueError: If the universe domain is an empty string.
        """
        universe_domain = TargetSslProxiesClient._DEFAULT_UNIVERSE
        if client_universe_domain is not None:
            universe_domain = client_universe_domain
        elif universe_domain_env is not None:
            universe_domain = universe_domain_env
        if len(universe_domain.strip()) == 0:
            raise ValueError("Universe Domain cannot be an empty string.")
        return universe_domain

    @staticmethod
    def _compare_universes(
        client_universe: str, credentials: ga_credentials.Credentials
    ) -> bool:
        """Returns True iff the universe domains used by the client and credentials match.

        Args:
            client_universe (str): The universe domain configured via the client options.
            credentials (ga_credentials.Credentials): The credentials being used in the client.

        Returns:
            bool: True iff client_universe matches the universe in credentials.

        Raises:
            ValueError: when client_universe does not match the universe in credentials.
        """

        default_universe = TargetSslProxiesClient._DEFAULT_UNIVERSE
        credentials_universe = getattr(credentials, "universe_domain", default_universe)

        if client_universe != credentials_universe:
            raise ValueError(
                "The configured universe domain "
                f"({client_universe}) does not match the universe domain "
                f"found in the credentials ({credentials_universe}). "
                "If you haven't configured the universe domain explicitly, "
                f"`{default_universe}` is the default."
            )
        return True

    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """
        self._is_universe_domain_valid = (
            self._is_universe_domain_valid
            or TargetSslProxiesClient._compare_universes(
                self.universe_domain, self.transport._credentials
            )
        )
        return self._is_universe_domain_valid

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used by the client instance.
        """
        return self._universe_domain

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, TargetSslProxiesTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the target ssl proxies client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, TargetSslProxiesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library's source repository.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client_options = client_options
        if isinstance(self._client_options, dict):
            self._client_options = client_options_lib.from_dict(self._client_options)
        if self._client_options is None:
            self._client_options = client_options_lib.ClientOptions()
        self._client_options = cast(
            client_options_lib.ClientOptions, self._client_options
        )

        universe_domain_opt = getattr(self._client_options, "universe_domain", None)

        (
            self._use_client_cert,
            self._use_mtls_endpoint,
            self._universe_domain_env,
        ) = TargetSslProxiesClient._read_environment_variables()
        self._client_cert_source = TargetSslProxiesClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = TargetSslProxiesClient._get_universe_domain(
            universe_domain_opt, self._universe_domain_env
        )
        self._api_endpoint = None  # updated below, depending on `transport`

        # Initialize the universe domain validation.
        self._is_universe_domain_valid = False

        api_key_value = getattr(self._client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        transport_provided = isinstance(transport, TargetSslProxiesTransport)
        if transport_provided:
            # transport is a TargetSslProxiesTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = cast(TargetSslProxiesTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = (
            self._api_endpoint
            or TargetSslProxiesClient._get_api_endpoint(
                self._client_options.api_endpoint,
                self._client_cert_source,
                self._universe_domain,
                self._use_mtls_endpoint,
            )
        )

        if not transport_provided:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(cast(str, transport))
            self._transport = Transport(
                credentials=credentials,
                credentials_file=self._client_options.credentials_file,
                host=self._api_endpoint,
                scopes=self._client_options.scopes,
                client_cert_source_for_mtls=self._client_cert_source,
                quota_project_id=self._client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=self._client_options.api_audience,
            )

    def delete_unary(
        self,
        request: Optional[Union[compute.DeleteTargetSslProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Deletes the specified TargetSslProxy resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_delete():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.DeleteTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.DeleteTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.Delete. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                to delete.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target_ssl_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.DeleteTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.DeleteTargetSslProxyRequest):
            request = compute.DeleteTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete(
        self,
        request: Optional[Union[compute.DeleteTargetSslProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes the specified TargetSslProxy resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_delete():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.DeleteTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.DeleteTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.Delete. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                to delete.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target_ssl_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.DeleteTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.DeleteTargetSslProxyRequest):
            request = compute.DeleteTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def get(
        self,
        request: Optional[Union[compute.GetTargetSslProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.TargetSslProxy:
        r"""Returns the specified TargetSslProxy resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_get():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.GetTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.get(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.GetTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.Get. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                to return.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.compute_v1.types.TargetSslProxy:
                Represents a Target SSL Proxy
                resource. A target SSL proxy is a
                component of a Proxy Network Load
                Balancer. The forwarding rule references
                the target SSL proxy, and the target
                proxy then references a backend service.
                For more information, read Proxy Network
                Load Balancer overview.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target_ssl_proxy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.GetTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.GetTargetSslProxyRequest):
            request = compute.GetTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def insert_unary(
        self,
        request: Optional[Union[compute.InsertTargetSslProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy_resource: Optional[compute.TargetSslProxy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Creates a TargetSslProxy resource in the specified
        project using the data included in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_insert():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.InsertTargetSslProxyRequest(
                    project="project_value",
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.InsertTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.Insert. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy_resource (google.cloud.compute_v1.types.TargetSslProxy):
                The body resource for this request
                This corresponds to the ``target_ssl_proxy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target_ssl_proxy_resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.InsertTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.InsertTargetSslProxyRequest):
            request = compute.InsertTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy_resource is not None:
                request.target_ssl_proxy_resource = target_ssl_proxy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def insert(
        self,
        request: Optional[Union[compute.InsertTargetSslProxyRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy_resource: Optional[compute.TargetSslProxy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Creates a TargetSslProxy resource in the specified
        project using the data included in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_insert():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.InsertTargetSslProxyRequest(
                    project="project_value",
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.InsertTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.Insert. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy_resource (google.cloud.compute_v1.types.TargetSslProxy):
                The body resource for this request
                This corresponds to the ``target_ssl_proxy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target_ssl_proxy_resource])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.InsertTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.InsertTargetSslProxyRequest):
            request = compute.InsertTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy_resource is not None:
                request.target_ssl_proxy_resource = target_ssl_proxy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def list(
        self,
        request: Optional[Union[compute.ListTargetSslProxiesRequest, dict]] = None,
        *,
        project: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPager:
        r"""Retrieves the list of TargetSslProxy resources
        available to the specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_list():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.ListTargetSslProxiesRequest(
                    project="project_value",
                )

                # Make the request
                page_result = client.list(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.ListTargetSslProxiesRequest, dict]):
                The request object. A request message for
                TargetSslProxies.List. See the method
                description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.compute_v1.services.target_ssl_proxies.pagers.ListPager:
                Contains a list of TargetSslProxy
                resources.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.ListTargetSslProxiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.ListTargetSslProxiesRequest):
            request = compute.ListTargetSslProxiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_backend_service_unary(
        self,
        request: Optional[
            Union[compute.SetBackendServiceTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_backend_service_request_resource: Optional[
            compute.TargetSslProxiesSetBackendServiceRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Changes the BackendService for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_backend_service():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetBackendServiceTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_backend_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetBackendServiceTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetBackendService. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose BackendService resource is to be
                set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_backend_service_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetBackendServiceRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_backend_service_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_backend_service_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetBackendServiceTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetBackendServiceTargetSslProxyRequest):
            request = compute.SetBackendServiceTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_backend_service_request_resource is not None:
                request.target_ssl_proxies_set_backend_service_request_resource = (
                    target_ssl_proxies_set_backend_service_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_backend_service]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_backend_service(
        self,
        request: Optional[
            Union[compute.SetBackendServiceTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_backend_service_request_resource: Optional[
            compute.TargetSslProxiesSetBackendServiceRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Changes the BackendService for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_backend_service():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetBackendServiceTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_backend_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetBackendServiceTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetBackendService. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose BackendService resource is to be
                set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_backend_service_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetBackendServiceRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_backend_service_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_backend_service_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetBackendServiceTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetBackendServiceTargetSslProxyRequest):
            request = compute.SetBackendServiceTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_backend_service_request_resource is not None:
                request.target_ssl_proxies_set_backend_service_request_resource = (
                    target_ssl_proxies_set_backend_service_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_backend_service]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def set_certificate_map_unary(
        self,
        request: Optional[
            Union[compute.SetCertificateMapTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_certificate_map_request_resource: Optional[
            compute.TargetSslProxiesSetCertificateMapRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Changes the Certificate Map for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_certificate_map():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetCertificateMapTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_certificate_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetCertificateMapTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetCertificateMap. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose CertificateMap is to be set. The
                name must be 1-63 characters long, and
                comply with RFC1035.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_certificate_map_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetCertificateMapRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_certificate_map_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_certificate_map_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetCertificateMapTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetCertificateMapTargetSslProxyRequest):
            request = compute.SetCertificateMapTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_certificate_map_request_resource is not None:
                request.target_ssl_proxies_set_certificate_map_request_resource = (
                    target_ssl_proxies_set_certificate_map_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_certificate_map]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_certificate_map(
        self,
        request: Optional[
            Union[compute.SetCertificateMapTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_certificate_map_request_resource: Optional[
            compute.TargetSslProxiesSetCertificateMapRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Changes the Certificate Map for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_certificate_map():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetCertificateMapTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_certificate_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetCertificateMapTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetCertificateMap. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose CertificateMap is to be set. The
                name must be 1-63 characters long, and
                comply with RFC1035.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_certificate_map_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetCertificateMapRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_certificate_map_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_certificate_map_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetCertificateMapTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetCertificateMapTargetSslProxyRequest):
            request = compute.SetCertificateMapTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_certificate_map_request_resource is not None:
                request.target_ssl_proxies_set_certificate_map_request_resource = (
                    target_ssl_proxies_set_certificate_map_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_certificate_map]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def set_proxy_header_unary(
        self,
        request: Optional[
            Union[compute.SetProxyHeaderTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_proxy_header_request_resource: Optional[
            compute.TargetSslProxiesSetProxyHeaderRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Changes the ProxyHeaderType for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_proxy_header():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetProxyHeaderTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_proxy_header(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetProxyHeaderTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetProxyHeader. See the
                method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose ProxyHeader is to be set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_proxy_header_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetProxyHeaderRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_proxy_header_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_proxy_header_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetProxyHeaderTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetProxyHeaderTargetSslProxyRequest):
            request = compute.SetProxyHeaderTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_proxy_header_request_resource is not None:
                request.target_ssl_proxies_set_proxy_header_request_resource = (
                    target_ssl_proxies_set_proxy_header_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_proxy_header]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_proxy_header(
        self,
        request: Optional[
            Union[compute.SetProxyHeaderTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_proxy_header_request_resource: Optional[
            compute.TargetSslProxiesSetProxyHeaderRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Changes the ProxyHeaderType for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_proxy_header():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetProxyHeaderTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_proxy_header(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetProxyHeaderTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetProxyHeader. See the
                method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose ProxyHeader is to be set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_proxy_header_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetProxyHeaderRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_proxy_header_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_proxy_header_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetProxyHeaderTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetProxyHeaderTargetSslProxyRequest):
            request = compute.SetProxyHeaderTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_proxy_header_request_resource is not None:
                request.target_ssl_proxies_set_proxy_header_request_resource = (
                    target_ssl_proxies_set_proxy_header_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_proxy_header]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def set_ssl_certificates_unary(
        self,
        request: Optional[
            Union[compute.SetSslCertificatesTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_ssl_certificates_request_resource: Optional[
            compute.TargetSslProxiesSetSslCertificatesRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Changes SslCertificates for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_ssl_certificates():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetSslCertificatesTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_ssl_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetSslCertificatesTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetSslCertificates. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose SslCertificate resource is to be
                set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_ssl_certificates_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetSslCertificatesRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_ssl_certificates_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_ssl_certificates_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetSslCertificatesTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetSslCertificatesTargetSslProxyRequest):
            request = compute.SetSslCertificatesTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_ssl_certificates_request_resource is not None:
                request.target_ssl_proxies_set_ssl_certificates_request_resource = (
                    target_ssl_proxies_set_ssl_certificates_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_ssl_certificates]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_ssl_certificates(
        self,
        request: Optional[
            Union[compute.SetSslCertificatesTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        target_ssl_proxies_set_ssl_certificates_request_resource: Optional[
            compute.TargetSslProxiesSetSslCertificatesRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Changes SslCertificates for TargetSslProxy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_ssl_certificates():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetSslCertificatesTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_ssl_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetSslCertificatesTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetSslCertificates. See
                the method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose SslCertificate resource is to be
                set.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxies_set_ssl_certificates_request_resource (google.cloud.compute_v1.types.TargetSslProxiesSetSslCertificatesRequest):
                The body resource for this request
                This corresponds to the ``target_ssl_proxies_set_ssl_certificates_request_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [
                project,
                target_ssl_proxy,
                target_ssl_proxies_set_ssl_certificates_request_resource,
            ]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetSslCertificatesTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetSslCertificatesTargetSslProxyRequest):
            request = compute.SetSslCertificatesTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if target_ssl_proxies_set_ssl_certificates_request_resource is not None:
                request.target_ssl_proxies_set_ssl_certificates_request_resource = (
                    target_ssl_proxies_set_ssl_certificates_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_ssl_certificates]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def set_ssl_policy_unary(
        self,
        request: Optional[
            Union[compute.SetSslPolicyTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        ssl_policy_reference_resource: Optional[compute.SslPolicyReference] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> compute.Operation:
        r"""Sets the SSL policy for TargetSslProxy. The SSL
        policy specifies the server-side support for SSL
        features. This affects connections between clients and
        the load balancer. They do not affect the connection
        between the load balancer and the backends.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_ssl_policy():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetSslPolicyTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_ssl_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetSslPolicyTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetSslPolicy. See the
                method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose SSL policy is to be set. The name
                must be 1-63 characters long, and comply
                with RFC1035.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ssl_policy_reference_resource (google.cloud.compute_v1.types.SslPolicyReference):
                The body resource for this request
                This corresponds to the ``ssl_policy_reference_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project, target_ssl_proxy, ssl_policy_reference_resource]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetSslPolicyTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetSslPolicyTargetSslProxyRequest):
            request = compute.SetSslPolicyTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if ssl_policy_reference_resource is not None:
                request.ssl_policy_reference_resource = ssl_policy_reference_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_ssl_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def set_ssl_policy(
        self,
        request: Optional[
            Union[compute.SetSslPolicyTargetSslProxyRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        target_ssl_proxy: Optional[str] = None,
        ssl_policy_reference_resource: Optional[compute.SslPolicyReference] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Sets the SSL policy for TargetSslProxy. The SSL
        policy specifies the server-side support for SSL
        features. This affects connections between clients and
        the load balancer. They do not affect the connection
        between the load balancer and the backends.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1

            def sample_set_ssl_policy():
                # Create a client
                client = compute_v1.TargetSslProxiesClient()

                # Initialize request argument(s)
                request = compute_v1.SetSslPolicyTargetSslProxyRequest(
                    project="project_value",
                    target_ssl_proxy="target_ssl_proxy_value",
                )

                # Make the request
                response = client.set_ssl_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1.types.SetSslPolicyTargetSslProxyRequest, dict]):
                The request object. A request message for
                TargetSslProxies.SetSslPolicy. See the
                method description for details.
            project (str):
                Project ID for this request.
                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_ssl_proxy (str):
                Name of the TargetSslProxy resource
                whose SSL policy is to be set. The name
                must be 1-63 characters long, and comply
                with RFC1035.

                This corresponds to the ``target_ssl_proxy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ssl_policy_reference_resource (google.cloud.compute_v1.types.SslPolicyReference):
                The body resource for this request
                This corresponds to the ``ssl_policy_reference_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project, target_ssl_proxy, ssl_policy_reference_resource]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a compute.SetSslPolicyTargetSslProxyRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, compute.SetSslPolicyTargetSslProxyRequest):
            request = compute.SetSslPolicyTargetSslProxyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project is not None:
                request.project = project
            if target_ssl_proxy is not None:
                request.target_ssl_proxy = target_ssl_proxy
            if ssl_policy_reference_resource is not None:
                request.ssl_policy_reference_resource = ssl_policy_reference_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_ssl_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("target_ssl_proxy", request.target_ssl_proxy),
                )
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_operations_client
        operation_request = compute.GetGlobalOperationRequest()
        operation_request.project = request.project
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def __enter__(self) -> "TargetSslProxiesClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("TargetSslProxiesClient",)
