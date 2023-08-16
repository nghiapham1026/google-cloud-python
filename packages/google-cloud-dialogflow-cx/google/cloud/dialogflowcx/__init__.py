# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.cloud.dialogflowcx import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.dialogflowcx_v3.services.agents.async_client import AgentsAsyncClient
from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
from google.cloud.dialogflowcx_v3.services.changelogs.async_client import (
    ChangelogsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.changelogs.client import ChangelogsClient
from google.cloud.dialogflowcx_v3.services.deployments.async_client import (
    DeploymentsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.deployments.client import DeploymentsClient
from google.cloud.dialogflowcx_v3.services.entity_types.async_client import (
    EntityTypesAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.entity_types.client import EntityTypesClient
from google.cloud.dialogflowcx_v3.services.environments.async_client import (
    EnvironmentsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.environments.client import EnvironmentsClient
from google.cloud.dialogflowcx_v3.services.experiments.async_client import (
    ExperimentsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.experiments.client import ExperimentsClient
from google.cloud.dialogflowcx_v3.services.flows.async_client import FlowsAsyncClient
from google.cloud.dialogflowcx_v3.services.flows.client import FlowsClient
from google.cloud.dialogflowcx_v3.services.intents.async_client import (
    IntentsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.intents.client import IntentsClient
from google.cloud.dialogflowcx_v3.services.pages.async_client import PagesAsyncClient
from google.cloud.dialogflowcx_v3.services.pages.client import PagesClient
from google.cloud.dialogflowcx_v3.services.security_settings_service.async_client import (
    SecuritySettingsServiceAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.security_settings_service.client import (
    SecuritySettingsServiceClient,
)
from google.cloud.dialogflowcx_v3.services.session_entity_types.async_client import (
    SessionEntityTypesAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.session_entity_types.client import (
    SessionEntityTypesClient,
)
from google.cloud.dialogflowcx_v3.services.sessions.async_client import (
    SessionsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.sessions.client import SessionsClient
from google.cloud.dialogflowcx_v3.services.test_cases.async_client import (
    TestCasesAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.test_cases.client import TestCasesClient
from google.cloud.dialogflowcx_v3.services.transition_route_groups.async_client import (
    TransitionRouteGroupsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.transition_route_groups.client import (
    TransitionRouteGroupsClient,
)
from google.cloud.dialogflowcx_v3.services.versions.async_client import (
    VersionsAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.versions.client import VersionsClient
from google.cloud.dialogflowcx_v3.services.webhooks.async_client import (
    WebhooksAsyncClient,
)
from google.cloud.dialogflowcx_v3.services.webhooks.client import WebhooksClient
from google.cloud.dialogflowcx_v3.types.advanced_settings import AdvancedSettings
from google.cloud.dialogflowcx_v3.types.agent import (
    Agent,
    AgentValidationResult,
    CreateAgentRequest,
    DeleteAgentRequest,
    ExportAgentRequest,
    ExportAgentResponse,
    GetAgentRequest,
    GetAgentValidationResultRequest,
    ListAgentsRequest,
    ListAgentsResponse,
    RestoreAgentRequest,
    SpeechToTextSettings,
    UpdateAgentRequest,
    ValidateAgentRequest,
)
from google.cloud.dialogflowcx_v3.types.audio_config import (
    AudioEncoding,
    InputAudioConfig,
    OutputAudioConfig,
    OutputAudioEncoding,
    SpeechModelVariant,
    SpeechWordInfo,
    SsmlVoiceGender,
    SynthesizeSpeechConfig,
    TextToSpeechSettings,
    VoiceSelectionParams,
)
from google.cloud.dialogflowcx_v3.types.changelog import (
    Changelog,
    GetChangelogRequest,
    ListChangelogsRequest,
    ListChangelogsResponse,
)
from google.cloud.dialogflowcx_v3.types.deployment import (
    Deployment,
    GetDeploymentRequest,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
)
from google.cloud.dialogflowcx_v3.types.entity_type import (
    CreateEntityTypeRequest,
    DeleteEntityTypeRequest,
    EntityType,
    GetEntityTypeRequest,
    ListEntityTypesRequest,
    ListEntityTypesResponse,
    UpdateEntityTypeRequest,
)
from google.cloud.dialogflowcx_v3.types.environment import (
    ContinuousTestResult,
    CreateEnvironmentRequest,
    DeleteEnvironmentRequest,
    DeployFlowMetadata,
    DeployFlowRequest,
    DeployFlowResponse,
    Environment,
    GetEnvironmentRequest,
    ListContinuousTestResultsRequest,
    ListContinuousTestResultsResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    LookupEnvironmentHistoryRequest,
    LookupEnvironmentHistoryResponse,
    RunContinuousTestMetadata,
    RunContinuousTestRequest,
    RunContinuousTestResponse,
    UpdateEnvironmentRequest,
)
from google.cloud.dialogflowcx_v3.types.experiment import (
    CreateExperimentRequest,
    DeleteExperimentRequest,
    Experiment,
    GetExperimentRequest,
    ListExperimentsRequest,
    ListExperimentsResponse,
    RolloutConfig,
    RolloutState,
    StartExperimentRequest,
    StopExperimentRequest,
    UpdateExperimentRequest,
    VariantsHistory,
    VersionVariants,
)
from google.cloud.dialogflowcx_v3.types.flow import (
    CreateFlowRequest,
    DeleteFlowRequest,
    ExportFlowRequest,
    ExportFlowResponse,
    Flow,
    FlowImportStrategy,
    FlowValidationResult,
    GetFlowRequest,
    GetFlowValidationResultRequest,
    ImportFlowRequest,
    ImportFlowResponse,
    ListFlowsRequest,
    ListFlowsResponse,
    NluSettings,
    TrainFlowRequest,
    UpdateFlowRequest,
    ValidateFlowRequest,
)
from google.cloud.dialogflowcx_v3.types.fulfillment import Fulfillment
from google.cloud.dialogflowcx_v3.types.gcs import GcsDestination
from google.cloud.dialogflowcx_v3.types.import_strategy import ImportStrategy
from google.cloud.dialogflowcx_v3.types.intent import (
    CreateIntentRequest,
    DeleteIntentRequest,
    GetIntentRequest,
    Intent,
    IntentView,
    ListIntentsRequest,
    ListIntentsResponse,
    UpdateIntentRequest,
)
from google.cloud.dialogflowcx_v3.types.page import (
    CreatePageRequest,
    DeletePageRequest,
    EventHandler,
    Form,
    GetPageRequest,
    ListPagesRequest,
    ListPagesResponse,
    Page,
    TransitionRoute,
    UpdatePageRequest,
)
from google.cloud.dialogflowcx_v3.types.response_message import ResponseMessage
from google.cloud.dialogflowcx_v3.types.security_settings import (
    CreateSecuritySettingsRequest,
    DeleteSecuritySettingsRequest,
    GetSecuritySettingsRequest,
    ListSecuritySettingsRequest,
    ListSecuritySettingsResponse,
    SecuritySettings,
    UpdateSecuritySettingsRequest,
)
from google.cloud.dialogflowcx_v3.types.session import (
    AudioInput,
    CloudConversationDebuggingInfo,
    DetectIntentRequest,
    DetectIntentResponse,
    DtmfInput,
    EventInput,
    FulfillIntentRequest,
    FulfillIntentResponse,
    IntentInput,
    Match,
    MatchIntentRequest,
    MatchIntentResponse,
    QueryInput,
    QueryParameters,
    QueryResult,
    SentimentAnalysisResult,
    StreamingDetectIntentRequest,
    StreamingDetectIntentResponse,
    StreamingRecognitionResult,
    TextInput,
)
from google.cloud.dialogflowcx_v3.types.session_entity_type import (
    CreateSessionEntityTypeRequest,
    DeleteSessionEntityTypeRequest,
    GetSessionEntityTypeRequest,
    ListSessionEntityTypesRequest,
    ListSessionEntityTypesResponse,
    SessionEntityType,
    UpdateSessionEntityTypeRequest,
)
from google.cloud.dialogflowcx_v3.types.test_case import (
    BatchDeleteTestCasesRequest,
    BatchRunTestCasesMetadata,
    BatchRunTestCasesRequest,
    BatchRunTestCasesResponse,
    CalculateCoverageRequest,
    CalculateCoverageResponse,
    ConversationTurn,
    CreateTestCaseRequest,
    ExportTestCasesMetadata,
    ExportTestCasesRequest,
    ExportTestCasesResponse,
    GetTestCaseRequest,
    GetTestCaseResultRequest,
    ImportTestCasesMetadata,
    ImportTestCasesRequest,
    ImportTestCasesResponse,
    IntentCoverage,
    ListTestCaseResultsRequest,
    ListTestCaseResultsResponse,
    ListTestCasesRequest,
    ListTestCasesResponse,
    RunTestCaseMetadata,
    RunTestCaseRequest,
    RunTestCaseResponse,
    TestCase,
    TestCaseError,
    TestCaseResult,
    TestConfig,
    TestError,
    TestResult,
    TestRunDifference,
    TransitionCoverage,
    TransitionRouteGroupCoverage,
    UpdateTestCaseRequest,
)
from google.cloud.dialogflowcx_v3.types.transition_route_group import (
    CreateTransitionRouteGroupRequest,
    DeleteTransitionRouteGroupRequest,
    GetTransitionRouteGroupRequest,
    ListTransitionRouteGroupsRequest,
    ListTransitionRouteGroupsResponse,
    TransitionRouteGroup,
    UpdateTransitionRouteGroupRequest,
)
from google.cloud.dialogflowcx_v3.types.validation_message import (
    ResourceName,
    ValidationMessage,
)
from google.cloud.dialogflowcx_v3.types.version import (
    CompareVersionsRequest,
    CompareVersionsResponse,
    CreateVersionOperationMetadata,
    CreateVersionRequest,
    DeleteVersionRequest,
    GetVersionRequest,
    ListVersionsRequest,
    ListVersionsResponse,
    LoadVersionRequest,
    UpdateVersionRequest,
    Version,
)
from google.cloud.dialogflowcx_v3.types.webhook import (
    CreateWebhookRequest,
    DeleteWebhookRequest,
    GetWebhookRequest,
    ListWebhooksRequest,
    ListWebhooksResponse,
    PageInfo,
    SessionInfo,
    UpdateWebhookRequest,
    Webhook,
    WebhookRequest,
    WebhookResponse,
)

__all__ = (
    "AgentsClient",
    "AgentsAsyncClient",
    "ChangelogsClient",
    "ChangelogsAsyncClient",
    "DeploymentsClient",
    "DeploymentsAsyncClient",
    "EntityTypesClient",
    "EntityTypesAsyncClient",
    "EnvironmentsClient",
    "EnvironmentsAsyncClient",
    "ExperimentsClient",
    "ExperimentsAsyncClient",
    "FlowsClient",
    "FlowsAsyncClient",
    "IntentsClient",
    "IntentsAsyncClient",
    "PagesClient",
    "PagesAsyncClient",
    "SecuritySettingsServiceClient",
    "SecuritySettingsServiceAsyncClient",
    "SessionEntityTypesClient",
    "SessionEntityTypesAsyncClient",
    "SessionsClient",
    "SessionsAsyncClient",
    "TestCasesClient",
    "TestCasesAsyncClient",
    "TransitionRouteGroupsClient",
    "TransitionRouteGroupsAsyncClient",
    "VersionsClient",
    "VersionsAsyncClient",
    "WebhooksClient",
    "WebhooksAsyncClient",
    "AdvancedSettings",
    "Agent",
    "AgentValidationResult",
    "CreateAgentRequest",
    "DeleteAgentRequest",
    "ExportAgentRequest",
    "ExportAgentResponse",
    "GetAgentRequest",
    "GetAgentValidationResultRequest",
    "ListAgentsRequest",
    "ListAgentsResponse",
    "RestoreAgentRequest",
    "SpeechToTextSettings",
    "UpdateAgentRequest",
    "ValidateAgentRequest",
    "InputAudioConfig",
    "OutputAudioConfig",
    "SpeechWordInfo",
    "SynthesizeSpeechConfig",
    "TextToSpeechSettings",
    "VoiceSelectionParams",
    "AudioEncoding",
    "OutputAudioEncoding",
    "SpeechModelVariant",
    "SsmlVoiceGender",
    "Changelog",
    "GetChangelogRequest",
    "ListChangelogsRequest",
    "ListChangelogsResponse",
    "Deployment",
    "GetDeploymentRequest",
    "ListDeploymentsRequest",
    "ListDeploymentsResponse",
    "CreateEntityTypeRequest",
    "DeleteEntityTypeRequest",
    "EntityType",
    "GetEntityTypeRequest",
    "ListEntityTypesRequest",
    "ListEntityTypesResponse",
    "UpdateEntityTypeRequest",
    "ContinuousTestResult",
    "CreateEnvironmentRequest",
    "DeleteEnvironmentRequest",
    "DeployFlowMetadata",
    "DeployFlowRequest",
    "DeployFlowResponse",
    "Environment",
    "GetEnvironmentRequest",
    "ListContinuousTestResultsRequest",
    "ListContinuousTestResultsResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "LookupEnvironmentHistoryRequest",
    "LookupEnvironmentHistoryResponse",
    "RunContinuousTestMetadata",
    "RunContinuousTestRequest",
    "RunContinuousTestResponse",
    "UpdateEnvironmentRequest",
    "CreateExperimentRequest",
    "DeleteExperimentRequest",
    "Experiment",
    "GetExperimentRequest",
    "ListExperimentsRequest",
    "ListExperimentsResponse",
    "RolloutConfig",
    "RolloutState",
    "StartExperimentRequest",
    "StopExperimentRequest",
    "UpdateExperimentRequest",
    "VariantsHistory",
    "VersionVariants",
    "CreateFlowRequest",
    "DeleteFlowRequest",
    "ExportFlowRequest",
    "ExportFlowResponse",
    "Flow",
    "FlowImportStrategy",
    "FlowValidationResult",
    "GetFlowRequest",
    "GetFlowValidationResultRequest",
    "ImportFlowRequest",
    "ImportFlowResponse",
    "ListFlowsRequest",
    "ListFlowsResponse",
    "NluSettings",
    "TrainFlowRequest",
    "UpdateFlowRequest",
    "ValidateFlowRequest",
    "Fulfillment",
    "GcsDestination",
    "ImportStrategy",
    "CreateIntentRequest",
    "DeleteIntentRequest",
    "GetIntentRequest",
    "Intent",
    "ListIntentsRequest",
    "ListIntentsResponse",
    "UpdateIntentRequest",
    "IntentView",
    "CreatePageRequest",
    "DeletePageRequest",
    "EventHandler",
    "Form",
    "GetPageRequest",
    "ListPagesRequest",
    "ListPagesResponse",
    "Page",
    "TransitionRoute",
    "UpdatePageRequest",
    "ResponseMessage",
    "CreateSecuritySettingsRequest",
    "DeleteSecuritySettingsRequest",
    "GetSecuritySettingsRequest",
    "ListSecuritySettingsRequest",
    "ListSecuritySettingsResponse",
    "SecuritySettings",
    "UpdateSecuritySettingsRequest",
    "AudioInput",
    "CloudConversationDebuggingInfo",
    "DetectIntentRequest",
    "DetectIntentResponse",
    "DtmfInput",
    "EventInput",
    "FulfillIntentRequest",
    "FulfillIntentResponse",
    "IntentInput",
    "Match",
    "MatchIntentRequest",
    "MatchIntentResponse",
    "QueryInput",
    "QueryParameters",
    "QueryResult",
    "SentimentAnalysisResult",
    "StreamingDetectIntentRequest",
    "StreamingDetectIntentResponse",
    "StreamingRecognitionResult",
    "TextInput",
    "CreateSessionEntityTypeRequest",
    "DeleteSessionEntityTypeRequest",
    "GetSessionEntityTypeRequest",
    "ListSessionEntityTypesRequest",
    "ListSessionEntityTypesResponse",
    "SessionEntityType",
    "UpdateSessionEntityTypeRequest",
    "BatchDeleteTestCasesRequest",
    "BatchRunTestCasesMetadata",
    "BatchRunTestCasesRequest",
    "BatchRunTestCasesResponse",
    "CalculateCoverageRequest",
    "CalculateCoverageResponse",
    "ConversationTurn",
    "CreateTestCaseRequest",
    "ExportTestCasesMetadata",
    "ExportTestCasesRequest",
    "ExportTestCasesResponse",
    "GetTestCaseRequest",
    "GetTestCaseResultRequest",
    "ImportTestCasesMetadata",
    "ImportTestCasesRequest",
    "ImportTestCasesResponse",
    "IntentCoverage",
    "ListTestCaseResultsRequest",
    "ListTestCaseResultsResponse",
    "ListTestCasesRequest",
    "ListTestCasesResponse",
    "RunTestCaseMetadata",
    "RunTestCaseRequest",
    "RunTestCaseResponse",
    "TestCase",
    "TestCaseError",
    "TestCaseResult",
    "TestConfig",
    "TestError",
    "TestRunDifference",
    "TransitionCoverage",
    "TransitionRouteGroupCoverage",
    "UpdateTestCaseRequest",
    "TestResult",
    "CreateTransitionRouteGroupRequest",
    "DeleteTransitionRouteGroupRequest",
    "GetTransitionRouteGroupRequest",
    "ListTransitionRouteGroupsRequest",
    "ListTransitionRouteGroupsResponse",
    "TransitionRouteGroup",
    "UpdateTransitionRouteGroupRequest",
    "ResourceName",
    "ValidationMessage",
    "CompareVersionsRequest",
    "CompareVersionsResponse",
    "CreateVersionOperationMetadata",
    "CreateVersionRequest",
    "DeleteVersionRequest",
    "GetVersionRequest",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "LoadVersionRequest",
    "UpdateVersionRequest",
    "Version",
    "CreateWebhookRequest",
    "DeleteWebhookRequest",
    "GetWebhookRequest",
    "ListWebhooksRequest",
    "ListWebhooksResponse",
    "PageInfo",
    "SessionInfo",
    "UpdateWebhookRequest",
    "Webhook",
    "WebhookRequest",
    "WebhookResponse",
)
