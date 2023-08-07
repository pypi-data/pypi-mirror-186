"""
Type annotations for sagemaker service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker.client import SageMakerClient

    session = Session()
    client: SageMakerClient = session.client("sagemaker")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Mapping, Sequence, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActionStatusType,
    AlgorithmSortByType,
    AppImageConfigSortKeyType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppTypeType,
    AssociationEdgeTypeType,
    AuthModeType,
    AutoMLJobStatusType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    BatchStrategyType,
    CandidateSortByType,
    CandidateStatusType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    DirectInternetAccessType,
    DirectionType,
    EdgePackagingJobStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    HubContentSortByType,
    HubContentTypeType,
    HubSortByType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    ImageSortByType,
    ImageSortOrderType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    InferenceExperimentStatusType,
    InferenceExperimentStopDesiredStateType,
    InstanceTypeType,
    JobTypeType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelPackageGroupSortByType,
    ModelPackageSortByType,
    ModelPackageTypeType,
    ModelSortKeyType,
    ModelVariantActionType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    OfflineStoreStatusValueType,
    OrderKeyType,
    ProblemTypeType,
    ProcessingJobStatusType,
    ProcessorType,
    ProjectSortByType,
    ProjectSortOrderType,
    RecommendationJobStatusType,
    RecommendationJobTypeType,
    ResourceTypeType,
    RootAccessType,
    ScheduleStatusType,
    SearchSortOrderType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortInferenceExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SpaceSortKeyType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformJobStatusType,
    UserProfileSortKeyType,
    VendorGuidanceType,
    WarmPoolResourceStatusType,
)
from .paginator import (
    ListActionsPaginator,
    ListAlgorithmsPaginator,
    ListAliasesPaginator,
    ListAppImageConfigsPaginator,
    ListAppsPaginator,
    ListArtifactsPaginator,
    ListAssociationsPaginator,
    ListAutoMLJobsPaginator,
    ListCandidatesForAutoMLJobPaginator,
    ListCodeRepositoriesPaginator,
    ListCompilationJobsPaginator,
    ListContextsPaginator,
    ListDataQualityJobDefinitionsPaginator,
    ListDeviceFleetsPaginator,
    ListDevicesPaginator,
    ListDomainsPaginator,
    ListEdgeDeploymentPlansPaginator,
    ListEdgePackagingJobsPaginator,
    ListEndpointConfigsPaginator,
    ListEndpointsPaginator,
    ListExperimentsPaginator,
    ListFeatureGroupsPaginator,
    ListFlowDefinitionsPaginator,
    ListHumanTaskUisPaginator,
    ListHyperParameterTuningJobsPaginator,
    ListImagesPaginator,
    ListImageVersionsPaginator,
    ListInferenceExperimentsPaginator,
    ListInferenceRecommendationsJobsPaginator,
    ListInferenceRecommendationsJobStepsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListLineageGroupsPaginator,
    ListModelBiasJobDefinitionsPaginator,
    ListModelCardExportJobsPaginator,
    ListModelCardsPaginator,
    ListModelCardVersionsPaginator,
    ListModelExplainabilityJobDefinitionsPaginator,
    ListModelMetadataPaginator,
    ListModelPackageGroupsPaginator,
    ListModelPackagesPaginator,
    ListModelQualityJobDefinitionsPaginator,
    ListModelsPaginator,
    ListMonitoringAlertHistoryPaginator,
    ListMonitoringAlertsPaginator,
    ListMonitoringExecutionsPaginator,
    ListMonitoringSchedulesPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelineExecutionStepsPaginator,
    ListPipelineParametersForExecutionPaginator,
    ListPipelinesPaginator,
    ListProcessingJobsPaginator,
    ListSpacesPaginator,
    ListStageDevicesPaginator,
    ListStudioLifecycleConfigsPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListTrialComponentsPaginator,
    ListTrialsPaginator,
    ListUserProfilesPaginator,
    ListWorkforcesPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from .type_defs import (
    ActionSourceTypeDef,
    AddAssociationResponseTypeDef,
    AdditionalInferenceSpecificationDefinitionTypeDef,
    AddTagsOutputTypeDef,
    AlgorithmSpecificationTypeDef,
    AlgorithmValidationSpecificationTypeDef,
    AppSpecificationTypeDef,
    ArtifactSourceTypeDef,
    AssociateTrialComponentResponseTypeDef,
    AsyncInferenceConfigTypeDef,
    AutoMLChannelTypeDef,
    AutoMLJobConfigTypeDef,
    AutoMLJobObjectiveTypeDef,
    AutoMLOutputDataConfigTypeDef,
    BatchDataCaptureConfigTypeDef,
    BatchDescribeModelPackageOutputTypeDef,
    ChannelTypeDef,
    CheckpointConfigTypeDef,
    CognitoConfigTypeDef,
    ContainerDefinitionTypeDef,
    ContextSourceTypeDef,
    CreateActionResponseTypeDef,
    CreateAlgorithmOutputTypeDef,
    CreateAppImageConfigResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateArtifactResponseTypeDef,
    CreateAutoMLJobResponseTypeDef,
    CreateCodeRepositoryOutputTypeDef,
    CreateCompilationJobResponseTypeDef,
    CreateContextResponseTypeDef,
    CreateDataQualityJobDefinitionResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEdgeDeploymentPlanResponseTypeDef,
    CreateEndpointConfigOutputTypeDef,
    CreateEndpointOutputTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFeatureGroupResponseTypeDef,
    CreateFlowDefinitionResponseTypeDef,
    CreateHubResponseTypeDef,
    CreateHumanTaskUiResponseTypeDef,
    CreateHyperParameterTuningJobResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateImageVersionResponseTypeDef,
    CreateInferenceExperimentResponseTypeDef,
    CreateInferenceRecommendationsJobResponseTypeDef,
    CreateLabelingJobResponseTypeDef,
    CreateModelBiasJobDefinitionResponseTypeDef,
    CreateModelCardExportJobResponseTypeDef,
    CreateModelCardResponseTypeDef,
    CreateModelExplainabilityJobDefinitionResponseTypeDef,
    CreateModelOutputTypeDef,
    CreateModelPackageGroupOutputTypeDef,
    CreateModelPackageOutputTypeDef,
    CreateModelQualityJobDefinitionResponseTypeDef,
    CreateMonitoringScheduleResponseTypeDef,
    CreateNotebookInstanceLifecycleConfigOutputTypeDef,
    CreateNotebookInstanceOutputTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresignedDomainUrlResponseTypeDef,
    CreatePresignedNotebookInstanceUrlOutputTypeDef,
    CreateProcessingJobResponseTypeDef,
    CreateProjectOutputTypeDef,
    CreateSpaceResponseTypeDef,
    CreateStudioLifecycleConfigResponseTypeDef,
    CreateTrainingJobResponseTypeDef,
    CreateTransformJobResponseTypeDef,
    CreateTrialComponentResponseTypeDef,
    CreateTrialResponseTypeDef,
    CreateUserProfileResponseTypeDef,
    CreateWorkforceResponseTypeDef,
    CreateWorkteamResponseTypeDef,
    DataCaptureConfigTypeDef,
    DataProcessingTypeDef,
    DataQualityAppSpecificationTypeDef,
    DataQualityBaselineConfigTypeDef,
    DataQualityJobInputTypeDef,
    DebugHookConfigTypeDef,
    DebugRuleConfigurationTypeDef,
    DefaultSpaceSettingsTypeDef,
    DeleteActionResponseTypeDef,
    DeleteArtifactResponseTypeDef,
    DeleteAssociationResponseTypeDef,
    DeleteContextResponseTypeDef,
    DeleteExperimentResponseTypeDef,
    DeleteInferenceExperimentResponseTypeDef,
    DeletePipelineResponseTypeDef,
    DeleteTrialComponentResponseTypeDef,
    DeleteTrialResponseTypeDef,
    DeleteWorkteamResponseTypeDef,
    DeploymentConfigTypeDef,
    DeploymentStageTypeDef,
    DescribeActionResponseTypeDef,
    DescribeAlgorithmOutputTypeDef,
    DescribeAppImageConfigResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeArtifactResponseTypeDef,
    DescribeAutoMLJobResponseTypeDef,
    DescribeCodeRepositoryOutputTypeDef,
    DescribeCompilationJobResponseTypeDef,
    DescribeContextResponseTypeDef,
    DescribeDataQualityJobDefinitionResponseTypeDef,
    DescribeDeviceFleetResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeEdgeDeploymentPlanResponseTypeDef,
    DescribeEdgePackagingJobResponseTypeDef,
    DescribeEndpointConfigOutputTypeDef,
    DescribeEndpointOutputTypeDef,
    DescribeExperimentResponseTypeDef,
    DescribeFeatureGroupResponseTypeDef,
    DescribeFeatureMetadataResponseTypeDef,
    DescribeFlowDefinitionResponseTypeDef,
    DescribeHubContentResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeHumanTaskUiResponseTypeDef,
    DescribeHyperParameterTuningJobResponseTypeDef,
    DescribeImageResponseTypeDef,
    DescribeImageVersionResponseTypeDef,
    DescribeInferenceExperimentResponseTypeDef,
    DescribeInferenceRecommendationsJobResponseTypeDef,
    DescribeLabelingJobResponseTypeDef,
    DescribeLineageGroupResponseTypeDef,
    DescribeModelBiasJobDefinitionResponseTypeDef,
    DescribeModelCardExportJobResponseTypeDef,
    DescribeModelCardResponseTypeDef,
    DescribeModelExplainabilityJobDefinitionResponseTypeDef,
    DescribeModelOutputTypeDef,
    DescribeModelPackageGroupOutputTypeDef,
    DescribeModelPackageOutputTypeDef,
    DescribeModelQualityJobDefinitionResponseTypeDef,
    DescribeMonitoringScheduleResponseTypeDef,
    DescribeNotebookInstanceLifecycleConfigOutputTypeDef,
    DescribeNotebookInstanceOutputTypeDef,
    DescribePipelineDefinitionForExecutionResponseTypeDef,
    DescribePipelineExecutionResponseTypeDef,
    DescribePipelineResponseTypeDef,
    DescribeProcessingJobResponseTypeDef,
    DescribeProjectOutputTypeDef,
    DescribeSpaceResponseTypeDef,
    DescribeStudioLifecycleConfigResponseTypeDef,
    DescribeSubscribedWorkteamResponseTypeDef,
    DescribeTrainingJobResponseTypeDef,
    DescribeTransformJobResponseTypeDef,
    DescribeTrialComponentResponseTypeDef,
    DescribeTrialResponseTypeDef,
    DescribeUserProfileResponseTypeDef,
    DescribeWorkforceResponseTypeDef,
    DescribeWorkteamResponseTypeDef,
    DesiredWeightAndCapacityTypeDef,
    DeviceTypeDef,
    DisassociateTrialComponentResponseTypeDef,
    DomainSettingsForUpdateTypeDef,
    DomainSettingsTypeDef,
    DriftCheckBaselinesTypeDef,
    EdgeDeploymentModelConfigTypeDef,
    EdgeOutputConfigTypeDef,
    EmptyResponseMetadataTypeDef,
    ExperimentConfigTypeDef,
    ExplainerConfigTypeDef,
    FeatureDefinitionTypeDef,
    FeatureParameterTypeDef,
    FlowDefinitionOutputConfigTypeDef,
    GetDeviceFleetReportResponseTypeDef,
    GetLineageGroupPolicyResponseTypeDef,
    GetModelPackageGroupPolicyOutputTypeDef,
    GetSagemakerServicecatalogPortfolioStatusOutputTypeDef,
    GetSearchSuggestionsResponseTypeDef,
    GitConfigForUpdateTypeDef,
    GitConfigTypeDef,
    HubS3StorageConfigTypeDef,
    HumanLoopActivationConfigTypeDef,
    HumanLoopConfigTypeDef,
    HumanLoopRequestSourceTypeDef,
    HumanTaskConfigTypeDef,
    HyperParameterTrainingJobDefinitionTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    HyperParameterTuningJobWarmStartConfigTypeDef,
    ImportHubContentResponseTypeDef,
    InferenceExecutionConfigTypeDef,
    InferenceExperimentDataStorageConfigTypeDef,
    InferenceExperimentScheduleTypeDef,
    InferenceSpecificationTypeDef,
    InputConfigTypeDef,
    InstanceMetadataServiceConfigurationTypeDef,
    KernelGatewayImageConfigTypeDef,
    LabelingJobAlgorithmsConfigTypeDef,
    LabelingJobInputConfigTypeDef,
    LabelingJobOutputConfigTypeDef,
    LabelingJobStoppingConditionsTypeDef,
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAliasesResponseTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgeDeploymentPlansResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHubContentsResponseTypeDef,
    ListHubContentVersionsResponseTypeDef,
    ListHubsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListInferenceExperimentsResponseTypeDef,
    ListInferenceRecommendationsJobsResponseTypeDef,
    ListInferenceRecommendationsJobStepsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListLineageGroupsResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelCardExportJobsResponseTypeDef,
    ListModelCardsResponseTypeDef,
    ListModelCardVersionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelMetadataResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringAlertHistoryResponseTypeDef,
    ListMonitoringAlertsResponseTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListProjectsOutputTypeDef,
    ListSpacesResponseTypeDef,
    ListStageDevicesResponseTypeDef,
    ListStudioLifecycleConfigsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    MemberDefinitionTypeDef,
    MetadataPropertiesTypeDef,
    ModelBiasAppSpecificationTypeDef,
    ModelBiasBaselineConfigTypeDef,
    ModelBiasJobInputTypeDef,
    ModelCardExportOutputConfigTypeDef,
    ModelCardSecurityConfigTypeDef,
    ModelClientConfigTypeDef,
    ModelDeployConfigTypeDef,
    ModelExplainabilityAppSpecificationTypeDef,
    ModelExplainabilityBaselineConfigTypeDef,
    ModelExplainabilityJobInputTypeDef,
    ModelMetadataSearchExpressionTypeDef,
    ModelMetricsTypeDef,
    ModelPackageValidationSpecificationTypeDef,
    ModelQualityAppSpecificationTypeDef,
    ModelQualityBaselineConfigTypeDef,
    ModelQualityJobInputTypeDef,
    ModelVariantConfigTypeDef,
    MonitoringNetworkConfigTypeDef,
    MonitoringOutputConfigTypeDef,
    MonitoringResourcesTypeDef,
    MonitoringScheduleConfigTypeDef,
    MonitoringStoppingConditionTypeDef,
    NeoVpcConfigTypeDef,
    NetworkConfigTypeDef,
    NotebookInstanceLifecycleHookTypeDef,
    NotificationConfigurationTypeDef,
    OfflineStoreConfigTypeDef,
    OidcConfigTypeDef,
    OnlineStoreConfigTypeDef,
    OutputConfigTypeDef,
    OutputDataConfigTypeDef,
    OutputParameterTypeDef,
    ParallelismConfigurationTypeDef,
    ParameterTypeDef,
    PipelineDefinitionS3LocationTypeDef,
    ProcessingInputTypeDef,
    ProcessingOutputConfigTypeDef,
    ProcessingResourcesTypeDef,
    ProcessingStoppingConditionTypeDef,
    ProductionVariantTypeDef,
    ProfilerConfigForUpdateTypeDef,
    ProfilerConfigTypeDef,
    ProfilerRuleConfigurationTypeDef,
    PutModelPackageGroupPolicyOutputTypeDef,
    QueryFiltersTypeDef,
    QueryLineageResponseTypeDef,
    RecommendationJobInputConfigTypeDef,
    RecommendationJobOutputConfigTypeDef,
    RecommendationJobStoppingConditionsTypeDef,
    RenderableTaskTypeDef,
    RenderUiTemplateResponseTypeDef,
    ResourceConfigForUpdateTypeDef,
    ResourceConfigTypeDef,
    ResourceSpecTypeDef,
    RetentionPolicyTypeDef,
    RetryPipelineExecutionResponseTypeDef,
    RetryStrategyTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
    SendPipelineExecutionStepFailureResponseTypeDef,
    SendPipelineExecutionStepSuccessResponseTypeDef,
    ServiceCatalogProvisioningDetailsTypeDef,
    ServiceCatalogProvisioningUpdateDetailsTypeDef,
    ShadowModeConfigTypeDef,
    SourceAlgorithmSpecificationTypeDef,
    SourceIpConfigTypeDef,
    SpaceSettingsTypeDef,
    StartInferenceExperimentResponseTypeDef,
    StartPipelineExecutionResponseTypeDef,
    StopInferenceExperimentResponseTypeDef,
    StoppingConditionTypeDef,
    StopPipelineExecutionResponseTypeDef,
    SuggestionQueryTypeDef,
    TagTypeDef,
    TensorBoardOutputConfigTypeDef,
    TrainingSpecificationTypeDef,
    TransformInputTypeDef,
    TransformOutputTypeDef,
    TransformResourcesTypeDef,
    TrialComponentArtifactTypeDef,
    TrialComponentParameterValueTypeDef,
    TrialComponentStatusTypeDef,
    UiTemplateTypeDef,
    UpdateActionResponseTypeDef,
    UpdateAppImageConfigResponseTypeDef,
    UpdateArtifactResponseTypeDef,
    UpdateCodeRepositoryOutputTypeDef,
    UpdateContextResponseTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEndpointOutputTypeDef,
    UpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateFeatureGroupResponseTypeDef,
    UpdateHubResponseTypeDef,
    UpdateImageResponseTypeDef,
    UpdateImageVersionResponseTypeDef,
    UpdateInferenceExperimentResponseTypeDef,
    UpdateModelCardResponseTypeDef,
    UpdateModelPackageOutputTypeDef,
    UpdateMonitoringAlertResponseTypeDef,
    UpdateMonitoringScheduleResponseTypeDef,
    UpdatePipelineExecutionResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSpaceResponseTypeDef,
    UpdateTrainingJobResponseTypeDef,
    UpdateTrialComponentResponseTypeDef,
    UpdateTrialResponseTypeDef,
    UpdateUserProfileResponseTypeDef,
    UpdateWorkforceResponseTypeDef,
    UpdateWorkteamResponseTypeDef,
    UserSettingsTypeDef,
    VariantPropertyTypeDef,
    VpcConfigTypeDef,
    WorkforceVpcConfigRequestTypeDef,
)
from .waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    ImageCreatedWaiter,
    ImageDeletedWaiter,
    ImageUpdatedWaiter,
    ImageVersionCreatedWaiter,
    ImageVersionDeletedWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    ProcessingJobCompletedOrStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SageMakerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]


class SageMakerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#exceptions)
        """

    def add_association(
        self, *, SourceArn: str, DestinationArn: str, AssociationType: AssociationEdgeTypeType = ...
    ) -> AddAssociationResponseTypeDef:
        """
        Creates an *association* between the source and the destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#add_association)
        """

    def add_tags(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> AddTagsOutputTypeDef:
        """
        Adds or overwrites one or more tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#add_tags)
        """

    def associate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> AssociateTrialComponentResponseTypeDef:
        """
        Associates a trial component with a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#associate_trial_component)
        """

    def batch_describe_model_package(
        self, *, ModelPackageArnList: Sequence[str]
    ) -> BatchDescribeModelPackageOutputTypeDef:
        """
        This action batch describes a list of versioned model packages See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/BatchDescribeModelPackage).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.batch_describe_model_package)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#batch_describe_model_package)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#close)
        """

    def create_action(
        self,
        *,
        ActionName: str,
        Source: ActionSourceTypeDef,
        ActionType: str,
        Description: str = ...,
        Status: ActionStatusType = ...,
        Properties: Mapping[str, str] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateActionResponseTypeDef:
        """
        Creates an *action*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_action)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_action)
        """

    def create_algorithm(
        self,
        *,
        AlgorithmName: str,
        TrainingSpecification: TrainingSpecificationTypeDef,
        AlgorithmDescription: str = ...,
        InferenceSpecification: InferenceSpecificationTypeDef = ...,
        ValidationSpecification: AlgorithmValidationSpecificationTypeDef = ...,
        CertifyForMarketplace: bool = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateAlgorithmOutputTypeDef:
        """
        Create a machine learning algorithm that you can use in SageMaker and list in
        the Amazon Web Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_algorithm)
        """

    def create_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ResourceSpec: ResourceSpecTypeDef = ...,
        SpaceName: str = ...
    ) -> CreateAppResponseTypeDef:
        """
        Creates a running app for the specified UserProfile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_app)
        """

    def create_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        Tags: Sequence[TagTypeDef] = ...,
        KernelGatewayImageConfig: KernelGatewayImageConfigTypeDef = ...
    ) -> CreateAppImageConfigResponseTypeDef:
        """
        Creates a configuration for running a SageMaker image as a KernelGateway app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_app_image_config)
        """

    def create_artifact(
        self,
        *,
        Source: ArtifactSourceTypeDef,
        ArtifactType: str,
        ArtifactName: str = ...,
        Properties: Mapping[str, str] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateArtifactResponseTypeDef:
        """
        Creates an *artifact*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_artifact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_artifact)
        """

    def create_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        InputDataConfig: Sequence[AutoMLChannelTypeDef],
        OutputDataConfig: AutoMLOutputDataConfigTypeDef,
        RoleArn: str,
        ProblemType: ProblemTypeType = ...,
        AutoMLJobObjective: AutoMLJobObjectiveTypeDef = ...,
        AutoMLJobConfig: AutoMLJobConfigTypeDef = ...,
        GenerateCandidateDefinitionsOnly: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ModelDeployConfig: ModelDeployConfigTypeDef = ...
    ) -> CreateAutoMLJobResponseTypeDef:
        """
        Creates an Autopilot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_auto_ml_job)
        """

    def create_code_repository(
        self,
        *,
        CodeRepositoryName: str,
        GitConfig: GitConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateCodeRepositoryOutputTypeDef:
        """
        Creates a Git repository as a resource in your SageMaker account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_code_repository)
        """

    def create_compilation_job(
        self,
        *,
        CompilationJobName: str,
        RoleArn: str,
        OutputConfig: OutputConfigTypeDef,
        StoppingCondition: StoppingConditionTypeDef,
        ModelPackageVersionArn: str = ...,
        InputConfig: InputConfigTypeDef = ...,
        VpcConfig: NeoVpcConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateCompilationJobResponseTypeDef:
        """
        Starts a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_compilation_job)
        """

    def create_context(
        self,
        *,
        ContextName: str,
        Source: ContextSourceTypeDef,
        ContextType: str,
        Description: str = ...,
        Properties: Mapping[str, str] = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateContextResponseTypeDef:
        """
        Creates a *context*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_context)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_context)
        """

    def create_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        DataQualityAppSpecification: DataQualityAppSpecificationTypeDef,
        DataQualityJobInput: DataQualityJobInputTypeDef,
        DataQualityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        DataQualityBaselineConfig: DataQualityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateDataQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors data quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_data_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_data_quality_job_definition)
        """

    def create_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        RoleArn: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        EnableIotRoleAlias: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a device fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_device_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_device_fleet)
        """

    def create_domain(
        self,
        *,
        DomainName: str,
        AuthMode: AuthModeType,
        DefaultUserSettings: UserSettingsTypeDef,
        SubnetIds: Sequence[str],
        VpcId: str,
        Tags: Sequence[TagTypeDef] = ...,
        AppNetworkAccessType: AppNetworkAccessTypeType = ...,
        HomeEfsFileSystemKmsKeyId: str = ...,
        KmsKeyId: str = ...,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = ...,
        DomainSettings: DomainSettingsTypeDef = ...,
        DefaultSpaceSettings: DefaultSpaceSettingsTypeDef = ...
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a `Domain` used by Amazon SageMaker Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_domain)
        """

    def create_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
        ModelConfigs: Sequence[EdgeDeploymentModelConfigTypeDef],
        DeviceFleetName: str,
        Stages: Sequence[DeploymentStageTypeDef] = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateEdgeDeploymentPlanResponseTypeDef:
        """
        Creates an edge deployment plan, consisting of multiple stages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_plan)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_edge_deployment_plan)
        """

    def create_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, Stages: Sequence[DeploymentStageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a new stage in an existing edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_stage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_edge_deployment_stage)
        """

    def create_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
        CompilationJobName: str,
        ModelName: str,
        ModelVersion: str,
        RoleArn: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        ResourceKey: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a SageMaker Edge Manager model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_packaging_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_edge_packaging_job)
        """

    def create_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        DeploymentConfig: DeploymentConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateEndpointOutputTypeDef:
        """
        Creates an endpoint using the endpoint configuration specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_endpoint)
        """

    def create_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
        ProductionVariants: Sequence[ProductionVariantTypeDef],
        DataCaptureConfig: DataCaptureConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        KmsKeyId: str = ...,
        AsyncInferenceConfig: AsyncInferenceConfigTypeDef = ...,
        ExplainerConfig: ExplainerConfigTypeDef = ...,
        ShadowProductionVariants: Sequence[ProductionVariantTypeDef] = ...
    ) -> CreateEndpointConfigOutputTypeDef:
        """
        Creates an endpoint configuration that SageMaker hosting services uses to deploy
        models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_endpoint_config)
        """

    def create_experiment(
        self,
        *,
        ExperimentName: str,
        DisplayName: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateExperimentResponseTypeDef:
        """
        Creates a SageMaker *experiment*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_experiment)
        """

    def create_feature_group(
        self,
        *,
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        EventTimeFeatureName: str,
        FeatureDefinitions: Sequence[FeatureDefinitionTypeDef],
        OnlineStoreConfig: OnlineStoreConfigTypeDef = ...,
        OfflineStoreConfig: OfflineStoreConfigTypeDef = ...,
        RoleArn: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateFeatureGroupResponseTypeDef:
        """
        Create a new `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_feature_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_feature_group)
        """

    def create_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
        HumanLoopConfig: HumanLoopConfigTypeDef,
        OutputConfig: FlowDefinitionOutputConfigTypeDef,
        RoleArn: str,
        HumanLoopRequestSource: HumanLoopRequestSourceTypeDef = ...,
        HumanLoopActivationConfig: HumanLoopActivationConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateFlowDefinitionResponseTypeDef:
        """
        Creates a flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_flow_definition)
        """

    def create_hub(
        self,
        *,
        HubName: str,
        HubDescription: str,
        HubDisplayName: str = ...,
        HubSearchKeywords: Sequence[str] = ...,
        S3StorageConfig: HubS3StorageConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateHubResponseTypeDef:
        """
        Create a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_hub)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_hub)
        """

    def create_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
        UiTemplate: UiTemplateTypeDef,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateHumanTaskUiResponseTypeDef:
        """
        Defines the settings you will use for the human review workflow user interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_human_task_ui)
        """

    def create_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: HyperParameterTuningJobConfigTypeDef,
        TrainingJobDefinition: HyperParameterTrainingJobDefinitionTypeDef = ...,
        TrainingJobDefinitions: Sequence[HyperParameterTrainingJobDefinitionTypeDef] = ...,
        WarmStartConfig: HyperParameterTuningJobWarmStartConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateHyperParameterTuningJobResponseTypeDef:
        """
        Starts a hyperparameter tuning job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_hyper_parameter_tuning_job)
        """

    def create_image(
        self,
        *,
        ImageName: str,
        RoleArn: str,
        Description: str = ...,
        DisplayName: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateImageResponseTypeDef:
        """
        Creates a custom SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_image)
        """

    def create_image_version(
        self,
        *,
        BaseImage: str,
        ClientToken: str,
        ImageName: str,
        Aliases: Sequence[str] = ...,
        VendorGuidance: VendorGuidanceType = ...,
        JobType: JobTypeType = ...,
        MLFramework: str = ...,
        ProgrammingLang: str = ...,
        Processor: ProcessorType = ...,
        Horovod: bool = ...,
        ReleaseNotes: str = ...
    ) -> CreateImageVersionResponseTypeDef:
        """
        Creates a version of the SageMaker image specified by `ImageName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_image_version)
        """

    def create_inference_experiment(
        self,
        *,
        Name: str,
        Type: Literal["ShadowMode"],
        RoleArn: str,
        EndpointName: str,
        ModelVariants: Sequence[ModelVariantConfigTypeDef],
        ShadowModeConfig: ShadowModeConfigTypeDef,
        Schedule: InferenceExperimentScheduleTypeDef = ...,
        Description: str = ...,
        DataStorageConfig: InferenceExperimentDataStorageConfigTypeDef = ...,
        KmsKey: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateInferenceExperimentResponseTypeDef:
        """
        Creates an inference experiment using the configurations specified in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_inference_experiment)
        """

    def create_inference_recommendations_job(
        self,
        *,
        JobName: str,
        JobType: RecommendationJobTypeType,
        RoleArn: str,
        InputConfig: RecommendationJobInputConfigTypeDef,
        JobDescription: str = ...,
        StoppingConditions: RecommendationJobStoppingConditionsTypeDef = ...,
        OutputConfig: RecommendationJobOutputConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateInferenceRecommendationsJobResponseTypeDef:
        """
        Starts a recommendation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_inference_recommendations_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_inference_recommendations_job)
        """

    def create_labeling_job(
        self,
        *,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: LabelingJobInputConfigTypeDef,
        OutputConfig: LabelingJobOutputConfigTypeDef,
        RoleArn: str,
        HumanTaskConfig: HumanTaskConfigTypeDef,
        LabelCategoryConfigS3Uri: str = ...,
        StoppingConditions: LabelingJobStoppingConditionsTypeDef = ...,
        LabelingJobAlgorithmsConfig: LabelingJobAlgorithmsConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateLabelingJobResponseTypeDef:
        """
        Creates a job that uses workers to label the data objects in your input dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_labeling_job)
        """

    def create_model(
        self,
        *,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: ContainerDefinitionTypeDef = ...,
        Containers: Sequence[ContainerDefinitionTypeDef] = ...,
        InferenceExecutionConfig: InferenceExecutionConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        VpcConfig: VpcConfigTypeDef = ...,
        EnableNetworkIsolation: bool = ...
    ) -> CreateModelOutputTypeDef:
        """
        Creates a model in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model)
        """

    def create_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelBiasAppSpecification: ModelBiasAppSpecificationTypeDef,
        ModelBiasJobInput: ModelBiasJobInputTypeDef,
        ModelBiasJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelBiasBaselineConfig: ModelBiasBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateModelBiasJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model bias job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_bias_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_bias_job_definition)
        """

    def create_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str,
        ModelCardStatus: ModelCardStatusType,
        SecurityConfig: ModelCardSecurityConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateModelCardResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_card)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_card)
        """

    def create_model_card_export_job(
        self,
        *,
        ModelCardName: str,
        ModelCardExportJobName: str,
        OutputConfig: ModelCardExportOutputConfigTypeDef,
        ModelCardVersion: int = ...
    ) -> CreateModelCardExportJobResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_card_export_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_card_export_job)
        """

    def create_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationTypeDef,
        ModelExplainabilityJobInput: ModelExplainabilityJobInputTypeDef,
        ModelExplainabilityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelExplainabilityBaselineConfig: ModelExplainabilityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model explainability job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_explainability_job_definition)
        """

    def create_model_package(
        self,
        *,
        ModelPackageName: str = ...,
        ModelPackageGroupName: str = ...,
        ModelPackageDescription: str = ...,
        InferenceSpecification: InferenceSpecificationTypeDef = ...,
        ValidationSpecification: ModelPackageValidationSpecificationTypeDef = ...,
        SourceAlgorithmSpecification: SourceAlgorithmSpecificationTypeDef = ...,
        CertifyForMarketplace: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        ModelMetrics: ModelMetricsTypeDef = ...,
        ClientToken: str = ...,
        CustomerMetadataProperties: Mapping[str, str] = ...,
        DriftCheckBaselines: DriftCheckBaselinesTypeDef = ...,
        Domain: str = ...,
        Task: str = ...,
        SamplePayloadUrl: str = ...,
        AdditionalInferenceSpecifications: Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ] = ...
    ) -> CreateModelPackageOutputTypeDef:
        """
        Creates a model package that you can use to create SageMaker models or list on
        Amazon Web Services Marketplace, or a versioned model that is part of a model
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_package)
        """

    def create_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
        ModelPackageGroupDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateModelPackageGroupOutputTypeDef:
        """
        Creates a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_package_group)
        """

    def create_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelQualityAppSpecification: ModelQualityAppSpecificationTypeDef,
        ModelQualityJobInput: ModelQualityJobInputTypeDef,
        ModelQualityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelQualityBaselineConfig: ModelQualityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateModelQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors model quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_model_quality_job_definition)
        """

    def create_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateMonitoringScheduleResponseTypeDef:
        """
        Creates a schedule that regularly starts Amazon SageMaker Processing Jobs to
        monitor the data captured for an Amazon SageMaker Endoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_monitoring_schedule)
        """

    def create_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType,
        RoleArn: str,
        SubnetId: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        KmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        LifecycleConfigName: str = ...,
        DirectInternetAccess: DirectInternetAccessType = ...,
        VolumeSizeInGB: int = ...,
        AcceleratorTypes: Sequence[NotebookInstanceAcceleratorTypeType] = ...,
        DefaultCodeRepository: str = ...,
        AdditionalCodeRepositories: Sequence[str] = ...,
        RootAccess: RootAccessType = ...,
        PlatformIdentifier: str = ...,
        InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfigurationTypeDef = ...
    ) -> CreateNotebookInstanceOutputTypeDef:
        """
        Creates an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_notebook_instance)
        """

    def create_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
        OnStart: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...
    ) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Creates a lifecycle configuration that you can associate with a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_notebook_instance_lifecycle_config)
        """

    def create_pipeline(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        RoleArn: str,
        PipelineDisplayName: str = ...,
        PipelineDefinition: str = ...,
        PipelineDefinitionS3Location: PipelineDefinitionS3LocationTypeDef = ...,
        PipelineDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates a pipeline using a JSON pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_pipeline)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_pipeline)
        """

    def create_presigned_domain_url(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SessionExpirationDurationInSeconds: int = ...,
        ExpiresInSeconds: int = ...,
        SpaceName: str = ...
    ) -> CreatePresignedDomainUrlResponseTypeDef:
        """
        Creates a URL for a specified UserProfile in a Domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_presigned_domain_url)
        """

    def create_presigned_notebook_instance_url(
        self, *, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = ...
    ) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
        """
        Returns a URL that you can use to connect to the Jupyter server from a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_presigned_notebook_instance_url)
        """

    def create_processing_job(
        self,
        *,
        ProcessingJobName: str,
        ProcessingResources: ProcessingResourcesTypeDef,
        AppSpecification: AppSpecificationTypeDef,
        RoleArn: str,
        ProcessingInputs: Sequence[ProcessingInputTypeDef] = ...,
        ProcessingOutputConfig: ProcessingOutputConfigTypeDef = ...,
        StoppingCondition: ProcessingStoppingConditionTypeDef = ...,
        Environment: Mapping[str, str] = ...,
        NetworkConfig: NetworkConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...
    ) -> CreateProcessingJobResponseTypeDef:
        """
        Creates a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_processing_job)
        """

    def create_project(
        self,
        *,
        ProjectName: str,
        ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsTypeDef,
        ProjectDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateProjectOutputTypeDef:
        """
        Creates a machine learning (ML) project that can contain one or more templates
        that set up an ML pipeline from training to deploying an approved model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_project)
        """

    def create_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        Tags: Sequence[TagTypeDef] = ...,
        SpaceSettings: SpaceSettingsTypeDef = ...
    ) -> CreateSpaceResponseTypeDef:
        """
        Creates a space used for real time collaboration in a Domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_space)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_space)
        """

    def create_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
        StudioLifecycleConfigContent: str,
        StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateStudioLifecycleConfigResponseTypeDef:
        """
        Creates a new Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_studio_lifecycle_config)
        """

    def create_training_job(
        self,
        *,
        TrainingJobName: str,
        AlgorithmSpecification: AlgorithmSpecificationTypeDef,
        RoleArn: str,
        OutputDataConfig: OutputDataConfigTypeDef,
        ResourceConfig: ResourceConfigTypeDef,
        StoppingCondition: StoppingConditionTypeDef,
        HyperParameters: Mapping[str, str] = ...,
        InputDataConfig: Sequence[ChannelTypeDef] = ...,
        VpcConfig: VpcConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        EnableNetworkIsolation: bool = ...,
        EnableInterContainerTrafficEncryption: bool = ...,
        EnableManagedSpotTraining: bool = ...,
        CheckpointConfig: CheckpointConfigTypeDef = ...,
        DebugHookConfig: DebugHookConfigTypeDef = ...,
        DebugRuleConfigurations: Sequence[DebugRuleConfigurationTypeDef] = ...,
        TensorBoardOutputConfig: TensorBoardOutputConfigTypeDef = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...,
        ProfilerConfig: ProfilerConfigTypeDef = ...,
        ProfilerRuleConfigurations: Sequence[ProfilerRuleConfigurationTypeDef] = ...,
        Environment: Mapping[str, str] = ...,
        RetryStrategy: RetryStrategyTypeDef = ...
    ) -> CreateTrainingJobResponseTypeDef:
        """
        Starts a model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_training_job)
        """

    def create_transform_job(
        self,
        *,
        TransformJobName: str,
        ModelName: str,
        TransformInput: TransformInputTypeDef,
        TransformOutput: TransformOutputTypeDef,
        TransformResources: TransformResourcesTypeDef,
        MaxConcurrentTransforms: int = ...,
        ModelClientConfig: ModelClientConfigTypeDef = ...,
        MaxPayloadInMB: int = ...,
        BatchStrategy: BatchStrategyType = ...,
        Environment: Mapping[str, str] = ...,
        DataCaptureConfig: BatchDataCaptureConfigTypeDef = ...,
        DataProcessing: DataProcessingTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...
    ) -> CreateTransformJobResponseTypeDef:
        """
        Starts a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_transform_job)
        """

    def create_trial(
        self,
        *,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateTrialResponseTypeDef:
        """
        Creates an SageMaker *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_trial)
        """

    def create_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = ...,
        Status: TrialComponentStatusTypeDef = ...,
        StartTime: Union[datetime, str] = ...,
        EndTime: Union[datetime, str] = ...,
        Parameters: Mapping[str, TrialComponentParameterValueTypeDef] = ...,
        InputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        OutputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateTrialComponentResponseTypeDef:
        """
        Creates a *trial component* , which is a stage of a machine learning *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_trial_component)
        """

    def create_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = ...,
        SingleSignOnUserValue: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        UserSettings: UserSettingsTypeDef = ...
    ) -> CreateUserProfileResponseTypeDef:
        """
        Creates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_user_profile)
        """

    def create_workforce(
        self,
        *,
        WorkforceName: str,
        CognitoConfig: CognitoConfigTypeDef = ...,
        OidcConfig: OidcConfigTypeDef = ...,
        SourceIpConfig: SourceIpConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        WorkforceVpcConfig: WorkforceVpcConfigRequestTypeDef = ...
    ) -> CreateWorkforceResponseTypeDef:
        """
        Use this operation to create a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workforce)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_workforce)
        """

    def create_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: Sequence[MemberDefinitionTypeDef],
        Description: str,
        WorkforceName: str = ...,
        NotificationConfiguration: NotificationConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateWorkteamResponseTypeDef:
        """
        Creates a new work team for labeling your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#create_workteam)
        """

    def delete_action(self, *, ActionName: str) -> DeleteActionResponseTypeDef:
        """
        Deletes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_action)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_action)
        """

    def delete_algorithm(self, *, AlgorithmName: str) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified algorithm from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_algorithm)
        """

    def delete_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        SpaceName: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to stop and delete an app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_app)
        """

    def delete_app_image_config(self, *, AppImageConfigName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_app_image_config)
        """

    def delete_artifact(
        self, *, ArtifactArn: str = ..., Source: ArtifactSourceTypeDef = ...
    ) -> DeleteArtifactResponseTypeDef:
        """
        Deletes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_artifact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_artifact)
        """

    def delete_association(
        self, *, SourceArn: str, DestinationArn: str
    ) -> DeleteAssociationResponseTypeDef:
        """
        Deletes an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_association)
        """

    def delete_code_repository(self, *, CodeRepositoryName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Git repository from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_code_repository)
        """

    def delete_context(self, *, ContextName: str) -> DeleteContextResponseTypeDef:
        """
        Deletes an context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_context)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_context)
        """

    def delete_data_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_data_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_data_quality_job_definition)
        """

    def delete_device_fleet(self, *, DeviceFleetName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_device_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_device_fleet)
        """

    def delete_domain(
        self, *, DomainId: str, RetentionPolicy: RetentionPolicyTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to delete a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_domain)
        """

    def delete_edge_deployment_plan(
        self, *, EdgeDeploymentPlanName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an edge deployment plan if (and only if) all the stages in the plan are
        inactive or there are no stages in the plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_plan)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_edge_deployment_plan)
        """

    def delete_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a stage in an edge deployment plan if (and only if) the stage is
        inactive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_stage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_edge_deployment_stage)
        """

    def delete_endpoint(self, *, EndpointName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_endpoint)
        """

    def delete_endpoint_config(self, *, EndpointConfigName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an endpoint configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_endpoint_config)
        """

    def delete_experiment(self, *, ExperimentName: str) -> DeleteExperimentResponseTypeDef:
        """
        Deletes an SageMaker experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_experiment)
        """

    def delete_feature_group(self, *, FeatureGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete the `FeatureGroup` and any data that was written to the `OnlineStore` of
        the `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_feature_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_feature_group)
        """

    def delete_flow_definition(self, *, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        Deletes the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_flow_definition)
        """

    def delete_hub(self, *, HubName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_hub)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_hub)
        """

    def delete_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_hub_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_hub_content)
        """

    def delete_human_task_ui(self, *, HumanTaskUiName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a human task user interface (worker task template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_human_task_ui)
        """

    def delete_image(self, *, ImageName: str) -> Dict[str, Any]:
        """
        Deletes a SageMaker image and all versions of the image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_image)
        """

    def delete_image_version(
        self, *, ImageName: str, Version: int = ..., Alias: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_image_version)
        """

    def delete_inference_experiment(self, *, Name: str) -> DeleteInferenceExperimentResponseTypeDef:
        """
        Deletes an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_inference_experiment)
        """

    def delete_model(self, *, ModelName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model)
        """

    def delete_model_bias_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_bias_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_bias_job_definition)
        """

    def delete_model_card(self, *, ModelCardName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_card)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_card)
        """

    def delete_model_explainability_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_explainability_job_definition)
        """

    def delete_model_package(self, *, ModelPackageName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_package)
        """

    def delete_model_package_group(
        self, *, ModelPackageGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_package_group)
        """

    def delete_model_package_group_policy(
        self, *, ModelPackageGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model group resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_package_group_policy)
        """

    def delete_model_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the secified model quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_model_quality_job_definition)
        """

    def delete_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_monitoring_schedule)
        """

    def delete_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_notebook_instance)
        """

    def delete_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_notebook_instance_lifecycle_config)
        """

    def delete_pipeline(
        self, *, PipelineName: str, ClientRequestToken: str
    ) -> DeletePipelineResponseTypeDef:
        """
        Deletes a pipeline if there are no running instances of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_pipeline)
        """

    def delete_project(self, *, ProjectName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_project)
        """

    def delete_space(self, *, DomainId: str, SpaceName: str) -> EmptyResponseMetadataTypeDef:
        """
        Used to delete a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_space)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_space)
        """

    def delete_studio_lifecycle_config(
        self, *, StudioLifecycleConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_studio_lifecycle_config)
        """

    def delete_tags(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from an SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_tags)
        """

    def delete_trial(self, *, TrialName: str) -> DeleteTrialResponseTypeDef:
        """
        Deletes the specified trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_trial)
        """

    def delete_trial_component(
        self, *, TrialComponentName: str
    ) -> DeleteTrialComponentResponseTypeDef:
        """
        Deletes the specified trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_trial_component)
        """

    def delete_user_profile(
        self, *, DomainId: str, UserProfileName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_user_profile)
        """

    def delete_workforce(self, *, WorkforceName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_workforce)
        """

    def delete_workteam(self, *, WorkteamName: str) -> DeleteWorkteamResponseTypeDef:
        """
        Deletes an existing work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#delete_workteam)
        """

    def deregister_devices(
        self, *, DeviceFleetName: str, DeviceNames: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters the specified devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.deregister_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#deregister_devices)
        """

    def describe_action(self, *, ActionName: str) -> DescribeActionResponseTypeDef:
        """
        Describes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_action)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_action)
        """

    def describe_algorithm(self, *, AlgorithmName: str) -> DescribeAlgorithmOutputTypeDef:
        """
        Returns a description of the specified algorithm that is in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_algorithm)
        """

    def describe_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        SpaceName: str = ...
    ) -> DescribeAppResponseTypeDef:
        """
        Describes the app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_app)
        """

    def describe_app_image_config(
        self, *, AppImageConfigName: str
    ) -> DescribeAppImageConfigResponseTypeDef:
        """
        Describes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_app_image_config)
        """

    def describe_artifact(self, *, ArtifactArn: str) -> DescribeArtifactResponseTypeDef:
        """
        Describes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_artifact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_artifact)
        """

    def describe_auto_ml_job(self, *, AutoMLJobName: str) -> DescribeAutoMLJobResponseTypeDef:
        """
        Returns information about an Amazon SageMaker AutoML job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_auto_ml_job)
        """

    def describe_code_repository(
        self, *, CodeRepositoryName: str
    ) -> DescribeCodeRepositoryOutputTypeDef:
        """
        Gets details about the specified Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_code_repository)
        """

    def describe_compilation_job(
        self, *, CompilationJobName: str
    ) -> DescribeCompilationJobResponseTypeDef:
        """
        Returns information about a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_compilation_job)
        """

    def describe_context(self, *, ContextName: str) -> DescribeContextResponseTypeDef:
        """
        Describes a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_context)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_context)
        """

    def describe_data_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeDataQualityJobDefinitionResponseTypeDef:
        """
        Gets the details of a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_data_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_data_quality_job_definition)
        """

    def describe_device(
        self, *, DeviceName: str, DeviceFleetName: str, NextToken: str = ...
    ) -> DescribeDeviceResponseTypeDef:
        """
        Describes the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_device)
        """

    def describe_device_fleet(self, *, DeviceFleetName: str) -> DescribeDeviceFleetResponseTypeDef:
        """
        A description of the fleet the device belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_device_fleet)
        """

    def describe_domain(self, *, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        The description of the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_domain)
        """

    def describe_edge_deployment_plan(
        self, *, EdgeDeploymentPlanName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeEdgeDeploymentPlanResponseTypeDef:
        """
        Describes an edge deployment plan with deployment status per stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_edge_deployment_plan)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_edge_deployment_plan)
        """

    def describe_edge_packaging_job(
        self, *, EdgePackagingJobName: str
    ) -> DescribeEdgePackagingJobResponseTypeDef:
        """
        A description of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_edge_packaging_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_edge_packaging_job)
        """

    def describe_endpoint(self, *, EndpointName: str) -> DescribeEndpointOutputTypeDef:
        """
        Returns the description of an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_endpoint)
        """

    def describe_endpoint_config(
        self, *, EndpointConfigName: str
    ) -> DescribeEndpointConfigOutputTypeDef:
        """
        Returns the description of an endpoint configuration created using the
        `CreateEndpointConfig` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_endpoint_config)
        """

    def describe_experiment(self, *, ExperimentName: str) -> DescribeExperimentResponseTypeDef:
        """
        Provides a list of an experiment's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_experiment)
        """

    def describe_feature_group(
        self, *, FeatureGroupName: str, NextToken: str = ...
    ) -> DescribeFeatureGroupResponseTypeDef:
        """
        Use this operation to describe a `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_feature_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_feature_group)
        """

    def describe_feature_metadata(
        self, *, FeatureGroupName: str, FeatureName: str
    ) -> DescribeFeatureMetadataResponseTypeDef:
        """
        Shows the metadata for a feature within a feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_feature_metadata)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_feature_metadata)
        """

    def describe_flow_definition(
        self, *, FlowDefinitionName: str
    ) -> DescribeFlowDefinitionResponseTypeDef:
        """
        Returns information about the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_flow_definition)
        """

    def describe_hub(self, *, HubName: str) -> DescribeHubResponseTypeDef:
        """
        Describe a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hub)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_hub)
        """

    def describe_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str = ...
    ) -> DescribeHubContentResponseTypeDef:
        """
        Describe the content of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hub_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_hub_content)
        """

    def describe_human_task_ui(self, *, HumanTaskUiName: str) -> DescribeHumanTaskUiResponseTypeDef:
        """
        Returns information about the requested human task user interface (worker task
        template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_human_task_ui)
        """

    def describe_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> DescribeHyperParameterTuningJobResponseTypeDef:
        """
        Gets a description of a hyperparameter tuning job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_hyper_parameter_tuning_job)
        """

    def describe_image(self, *, ImageName: str) -> DescribeImageResponseTypeDef:
        """
        Describes a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_image)
        """

    def describe_image_version(
        self, *, ImageName: str, Version: int = ..., Alias: str = ...
    ) -> DescribeImageVersionResponseTypeDef:
        """
        Describes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_image_version)
        """

    def describe_inference_experiment(
        self, *, Name: str
    ) -> DescribeInferenceExperimentResponseTypeDef:
        """
        Returns details about an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_inference_experiment)
        """

    def describe_inference_recommendations_job(
        self, *, JobName: str
    ) -> DescribeInferenceRecommendationsJobResponseTypeDef:
        """
        Provides the results of the Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_inference_recommendations_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_inference_recommendations_job)
        """

    def describe_labeling_job(self, *, LabelingJobName: str) -> DescribeLabelingJobResponseTypeDef:
        """
        Gets information about a labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_labeling_job)
        """

    def describe_lineage_group(
        self, *, LineageGroupName: str
    ) -> DescribeLineageGroupResponseTypeDef:
        """
        Provides a list of properties for the requested lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_lineage_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_lineage_group)
        """

    def describe_model(self, *, ModelName: str) -> DescribeModelOutputTypeDef:
        """
        Describes a model that you created using the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model)
        """

    def describe_model_bias_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelBiasJobDefinitionResponseTypeDef:
        """
        Returns a description of a model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_bias_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_bias_job_definition)
        """

    def describe_model_card(
        self, *, ModelCardName: str, ModelCardVersion: int = ...
    ) -> DescribeModelCardResponseTypeDef:
        """
        Describes the content, creation time, and security configuration of an Amazon
        SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_card)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_card)
        """

    def describe_model_card_export_job(
        self, *, ModelCardExportJobArn: str
    ) -> DescribeModelCardExportJobResponseTypeDef:
        """
        Describes an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_card_export_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_card_export_job)
        """

    def describe_model_explainability_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_explainability_job_definition)
        """

    def describe_model_package(self, *, ModelPackageName: str) -> DescribeModelPackageOutputTypeDef:
        """
        Returns a description of the specified model package, which is used to create
        SageMaker models or list them on Amazon Web Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_package)
        """

    def describe_model_package_group(
        self, *, ModelPackageGroupName: str
    ) -> DescribeModelPackageGroupOutputTypeDef:
        """
        Gets a description for the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_package_group)
        """

    def describe_model_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelQualityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model quality job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_quality_job_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_model_quality_job_definition)
        """

    def describe_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> DescribeMonitoringScheduleResponseTypeDef:
        """
        Describes the schedule for a monitoring job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_monitoring_schedule)
        """

    def describe_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> DescribeNotebookInstanceOutputTypeDef:
        """
        Returns information about a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_notebook_instance)
        """

    def describe_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Returns a description of a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_notebook_instance_lifecycle_config)
        """

    def describe_pipeline(self, *, PipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        Describes the details of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_pipeline)
        """

    def describe_pipeline_definition_for_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineDefinitionForExecutionResponseTypeDef:
        """
        Describes the details of an execution's pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_definition_for_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_pipeline_definition_for_execution)
        """

    def describe_pipeline_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineExecutionResponseTypeDef:
        """
        Describes the details of a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_pipeline_execution)
        """

    def describe_processing_job(
        self, *, ProcessingJobName: str
    ) -> DescribeProcessingJobResponseTypeDef:
        """
        Returns a description of a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_processing_job)
        """

    def describe_project(self, *, ProjectName: str) -> DescribeProjectOutputTypeDef:
        """
        Describes the details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_project)
        """

    def describe_space(self, *, DomainId: str, SpaceName: str) -> DescribeSpaceResponseTypeDef:
        """
        Describes the space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_space)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_space)
        """

    def describe_studio_lifecycle_config(
        self, *, StudioLifecycleConfigName: str
    ) -> DescribeStudioLifecycleConfigResponseTypeDef:
        """
        Describes the Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_studio_lifecycle_config)
        """

    def describe_subscribed_workteam(
        self, *, WorkteamArn: str
    ) -> DescribeSubscribedWorkteamResponseTypeDef:
        """
        Gets information about a work team provided by a vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_subscribed_workteam)
        """

    def describe_training_job(self, *, TrainingJobName: str) -> DescribeTrainingJobResponseTypeDef:
        """
        Returns information about a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_training_job)
        """

    def describe_transform_job(
        self, *, TransformJobName: str
    ) -> DescribeTransformJobResponseTypeDef:
        """
        Returns information about a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_transform_job)
        """

    def describe_trial(self, *, TrialName: str) -> DescribeTrialResponseTypeDef:
        """
        Provides a list of a trial's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_trial)
        """

    def describe_trial_component(
        self, *, TrialComponentName: str
    ) -> DescribeTrialComponentResponseTypeDef:
        """
        Provides a list of a trials component's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_trial_component)
        """

    def describe_user_profile(
        self, *, DomainId: str, UserProfileName: str
    ) -> DescribeUserProfileResponseTypeDef:
        """
        Describes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_user_profile)
        """

    def describe_workforce(self, *, WorkforceName: str) -> DescribeWorkforceResponseTypeDef:
        """
        Lists private workforce information, including workforce name, Amazon Resource
        Name (ARN), and, if applicable, allowed IP address ranges (
        [CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)_ ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_workforce)
        """

    def describe_workteam(self, *, WorkteamName: str) -> DescribeWorkteamResponseTypeDef:
        """
        Gets information about a specific work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#describe_workteam)
        """

    def disable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Disables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#disable_sagemaker_servicecatalog_portfolio)
        """

    def disassociate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> DisassociateTrialComponentResponseTypeDef:
        """
        Disassociates a trial component from a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#disassociate_trial_component)
        """

    def enable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Enables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.enable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#enable_sagemaker_servicecatalog_portfolio)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#generate_presigned_url)
        """

    def get_device_fleet_report(
        self, *, DeviceFleetName: str
    ) -> GetDeviceFleetReportResponseTypeDef:
        """
        Describes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_device_fleet_report)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_device_fleet_report)
        """

    def get_lineage_group_policy(
        self, *, LineageGroupName: str
    ) -> GetLineageGroupPolicyResponseTypeDef:
        """
        The resource policy for the lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_lineage_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_lineage_group_policy)
        """

    def get_model_package_group_policy(
        self, *, ModelPackageGroupName: str
    ) -> GetModelPackageGroupPolicyOutputTypeDef:
        """
        Gets a resource policy that manages access for a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_model_package_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_model_package_group_policy)
        """

    def get_sagemaker_servicecatalog_portfolio_status(
        self,
    ) -> GetSagemakerServicecatalogPortfolioStatusOutputTypeDef:
        """
        Gets the status of Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_sagemaker_servicecatalog_portfolio_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_sagemaker_servicecatalog_portfolio_status)
        """

    def get_search_suggestions(
        self, *, Resource: ResourceTypeType, SuggestionQuery: SuggestionQueryTypeDef = ...
    ) -> GetSearchSuggestionsResponseTypeDef:
        """
        An auto-complete API for the search functionality in the Amazon SageMaker
        console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_search_suggestions)
        """

    def import_hub_content(
        self,
        *,
        HubContentName: str,
        HubContentType: HubContentTypeType,
        DocumentSchemaVersion: str,
        HubName: str,
        HubContentDocument: str,
        HubContentVersion: str = ...,
        HubContentDisplayName: str = ...,
        HubContentDescription: str = ...,
        HubContentMarkdown: str = ...,
        HubContentSearchKeywords: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> ImportHubContentResponseTypeDef:
        """
        Import hub content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.import_hub_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#import_hub_content)
        """

    def list_actions(
        self,
        *,
        SourceUri: str = ...,
        ActionType: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortActionsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListActionsResponseTypeDef:
        """
        Lists the actions in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_actions)
        """

    def list_algorithms(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: AlgorithmSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListAlgorithmsOutputTypeDef:
        """
        Lists the machine learning algorithms that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_algorithms)
        """

    def list_aliases(
        self,
        *,
        ImageName: str,
        Alias: str = ...,
        Version: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListAliasesResponseTypeDef:
        """
        Lists the aliases of a specified image or image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_aliases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_aliases)
        """

    def list_app_image_configs(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        ModifiedTimeBefore: Union[datetime, str] = ...,
        ModifiedTimeAfter: Union[datetime, str] = ...,
        SortBy: AppImageConfigSortKeyType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListAppImageConfigsResponseTypeDef:
        """
        Lists the AppImageConfigs in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_app_image_configs)
        """

    def list_apps(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: Literal["CreationTime"] = ...,
        DomainIdEquals: str = ...,
        UserProfileNameEquals: str = ...,
        SpaceNameEquals: str = ...
    ) -> ListAppsResponseTypeDef:
        """
        Lists apps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_apps)
        """

    def list_artifacts(
        self,
        *,
        SourceUri: str = ...,
        ArtifactType: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: Literal["CreationTime"] = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListArtifactsResponseTypeDef:
        """
        Lists the artifacts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_artifacts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_artifacts)
        """

    def list_associations(
        self,
        *,
        SourceArn: str = ...,
        DestinationArn: str = ...,
        SourceType: str = ...,
        DestinationType: str = ...,
        AssociationType: AssociationEdgeTypeType = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortAssociationsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListAssociationsResponseTypeDef:
        """
        Lists the associations in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_associations)
        """

    def list_auto_ml_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: AutoMLJobStatusType = ...,
        SortOrder: AutoMLSortOrderType = ...,
        SortBy: AutoMLSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListAutoMLJobsResponseTypeDef:
        """
        Request a list of jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_auto_ml_jobs)
        """

    def list_candidates_for_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        StatusEquals: CandidateStatusType = ...,
        CandidateNameEquals: str = ...,
        SortOrder: AutoMLSortOrderType = ...,
        SortBy: CandidateSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListCandidatesForAutoMLJobResponseTypeDef:
        """
        List the candidates created for the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_candidates_for_auto_ml_job)
        """

    def list_code_repositories(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: CodeRepositorySortByType = ...,
        SortOrder: CodeRepositorySortOrderType = ...
    ) -> ListCodeRepositoriesOutputTypeDef:
        """
        Gets a list of the Git repositories in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_code_repositories)
        """

    def list_compilation_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: CompilationJobStatusType = ...,
        SortBy: ListCompilationJobsSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListCompilationJobsResponseTypeDef:
        """
        Lists model compilation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_compilation_jobs)
        """

    def list_contexts(
        self,
        *,
        SourceUri: str = ...,
        ContextType: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortContextsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListContextsResponseTypeDef:
        """
        Lists the contexts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_contexts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_contexts)
        """

    def list_data_quality_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListDataQualityJobDefinitionsResponseTypeDef:
        """
        Lists the data quality job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_data_quality_job_definitions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_data_quality_job_definitions)
        """

    def list_device_fleets(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        SortBy: ListDeviceFleetsSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListDeviceFleetsResponseTypeDef:
        """
        Returns a list of devices in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_device_fleets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_device_fleets)
        """

    def list_devices(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        LatestHeartbeatAfter: Union[datetime, str] = ...,
        ModelName: str = ...,
        DeviceFleetName: str = ...
    ) -> ListDevicesResponseTypeDef:
        """
        A list of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_devices)
        """

    def list_domains(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDomainsResponseTypeDef:
        """
        Lists the domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_domains)
        """

    def list_edge_deployment_plans(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        DeviceFleetNameContains: str = ...,
        SortBy: ListEdgeDeploymentPlansSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListEdgeDeploymentPlansResponseTypeDef:
        """
        Lists all edge deployment plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_edge_deployment_plans)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_edge_deployment_plans)
        """

    def list_edge_packaging_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        ModelNameContains: str = ...,
        StatusEquals: EdgePackagingJobStatusType = ...,
        SortBy: ListEdgePackagingJobsSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListEdgePackagingJobsResponseTypeDef:
        """
        Returns a list of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_edge_packaging_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_edge_packaging_jobs)
        """

    def list_endpoint_configs(
        self,
        *,
        SortBy: EndpointConfigSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListEndpointConfigsOutputTypeDef:
        """
        Lists endpoint configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_endpoint_configs)
        """

    def list_endpoints(
        self,
        *,
        SortBy: EndpointSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        StatusEquals: EndpointStatusType = ...
    ) -> ListEndpointsOutputTypeDef:
        """
        Lists endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_endpoints)
        """

    def list_experiments(
        self,
        *,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortExperimentsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists all the experiments in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_experiments)
        """

    def list_feature_groups(
        self,
        *,
        NameContains: str = ...,
        FeatureGroupStatusEquals: FeatureGroupStatusType = ...,
        OfflineStoreStatusEquals: OfflineStoreStatusValueType = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        SortOrder: FeatureGroupSortOrderType = ...,
        SortBy: FeatureGroupSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListFeatureGroupsResponseTypeDef:
        """
        List `FeatureGroup` s based on given filter and order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_feature_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_feature_groups)
        """

    def list_flow_definitions(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListFlowDefinitionsResponseTypeDef:
        """
        Returns information about the flow definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_flow_definitions)
        """

    def list_hub_content_versions(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        MinVersion: str = ...,
        MaxSchemaVersion: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        SortBy: HubContentSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListHubContentVersionsResponseTypeDef:
        """
        List hub content versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hub_content_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_hub_content_versions)
        """

    def list_hub_contents(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        NameContains: str = ...,
        MaxSchemaVersion: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        SortBy: HubContentSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListHubContentsResponseTypeDef:
        """
        List the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hub_contents)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_hub_contents)
        """

    def list_hubs(
        self,
        *,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        SortBy: HubSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListHubsResponseTypeDef:
        """
        List all existing hubs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hubs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_hubs)
        """

    def list_human_task_uis(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListHumanTaskUisResponseTypeDef:
        """
        Returns information about the human task user interfaces in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_human_task_uis)
        """

    def list_hyper_parameter_tuning_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: HyperParameterTuningJobSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        StatusEquals: HyperParameterTuningJobStatusType = ...
    ) -> ListHyperParameterTuningJobsResponseTypeDef:
        """
        Gets a list of  HyperParameterTuningJobSummary objects that describe the
        hyperparameter tuning jobs launched in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_hyper_parameter_tuning_jobs)
        """

    def list_image_versions(
        self,
        *,
        ImageName: str,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: ImageVersionSortByType = ...,
        SortOrder: ImageVersionSortOrderType = ...
    ) -> ListImageVersionsResponseTypeDef:
        """
        Lists the versions of a specified image and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_image_versions)
        """

    def list_images(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ImageSortByType = ...,
        SortOrder: ImageSortOrderType = ...
    ) -> ListImagesResponseTypeDef:
        """
        Lists the images in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_images)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_images)
        """

    def list_inference_experiments(
        self,
        *,
        NameContains: str = ...,
        Type: Literal["ShadowMode"] = ...,
        StatusEquals: InferenceExperimentStatusType = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        SortBy: SortInferenceExperimentsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListInferenceExperimentsResponseTypeDef:
        """
        Returns the list of all inference experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_experiments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_inference_experiments)
        """

    def list_inference_recommendations_job_steps(
        self,
        *,
        JobName: str,
        Status: RecommendationJobStatusType = ...,
        StepType: Literal["BENCHMARK"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListInferenceRecommendationsJobStepsResponseTypeDef:
        """
        Returns a list of the subtasks for an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_job_steps)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_inference_recommendations_job_steps)
        """

    def list_inference_recommendations_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: RecommendationJobStatusType = ...,
        SortBy: ListInferenceRecommendationsJobsSortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListInferenceRecommendationsJobsResponseTypeDef:
        """
        Lists recommendation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_inference_recommendations_jobs)
        """

    def list_labeling_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        StatusEquals: LabelingJobStatusType = ...
    ) -> ListLabelingJobsResponseTypeDef:
        """
        Gets a list of labeling jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_labeling_jobs)
        """

    def list_labeling_jobs_for_workteam(
        self,
        *,
        WorkteamArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        JobReferenceCodeContains: str = ...,
        SortBy: Literal["CreationTime"] = ...,
        SortOrder: SortOrderType = ...
    ) -> ListLabelingJobsForWorkteamResponseTypeDef:
        """
        Gets a list of labeling jobs assigned to a specified work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_labeling_jobs_for_workteam)
        """

    def list_lineage_groups(
        self,
        *,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortLineageGroupsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListLineageGroupsResponseTypeDef:
        """
        A list of lineage groups shared with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_lineage_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_lineage_groups)
        """

    def list_model_bias_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListModelBiasJobDefinitionsResponseTypeDef:
        """
        Lists model bias jobs definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_bias_job_definitions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_bias_job_definitions)
        """

    def list_model_card_export_jobs(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        ModelCardExportJobNameContains: str = ...,
        StatusEquals: ModelCardExportJobStatusType = ...,
        SortBy: ModelCardExportJobSortByType = ...,
        SortOrder: ModelCardExportJobSortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListModelCardExportJobsResponseTypeDef:
        """
        List the export jobs for the Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_card_export_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_card_export_jobs)
        """

    def list_model_card_versions(
        self,
        *,
        ModelCardName: str,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        ModelCardStatus: ModelCardStatusType = ...,
        NextToken: str = ...,
        SortBy: Literal["Version"] = ...,
        SortOrder: ModelCardSortOrderType = ...
    ) -> ListModelCardVersionsResponseTypeDef:
        """
        List existing versions of an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_card_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_card_versions)
        """

    def list_model_cards(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        ModelCardStatus: ModelCardStatusType = ...,
        NextToken: str = ...,
        SortBy: ModelCardSortByType = ...,
        SortOrder: ModelCardSortOrderType = ...
    ) -> ListModelCardsResponseTypeDef:
        """
        List existing model cards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_cards)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_cards)
        """

    def list_model_explainability_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListModelExplainabilityJobDefinitionsResponseTypeDef:
        """
        Lists model explainability job definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_explainability_job_definitions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_explainability_job_definitions)
        """

    def list_model_metadata(
        self,
        *,
        SearchExpression: ModelMetadataSearchExpressionTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListModelMetadataResponseTypeDef:
        """
        Lists the domain, framework, task, and model name of standard machine learning
        models found in common model zoos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_metadata)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_metadata)
        """

    def list_model_package_groups(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ModelPackageGroupSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListModelPackageGroupsOutputTypeDef:
        """
        Gets a list of the model groups in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_package_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_package_groups)
        """

    def list_model_packages(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        ModelPackageGroupName: str = ...,
        ModelPackageType: ModelPackageTypeType = ...,
        NextToken: str = ...,
        SortBy: ModelPackageSortByType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListModelPackagesOutputTypeDef:
        """
        Lists the model packages that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_packages)
        """

    def list_model_quality_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListModelQualityJobDefinitionsResponseTypeDef:
        """
        Gets a list of model quality monitoring job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_quality_job_definitions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_model_quality_job_definitions)
        """

    def list_models(
        self,
        *,
        SortBy: ModelSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...
    ) -> ListModelsOutputTypeDef:
        """
        Lists models created with the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_models)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_models)
        """

    def list_monitoring_alert_history(
        self,
        *,
        MonitoringScheduleName: str = ...,
        MonitoringAlertName: str = ...,
        SortBy: MonitoringAlertHistorySortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        StatusEquals: MonitoringAlertStatusType = ...
    ) -> ListMonitoringAlertHistoryResponseTypeDef:
        """
        Gets a list of past alerts in a model monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alert_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_monitoring_alert_history)
        """

    def list_monitoring_alerts(
        self, *, MonitoringScheduleName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMonitoringAlertsResponseTypeDef:
        """
        Gets the alerts for a single monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alerts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_monitoring_alerts)
        """

    def list_monitoring_executions(
        self,
        *,
        MonitoringScheduleName: str = ...,
        EndpointName: str = ...,
        SortBy: MonitoringExecutionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        ScheduledTimeBefore: Union[datetime, str] = ...,
        ScheduledTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        StatusEquals: ExecutionStatusType = ...,
        MonitoringJobDefinitionName: str = ...,
        MonitoringTypeEquals: MonitoringTypeType = ...
    ) -> ListMonitoringExecutionsResponseTypeDef:
        """
        Returns list of all monitoring job executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_monitoring_executions)
        """

    def list_monitoring_schedules(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringScheduleSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        StatusEquals: ScheduleStatusType = ...,
        MonitoringJobDefinitionName: str = ...,
        MonitoringTypeEquals: MonitoringTypeType = ...
    ) -> ListMonitoringSchedulesResponseTypeDef:
        """
        Returns list of all monitoring schedules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_monitoring_schedules)
        """

    def list_notebook_instance_lifecycle_configs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: NotebookInstanceLifecycleConfigSortKeyType = ...,
        SortOrder: NotebookInstanceLifecycleConfigSortOrderType = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...
    ) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
        """
        Lists notebook instance lifestyle configurations created with the
        CreateNotebookInstanceLifecycleConfig API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_notebook_instance_lifecycle_configs)
        """

    def list_notebook_instances(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: NotebookInstanceSortKeyType = ...,
        SortOrder: NotebookInstanceSortOrderType = ...,
        NameContains: str = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        StatusEquals: NotebookInstanceStatusType = ...,
        NotebookInstanceLifecycleConfigNameContains: str = ...,
        DefaultCodeRepositoryContains: str = ...,
        AdditionalCodeRepositoryEquals: str = ...
    ) -> ListNotebookInstancesOutputTypeDef:
        """
        Returns a list of the SageMaker notebook instances in the requester's account in
        an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_notebook_instances)
        """

    def list_pipeline_execution_steps(
        self,
        *,
        PipelineExecutionArn: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...
    ) -> ListPipelineExecutionStepsResponseTypeDef:
        """
        Gets a list of `PipeLineExecutionStep` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_execution_steps)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_pipeline_execution_steps)
        """

    def list_pipeline_executions(
        self,
        *,
        PipelineName: str,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortPipelineExecutionsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListPipelineExecutionsResponseTypeDef:
        """
        Gets a list of the pipeline executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_executions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_pipeline_executions)
        """

    def list_pipeline_parameters_for_execution(
        self, *, PipelineExecutionArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListPipelineParametersForExecutionResponseTypeDef:
        """
        Gets a list of parameters for a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_parameters_for_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_pipeline_parameters_for_execution)
        """

    def list_pipelines(
        self,
        *,
        PipelineNamePrefix: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortPipelinesByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListPipelinesResponseTypeDef:
        """
        Gets a list of pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipelines)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_pipelines)
        """

    def list_processing_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: ProcessingJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListProcessingJobsResponseTypeDef:
        """
        Lists processing jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_processing_jobs)
        """

    def list_projects(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ProjectSortByType = ...,
        SortOrder: ProjectSortOrderType = ...
    ) -> ListProjectsOutputTypeDef:
        """
        Gets a list of the projects in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_projects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_projects)
        """

    def list_spaces(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: SpaceSortKeyType = ...,
        DomainIdEquals: str = ...,
        SpaceNameContains: str = ...
    ) -> ListSpacesResponseTypeDef:
        """
        Lists spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_spaces)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_spaces)
        """

    def list_stage_devices(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        ExcludeDevicesDeployedInOtherStage: bool = ...
    ) -> ListStageDevicesResponseTypeDef:
        """
        Lists devices allocated to the stage, containing detailed device information and
        deployment status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_stage_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_stage_devices)
        """

    def list_studio_lifecycle_configs(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        AppTypeEquals: StudioLifecycleConfigAppTypeType = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        ModifiedTimeBefore: Union[datetime, str] = ...,
        ModifiedTimeAfter: Union[datetime, str] = ...,
        SortBy: StudioLifecycleConfigSortKeyType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListStudioLifecycleConfigsResponseTypeDef:
        """
        Lists the Studio Lifecycle Configurations in your Amazon Web Services Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_studio_lifecycle_configs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_studio_lifecycle_configs)
        """

    def list_subscribed_workteams(
        self, *, NameContains: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ListSubscribedWorkteamsResponseTypeDef:
        """
        Gets a list of the work teams that you are subscribed to in the Amazon Web
        Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_subscribed_workteams)
        """

    def list_tags(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsOutputTypeDef:
        """
        Returns the tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_tags)
        """

    def list_training_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: TrainingJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        WarmPoolStatusEquals: WarmPoolResourceStatusType = ...
    ) -> ListTrainingJobsResponseTypeDef:
        """
        Lists training jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_training_jobs)
        """

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        StatusEquals: TrainingJobStatusType = ...,
        SortBy: TrainingJobSortByOptionsType = ...,
        SortOrder: SortOrderType = ...
    ) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        Gets a list of  TrainingJobSummary objects that describe the training jobs that
        a hyperparameter tuning job launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_training_jobs_for_hyper_parameter_tuning_job)
        """

    def list_transform_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = ...,
        CreationTimeBefore: Union[datetime, str] = ...,
        LastModifiedTimeAfter: Union[datetime, str] = ...,
        LastModifiedTimeBefore: Union[datetime, str] = ...,
        NameContains: str = ...,
        StatusEquals: TransformJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListTransformJobsResponseTypeDef:
        """
        Lists transform jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_transform_jobs)
        """

    def list_trial_components(
        self,
        *,
        ExperimentName: str = ...,
        TrialName: str = ...,
        SourceArn: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortTrialComponentsByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListTrialComponentsResponseTypeDef:
        """
        Lists the trial components in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_trial_components)
        """

    def list_trials(
        self,
        *,
        ExperimentName: str = ...,
        TrialComponentName: str = ...,
        CreatedAfter: Union[datetime, str] = ...,
        CreatedBefore: Union[datetime, str] = ...,
        SortBy: SortTrialsByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListTrialsResponseTypeDef:
        """
        Lists the trials in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_trials)
        """

    def list_user_profiles(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: UserProfileSortKeyType = ...,
        DomainIdEquals: str = ...,
        UserProfileNameContains: str = ...
    ) -> ListUserProfilesResponseTypeDef:
        """
        Lists user profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_user_profiles)
        """

    def list_workforces(
        self,
        *,
        SortBy: ListWorkforcesSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListWorkforcesResponseTypeDef:
        """
        Use this operation to list all private and vendor workforces in an Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workforces)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_workforces)
        """

    def list_workteams(
        self,
        *,
        SortBy: ListWorkteamsSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListWorkteamsResponseTypeDef:
        """
        Gets a list of private work teams that you have defined in a region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#list_workteams)
        """

    def put_model_package_group_policy(
        self, *, ModelPackageGroupName: str, ResourcePolicy: str
    ) -> PutModelPackageGroupPolicyOutputTypeDef:
        """
        Adds a resouce policy to control access to a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.put_model_package_group_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#put_model_package_group_policy)
        """

    def query_lineage(
        self,
        *,
        StartArns: Sequence[str] = ...,
        Direction: DirectionType = ...,
        IncludeEdges: bool = ...,
        Filters: QueryFiltersTypeDef = ...,
        MaxDepth: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> QueryLineageResponseTypeDef:
        """
        Use this action to inspect your lineage and discover relationships between
        entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.query_lineage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#query_lineage)
        """

    def register_devices(
        self,
        *,
        DeviceFleetName: str,
        Devices: Sequence[DeviceTypeDef],
        Tags: Sequence[TagTypeDef] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Register devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.register_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#register_devices)
        """

    def render_ui_template(
        self,
        *,
        Task: RenderableTaskTypeDef,
        RoleArn: str,
        UiTemplate: UiTemplateTypeDef = ...,
        HumanTaskUiArn: str = ...
    ) -> RenderUiTemplateResponseTypeDef:
        """
        Renders the UI template so that you can preview the worker's experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#render_ui_template)
        """

    def retry_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        ClientRequestToken: str,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...
    ) -> RetryPipelineExecutionResponseTypeDef:
        """
        Retry the execution of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.retry_pipeline_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#retry_pipeline_execution)
        """

    def search(
        self,
        *,
        Resource: ResourceTypeType,
        SearchExpression: "SearchExpressionTypeDef" = ...,
        SortBy: str = ...,
        SortOrder: SearchSortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> SearchResponseTypeDef:
        """
        Finds Amazon SageMaker resources that match a search query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.search)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#search)
        """

    def send_pipeline_execution_step_failure(
        self, *, CallbackToken: str, FailureReason: str = ..., ClientRequestToken: str = ...
    ) -> SendPipelineExecutionStepFailureResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step failed, along with a
        message describing why.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_failure)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#send_pipeline_execution_step_failure)
        """

    def send_pipeline_execution_step_success(
        self,
        *,
        CallbackToken: str,
        OutputParameters: Sequence[OutputParameterTypeDef] = ...,
        ClientRequestToken: str = ...
    ) -> SendPipelineExecutionStepSuccessResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step succeeded and
        provides a list of the step's output parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_success)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#send_pipeline_execution_step_success)
        """

    def start_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_edge_deployment_stage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#start_edge_deployment_stage)
        """

    def start_inference_experiment(self, *, Name: str) -> StartInferenceExperimentResponseTypeDef:
        """
        Starts an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#start_inference_experiment)
        """

    def start_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a previously stopped monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#start_monitoring_schedule)
        """

    def start_notebook_instance(self, *, NotebookInstanceName: str) -> EmptyResponseMetadataTypeDef:
        """
        Launches an ML compute instance with the latest version of the libraries and
        attaches your ML storage volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#start_notebook_instance)
        """

    def start_pipeline_execution(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        PipelineExecutionDisplayName: str = ...,
        PipelineParameters: Sequence[ParameterTypeDef] = ...,
        PipelineExecutionDescription: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...
    ) -> StartPipelineExecutionResponseTypeDef:
        """
        Starts a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_pipeline_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#start_pipeline_execution)
        """

    def stop_auto_ml_job(self, *, AutoMLJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        A method for forcing the termination of a running job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_auto_ml_job)
        """

    def stop_compilation_job(self, *, CompilationJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_compilation_job)
        """

    def stop_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_edge_deployment_stage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_edge_deployment_stage)
        """

    def stop_edge_packaging_job(self, *, EdgePackagingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Request to stop an edge packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_edge_packaging_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_edge_packaging_job)
        """

    def stop_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a running hyperparameter tuning job and all running training jobs that the
        tuning job launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_hyper_parameter_tuning_job)
        """

    def stop_inference_experiment(
        self,
        *,
        Name: str,
        ModelVariantActions: Mapping[str, ModelVariantActionType],
        DesiredModelVariants: Sequence[ModelVariantConfigTypeDef] = ...,
        DesiredState: InferenceExperimentStopDesiredStateType = ...,
        Reason: str = ...
    ) -> StopInferenceExperimentResponseTypeDef:
        """
        Stops an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_inference_experiment)
        """

    def stop_inference_recommendations_job(self, *, JobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_inference_recommendations_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_inference_recommendations_job)
        """

    def stop_labeling_job(self, *, LabelingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a running labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_labeling_job)
        """

    def stop_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a previously started monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_monitoring_schedule)
        """

    def stop_notebook_instance(self, *, NotebookInstanceName: str) -> EmptyResponseMetadataTypeDef:
        """
        Terminates the ML compute instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_notebook_instance)
        """

    def stop_pipeline_execution(
        self, *, PipelineExecutionArn: str, ClientRequestToken: str
    ) -> StopPipelineExecutionResponseTypeDef:
        """
        Stops a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_pipeline_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_pipeline_execution)
        """

    def stop_processing_job(self, *, ProcessingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_processing_job)
        """

    def stop_training_job(self, *, TrainingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_training_job)
        """

    def stop_transform_job(self, *, TransformJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a batch transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#stop_transform_job)
        """

    def update_action(
        self,
        *,
        ActionName: str,
        Description: str = ...,
        Status: ActionStatusType = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...
    ) -> UpdateActionResponseTypeDef:
        """
        Updates an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_action)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_action)
        """

    def update_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        KernelGatewayImageConfig: KernelGatewayImageConfigTypeDef = ...
    ) -> UpdateAppImageConfigResponseTypeDef:
        """
        Updates the properties of an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_app_image_config)
        """

    def update_artifact(
        self,
        *,
        ArtifactArn: str,
        ArtifactName: str = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...
    ) -> UpdateArtifactResponseTypeDef:
        """
        Updates an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_artifact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_artifact)
        """

    def update_code_repository(
        self, *, CodeRepositoryName: str, GitConfig: GitConfigForUpdateTypeDef = ...
    ) -> UpdateCodeRepositoryOutputTypeDef:
        """
        Updates the specified Git repository with the specified values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_code_repository)
        """

    def update_context(
        self,
        *,
        ContextName: str,
        Description: str = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...
    ) -> UpdateContextResponseTypeDef:
        """
        Updates a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_context)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_context)
        """

    def update_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        RoleArn: str = ...,
        Description: str = ...,
        EnableIotRoleAlias: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a fleet of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_device_fleet)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_device_fleet)
        """

    def update_devices(
        self, *, DeviceFleetName: str, Devices: Sequence[DeviceTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates one or more devices in a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_devices)
        """

    def update_domain(
        self,
        *,
        DomainId: str,
        DefaultUserSettings: UserSettingsTypeDef = ...,
        DomainSettingsForUpdate: DomainSettingsForUpdateTypeDef = ...,
        DefaultSpaceSettings: DefaultSpaceSettingsTypeDef = ...,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = ...
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the default settings for new user profiles in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_domain)
        """

    def update_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool = ...,
        ExcludeRetainedVariantProperties: Sequence[VariantPropertyTypeDef] = ...,
        DeploymentConfig: DeploymentConfigTypeDef = ...,
        RetainDeploymentConfig: bool = ...
    ) -> UpdateEndpointOutputTypeDef:
        """
        Deploys the new `EndpointConfig` specified in the request, switches to using
        newly created endpoint, and then deletes resources provisioned for the endpoint
        using the previous `EndpointConfig` (there is no availability loss).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_endpoint)
        """

    def update_endpoint_weights_and_capacities(
        self,
        *,
        EndpointName: str,
        DesiredWeightsAndCapacities: Sequence[DesiredWeightAndCapacityTypeDef]
    ) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
        """
        Updates variant weight of one or more variants associated with an existing
        endpoint, or capacity of one variant associated with an existing endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_endpoint_weights_and_capacities)
        """

    def update_experiment(
        self, *, ExperimentName: str, DisplayName: str = ..., Description: str = ...
    ) -> UpdateExperimentResponseTypeDef:
        """
        Adds, updates, or removes the description of an experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_experiment)
        """

    def update_feature_group(
        self, *, FeatureGroupName: str, FeatureAdditions: Sequence[FeatureDefinitionTypeDef] = ...
    ) -> UpdateFeatureGroupResponseTypeDef:
        """
        Updates the feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_feature_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_feature_group)
        """

    def update_feature_metadata(
        self,
        *,
        FeatureGroupName: str,
        FeatureName: str,
        Description: str = ...,
        ParameterAdditions: Sequence[FeatureParameterTypeDef] = ...,
        ParameterRemovals: Sequence[str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the description and parameters of the feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_feature_metadata)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_feature_metadata)
        """

    def update_hub(
        self,
        *,
        HubName: str,
        HubDescription: str = ...,
        HubDisplayName: str = ...,
        HubSearchKeywords: Sequence[str] = ...
    ) -> UpdateHubResponseTypeDef:
        """
        Update a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_hub)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_hub)
        """

    def update_image(
        self,
        *,
        ImageName: str,
        DeleteProperties: Sequence[str] = ...,
        Description: str = ...,
        DisplayName: str = ...,
        RoleArn: str = ...
    ) -> UpdateImageResponseTypeDef:
        """
        Updates the properties of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_image)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_image)
        """

    def update_image_version(
        self,
        *,
        ImageName: str,
        Alias: str = ...,
        Version: int = ...,
        AliasesToAdd: Sequence[str] = ...,
        AliasesToDelete: Sequence[str] = ...,
        VendorGuidance: VendorGuidanceType = ...,
        JobType: JobTypeType = ...,
        MLFramework: str = ...,
        ProgrammingLang: str = ...,
        Processor: ProcessorType = ...,
        Horovod: bool = ...,
        ReleaseNotes: str = ...
    ) -> UpdateImageVersionResponseTypeDef:
        """
        Updates the properties of a SageMaker image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_image_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_image_version)
        """

    def update_inference_experiment(
        self,
        *,
        Name: str,
        Schedule: InferenceExperimentScheduleTypeDef = ...,
        Description: str = ...,
        ModelVariants: Sequence[ModelVariantConfigTypeDef] = ...,
        DataStorageConfig: InferenceExperimentDataStorageConfigTypeDef = ...,
        ShadowModeConfig: ShadowModeConfigTypeDef = ...
    ) -> UpdateInferenceExperimentResponseTypeDef:
        """
        Updates an inference experiment that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_inference_experiment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_inference_experiment)
        """

    def update_model_card(
        self, *, ModelCardName: str, Content: str = ..., ModelCardStatus: ModelCardStatusType = ...
    ) -> UpdateModelCardResponseTypeDef:
        """
        Update an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_model_card)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_model_card)
        """

    def update_model_package(
        self,
        *,
        ModelPackageArn: str,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        ApprovalDescription: str = ...,
        CustomerMetadataProperties: Mapping[str, str] = ...,
        CustomerMetadataPropertiesToRemove: Sequence[str] = ...,
        AdditionalInferenceSpecificationsToAdd: Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ] = ...
    ) -> UpdateModelPackageOutputTypeDef:
        """
        Updates a versioned model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_model_package)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_model_package)
        """

    def update_monitoring_alert(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringAlertName: str,
        DatapointsToAlert: int,
        EvaluationPeriod: int
    ) -> UpdateMonitoringAlertResponseTypeDef:
        """
        Update the parameters of a model monitor alert.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_alert)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_monitoring_alert)
        """

    def update_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef
    ) -> UpdateMonitoringScheduleResponseTypeDef:
        """
        Updates a previously created schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_monitoring_schedule)
        """

    def update_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType = ...,
        RoleArn: str = ...,
        LifecycleConfigName: str = ...,
        DisassociateLifecycleConfig: bool = ...,
        VolumeSizeInGB: int = ...,
        DefaultCodeRepository: str = ...,
        AdditionalCodeRepositories: Sequence[str] = ...,
        AcceleratorTypes: Sequence[NotebookInstanceAcceleratorTypeType] = ...,
        DisassociateAcceleratorTypes: bool = ...,
        DisassociateDefaultCodeRepository: bool = ...,
        DisassociateAdditionalCodeRepositories: bool = ...,
        RootAccess: RootAccessType = ...,
        InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfigurationTypeDef = ...
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_notebook_instance)
        """

    def update_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
        OnStart: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance lifecycle configuration created with the
        CreateNotebookInstanceLifecycleConfig API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_notebook_instance_lifecycle_config)
        """

    def update_pipeline(
        self,
        *,
        PipelineName: str,
        PipelineDisplayName: str = ...,
        PipelineDefinition: str = ...,
        PipelineDefinitionS3Location: PipelineDefinitionS3LocationTypeDef = ...,
        PipelineDescription: str = ...,
        RoleArn: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...
    ) -> UpdatePipelineResponseTypeDef:
        """
        Updates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_pipeline)
        """

    def update_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        PipelineExecutionDescription: str = ...,
        PipelineExecutionDisplayName: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...
    ) -> UpdatePipelineExecutionResponseTypeDef:
        """
        Updates a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_pipeline_execution)
        """

    def update_project(
        self,
        *,
        ProjectName: str,
        ProjectDescription: str = ...,
        ServiceCatalogProvisioningUpdateDetails: ServiceCatalogProvisioningUpdateDetailsTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates a machine learning (ML) project that is created from a template that
        sets up an ML pipeline from training to deploying an approved model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_project)
        """

    def update_space(
        self, *, DomainId: str, SpaceName: str, SpaceSettings: SpaceSettingsTypeDef = ...
    ) -> UpdateSpaceResponseTypeDef:
        """
        Updates the settings of a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_space)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_space)
        """

    def update_training_job(
        self,
        *,
        TrainingJobName: str,
        ProfilerConfig: ProfilerConfigForUpdateTypeDef = ...,
        ProfilerRuleConfigurations: Sequence[ProfilerRuleConfigurationTypeDef] = ...,
        ResourceConfig: ResourceConfigForUpdateTypeDef = ...
    ) -> UpdateTrainingJobResponseTypeDef:
        """
        Update a model training job to request a new Debugger profiling configuration or
        to change warm pool retention length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_training_job)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_training_job)
        """

    def update_trial(self, *, TrialName: str, DisplayName: str = ...) -> UpdateTrialResponseTypeDef:
        """
        Updates the display name of a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_trial)
        """

    def update_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = ...,
        Status: TrialComponentStatusTypeDef = ...,
        StartTime: Union[datetime, str] = ...,
        EndTime: Union[datetime, str] = ...,
        Parameters: Mapping[str, TrialComponentParameterValueTypeDef] = ...,
        ParametersToRemove: Sequence[str] = ...,
        InputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        InputArtifactsToRemove: Sequence[str] = ...,
        OutputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        OutputArtifactsToRemove: Sequence[str] = ...
    ) -> UpdateTrialComponentResponseTypeDef:
        """
        Updates one or more properties of a trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_trial_component)
        """

    def update_user_profile(
        self, *, DomainId: str, UserProfileName: str, UserSettings: UserSettingsTypeDef = ...
    ) -> UpdateUserProfileResponseTypeDef:
        """
        Updates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_user_profile)
        """

    def update_workforce(
        self,
        *,
        WorkforceName: str,
        SourceIpConfig: SourceIpConfigTypeDef = ...,
        OidcConfig: OidcConfigTypeDef = ...,
        WorkforceVpcConfig: WorkforceVpcConfigRequestTypeDef = ...
    ) -> UpdateWorkforceResponseTypeDef:
        """
        Use this operation to update your workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_workforce)
        """

    def update_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: Sequence[MemberDefinitionTypeDef] = ...,
        Description: str = ...,
        NotificationConfiguration: NotificationConfigurationTypeDef = ...
    ) -> UpdateWorkteamResponseTypeDef:
        """
        Updates an existing work team with new member definitions or description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#update_workteam)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_actions"]) -> ListActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_algorithms"]) -> ListAlgorithmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_image_configs"]
    ) -> ListAppImageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> ListAutoMLJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> ListCandidatesForAutoMLJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> ListCodeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> ListCompilationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contexts"]) -> ListContextsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_quality_job_definitions"]
    ) -> ListDataQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_fleets"]
    ) -> ListDeviceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_deployment_plans"]
    ) -> ListEdgeDeploymentPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_packaging_jobs"]
    ) -> ListEdgePackagingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> ListEndpointConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_feature_groups"]
    ) -> ListFeatureGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> ListFlowDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> ListHumanTaskUisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> ListHyperParameterTuningJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_versions"]
    ) -> ListImageVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_experiments"]
    ) -> ListInferenceExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_job_steps"]
    ) -> ListInferenceRecommendationsJobStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_jobs"]
    ) -> ListInferenceRecommendationsJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> ListLabelingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> ListLabelingJobsForWorkteamPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lineage_groups"]
    ) -> ListLineageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_bias_job_definitions"]
    ) -> ListModelBiasJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_export_jobs"]
    ) -> ListModelCardExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_versions"]
    ) -> ListModelCardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_model_cards"]) -> ListModelCardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_explainability_job_definitions"]
    ) -> ListModelExplainabilityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_metadata"]
    ) -> ListModelMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_package_groups"]
    ) -> ListModelPackageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> ListModelPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_quality_job_definitions"]
    ) -> ListModelQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alert_history"]
    ) -> ListMonitoringAlertHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alerts"]
    ) -> ListMonitoringAlertsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> ListMonitoringExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> ListMonitoringSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> ListNotebookInstanceLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> ListNotebookInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_execution_steps"]
    ) -> ListPipelineExecutionStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_parameters_for_execution"]
    ) -> ListPipelineParametersForExecutionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> ListProcessingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stage_devices"]
    ) -> ListStageDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_lifecycle_configs"]
    ) -> ListStudioLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> ListSubscribedWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> ListTrainingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> ListTransformJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> ListTrialComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trials"]) -> ListTrialsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workforces"]) -> ListWorkforcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workteams"]) -> ListWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_in_service"]) -> EndpointInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_created"]) -> ImageCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_deleted"]) -> ImageDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_updated"]) -> ImageUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_created"]
    ) -> ImageVersionCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_deleted"]
    ) -> ImageVersionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> NotebookInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> NotebookInstanceInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> NotebookInstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> ProcessingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> TrainingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> TransformJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client/#get_waiter)
        """
