"""
Type annotations for sagemaker service literal definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/literals/)

Usage::

    ```python
    from mypy_boto3_sagemaker.literals import ActionStatusType

    data: ActionStatusType = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionStatusType",
    "AlgorithmSortByType",
    "AlgorithmStatusType",
    "AppImageConfigSortKeyType",
    "AppInstanceTypeType",
    "AppNetworkAccessTypeType",
    "AppSecurityGroupManagementType",
    "AppSortKeyType",
    "AppStatusType",
    "AppTypeType",
    "ArtifactSourceIdTypeType",
    "AssemblyTypeType",
    "AssociationEdgeTypeType",
    "AthenaResultCompressionTypeType",
    "AthenaResultFormatType",
    "AuthModeType",
    "AutoMLChannelTypeType",
    "AutoMLJobObjectiveTypeType",
    "AutoMLJobSecondaryStatusType",
    "AutoMLJobStatusType",
    "AutoMLMetricEnumType",
    "AutoMLMetricExtendedEnumType",
    "AutoMLModeType",
    "AutoMLS3DataTypeType",
    "AutoMLSortByType",
    "AutoMLSortOrderType",
    "AwsManagedHumanLoopRequestSourceType",
    "BatchStrategyType",
    "BooleanOperatorType",
    "CandidateSortByType",
    "CandidateStatusType",
    "CandidateStepTypeType",
    "CapacitySizeTypeType",
    "CaptureModeType",
    "CaptureStatusType",
    "ClarifyFeatureTypeType",
    "ClarifyTextGranularityType",
    "ClarifyTextLanguageType",
    "CodeRepositorySortByType",
    "CodeRepositorySortOrderType",
    "CompilationJobStatusType",
    "CompressionTypeType",
    "ConditionOutcomeType",
    "ContainerModeType",
    "ContentClassifierType",
    "DataDistributionTypeType",
    "DetailedAlgorithmStatusType",
    "DetailedModelPackageStatusType",
    "DeviceDeploymentStatusType",
    "DeviceSubsetTypeType",
    "DirectInternetAccessType",
    "DirectionType",
    "DomainStatusType",
    "EdgePackagingJobStatusType",
    "EdgePresetDeploymentStatusType",
    "EdgePresetDeploymentTypeType",
    "EndpointConfigSortKeyType",
    "EndpointDeletedWaiterName",
    "EndpointInServiceWaiterName",
    "EndpointSortKeyType",
    "EndpointStatusType",
    "ExecutionRoleIdentityConfigType",
    "ExecutionStatusType",
    "FailureHandlingPolicyType",
    "FeatureGroupSortByType",
    "FeatureGroupSortOrderType",
    "FeatureGroupStatusType",
    "FeatureStatusType",
    "FeatureTypeType",
    "FileSystemAccessModeType",
    "FileSystemTypeType",
    "FlowDefinitionStatusType",
    "FrameworkType",
    "HubContentSortByType",
    "HubContentStatusType",
    "HubContentTypeType",
    "HubSortByType",
    "HubStatusType",
    "HumanTaskUiStatusType",
    "HyperParameterScalingTypeType",
    "HyperParameterTuningAllocationStrategyType",
    "HyperParameterTuningJobObjectiveTypeType",
    "HyperParameterTuningJobSortByOptionsType",
    "HyperParameterTuningJobStatusType",
    "HyperParameterTuningJobStrategyTypeType",
    "HyperParameterTuningJobWarmStartTypeType",
    "ImageCreatedWaiterName",
    "ImageDeletedWaiterName",
    "ImageSortByType",
    "ImageSortOrderType",
    "ImageStatusType",
    "ImageUpdatedWaiterName",
    "ImageVersionCreatedWaiterName",
    "ImageVersionDeletedWaiterName",
    "ImageVersionSortByType",
    "ImageVersionSortOrderType",
    "ImageVersionStatusType",
    "InferenceExecutionModeType",
    "InferenceExperimentStatusType",
    "InferenceExperimentStopDesiredStateType",
    "InferenceExperimentTypeType",
    "InputModeType",
    "InstanceTypeType",
    "JobTypeType",
    "JoinSourceType",
    "LabelingJobStatusType",
    "LastUpdateStatusValueType",
    "LineageTypeType",
    "ListActionsPaginatorName",
    "ListAlgorithmsPaginatorName",
    "ListAliasesPaginatorName",
    "ListAppImageConfigsPaginatorName",
    "ListAppsPaginatorName",
    "ListArtifactsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListAutoMLJobsPaginatorName",
    "ListCandidatesForAutoMLJobPaginatorName",
    "ListCodeRepositoriesPaginatorName",
    "ListCompilationJobsPaginatorName",
    "ListCompilationJobsSortByType",
    "ListContextsPaginatorName",
    "ListDataQualityJobDefinitionsPaginatorName",
    "ListDeviceFleetsPaginatorName",
    "ListDeviceFleetsSortByType",
    "ListDevicesPaginatorName",
    "ListDomainsPaginatorName",
    "ListEdgeDeploymentPlansPaginatorName",
    "ListEdgeDeploymentPlansSortByType",
    "ListEdgePackagingJobsPaginatorName",
    "ListEdgePackagingJobsSortByType",
    "ListEndpointConfigsPaginatorName",
    "ListEndpointsPaginatorName",
    "ListExperimentsPaginatorName",
    "ListFeatureGroupsPaginatorName",
    "ListFlowDefinitionsPaginatorName",
    "ListHumanTaskUisPaginatorName",
    "ListHyperParameterTuningJobsPaginatorName",
    "ListImageVersionsPaginatorName",
    "ListImagesPaginatorName",
    "ListInferenceExperimentsPaginatorName",
    "ListInferenceRecommendationsJobStepsPaginatorName",
    "ListInferenceRecommendationsJobsPaginatorName",
    "ListInferenceRecommendationsJobsSortByType",
    "ListLabelingJobsForWorkteamPaginatorName",
    "ListLabelingJobsForWorkteamSortByOptionsType",
    "ListLabelingJobsPaginatorName",
    "ListLineageGroupsPaginatorName",
    "ListModelBiasJobDefinitionsPaginatorName",
    "ListModelCardExportJobsPaginatorName",
    "ListModelCardVersionsPaginatorName",
    "ListModelCardsPaginatorName",
    "ListModelExplainabilityJobDefinitionsPaginatorName",
    "ListModelMetadataPaginatorName",
    "ListModelPackageGroupsPaginatorName",
    "ListModelPackagesPaginatorName",
    "ListModelQualityJobDefinitionsPaginatorName",
    "ListModelsPaginatorName",
    "ListMonitoringAlertHistoryPaginatorName",
    "ListMonitoringAlertsPaginatorName",
    "ListMonitoringExecutionsPaginatorName",
    "ListMonitoringSchedulesPaginatorName",
    "ListNotebookInstanceLifecycleConfigsPaginatorName",
    "ListNotebookInstancesPaginatorName",
    "ListPipelineExecutionStepsPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelineParametersForExecutionPaginatorName",
    "ListPipelinesPaginatorName",
    "ListProcessingJobsPaginatorName",
    "ListSpacesPaginatorName",
    "ListStageDevicesPaginatorName",
    "ListStudioLifecycleConfigsPaginatorName",
    "ListSubscribedWorkteamsPaginatorName",
    "ListTagsPaginatorName",
    "ListTrainingJobsForHyperParameterTuningJobPaginatorName",
    "ListTrainingJobsPaginatorName",
    "ListTransformJobsPaginatorName",
    "ListTrialComponentsPaginatorName",
    "ListTrialsPaginatorName",
    "ListUserProfilesPaginatorName",
    "ListWorkforcesPaginatorName",
    "ListWorkforcesSortByOptionsType",
    "ListWorkteamsPaginatorName",
    "ListWorkteamsSortByOptionsType",
    "MetricSetSourceType",
    "ModelApprovalStatusType",
    "ModelCacheSettingType",
    "ModelCardExportJobSortByType",
    "ModelCardExportJobSortOrderType",
    "ModelCardExportJobStatusType",
    "ModelCardProcessingStatusType",
    "ModelCardSortByType",
    "ModelCardSortOrderType",
    "ModelCardStatusType",
    "ModelCardVersionSortByType",
    "ModelInfrastructureTypeType",
    "ModelMetadataFilterTypeType",
    "ModelPackageGroupSortByType",
    "ModelPackageGroupStatusType",
    "ModelPackageSortByType",
    "ModelPackageStatusType",
    "ModelPackageTypeType",
    "ModelSortKeyType",
    "ModelVariantActionType",
    "ModelVariantStatusType",
    "MonitoringAlertHistorySortKeyType",
    "MonitoringAlertStatusType",
    "MonitoringExecutionSortKeyType",
    "MonitoringJobDefinitionSortKeyType",
    "MonitoringProblemTypeType",
    "MonitoringScheduleSortKeyType",
    "MonitoringTypeType",
    "NotebookInstanceAcceleratorTypeType",
    "NotebookInstanceDeletedWaiterName",
    "NotebookInstanceInServiceWaiterName",
    "NotebookInstanceLifecycleConfigSortKeyType",
    "NotebookInstanceLifecycleConfigSortOrderType",
    "NotebookInstanceSortKeyType",
    "NotebookInstanceSortOrderType",
    "NotebookInstanceStatusType",
    "NotebookInstanceStoppedWaiterName",
    "NotebookOutputOptionType",
    "ObjectiveStatusType",
    "OfflineStoreStatusValueType",
    "OperatorType",
    "OrderKeyType",
    "ParameterTypeType",
    "PipelineExecutionStatusType",
    "PipelineStatusType",
    "ProblemTypeType",
    "ProcessingInstanceTypeType",
    "ProcessingJobCompletedOrStoppedWaiterName",
    "ProcessingJobStatusType",
    "ProcessingS3CompressionTypeType",
    "ProcessingS3DataDistributionTypeType",
    "ProcessingS3DataTypeType",
    "ProcessingS3InputModeType",
    "ProcessingS3UploadModeType",
    "ProcessorType",
    "ProductionVariantAcceleratorTypeType",
    "ProductionVariantInstanceTypeType",
    "ProfilingStatusType",
    "ProjectSortByType",
    "ProjectSortOrderType",
    "ProjectStatusType",
    "RStudioServerProAccessStatusType",
    "RStudioServerProUserGroupType",
    "RecommendationJobStatusType",
    "RecommendationJobTypeType",
    "RecommendationStepTypeType",
    "RecordWrapperType",
    "RedshiftResultCompressionTypeType",
    "RedshiftResultFormatType",
    "RepositoryAccessModeType",
    "ResourceTypeType",
    "RetentionTypeType",
    "RootAccessType",
    "RuleEvaluationStatusType",
    "S3DataDistributionType",
    "S3DataTypeType",
    "SagemakerServicecatalogStatusType",
    "ScheduleStatusType",
    "SearchPaginatorName",
    "SearchSortOrderType",
    "SecondaryStatusType",
    "SortActionsByType",
    "SortArtifactsByType",
    "SortAssociationsByType",
    "SortByType",
    "SortContextsByType",
    "SortExperimentsByType",
    "SortInferenceExperimentsByType",
    "SortLineageGroupsByType",
    "SortOrderType",
    "SortPipelineExecutionsByType",
    "SortPipelinesByType",
    "SortTrialComponentsByType",
    "SortTrialsByType",
    "SpaceSortKeyType",
    "SpaceStatusType",
    "SplitTypeType",
    "StageStatusType",
    "StepStatusType",
    "StudioLifecycleConfigAppTypeType",
    "StudioLifecycleConfigSortKeyType",
    "TableFormatType",
    "TargetDeviceType",
    "TargetPlatformAcceleratorType",
    "TargetPlatformArchType",
    "TargetPlatformOsType",
    "TrafficRoutingConfigTypeType",
    "TrafficTypeType",
    "TrainingInputModeType",
    "TrainingInstanceTypeType",
    "TrainingJobCompletedOrStoppedWaiterName",
    "TrainingJobEarlyStoppingTypeType",
    "TrainingJobSortByOptionsType",
    "TrainingJobStatusType",
    "TransformInstanceTypeType",
    "TransformJobCompletedOrStoppedWaiterName",
    "TransformJobStatusType",
    "TrialComponentPrimaryStatusType",
    "UserProfileSortKeyType",
    "UserProfileStatusType",
    "VariantPropertyTypeType",
    "VariantStatusType",
    "VendorGuidanceType",
    "WarmPoolResourceStatusType",
    "WorkforceStatusType",
    "SageMakerServiceName",
    "ServiceName",
    "ResourceServiceName",
    "PaginatorName",
    "WaiterName",
    "RegionName",
)


ActionStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
AlgorithmSortByType = Literal["CreationTime", "Name"]
AlgorithmStatusType = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
AppImageConfigSortKeyType = Literal["CreationTime", "LastModifiedTime", "Name"]
AppInstanceTypeType = Literal[
    "ml.c5.12xlarge",
    "ml.c5.18xlarge",
    "ml.c5.24xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.2xlarge",
    "ml.g5.48xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.16xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.8xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.16xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.8xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.micro",
    "ml.t3.small",
    "ml.t3.xlarge",
    "system",
]
AppNetworkAccessTypeType = Literal["PublicInternetOnly", "VpcOnly"]
AppSecurityGroupManagementType = Literal["Customer", "Service"]
AppSortKeyType = Literal["CreationTime"]
AppStatusType = Literal["Deleted", "Deleting", "Failed", "InService", "Pending"]
AppTypeType = Literal[
    "JupyterServer", "KernelGateway", "RSessionGateway", "RStudioServerPro", "TensorBoard"
]
ArtifactSourceIdTypeType = Literal["Custom", "MD5Hash", "S3ETag", "S3Version"]
AssemblyTypeType = Literal["Line", "None"]
AssociationEdgeTypeType = Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
AthenaResultCompressionTypeType = Literal["GZIP", "SNAPPY", "ZLIB"]
AthenaResultFormatType = Literal["AVRO", "JSON", "ORC", "PARQUET", "TEXTFILE"]
AuthModeType = Literal["IAM", "SSO"]
AutoMLChannelTypeType = Literal["training", "validation"]
AutoMLJobObjectiveTypeType = Literal["Maximize", "Minimize"]
AutoMLJobSecondaryStatusType = Literal[
    "AnalyzingData",
    "CandidateDefinitionsGenerated",
    "Completed",
    "DeployingModel",
    "ExplainabilityError",
    "Failed",
    "FeatureEngineering",
    "GeneratingExplainabilityReport",
    "GeneratingModelInsightsReport",
    "MaxAutoMLJobRuntimeReached",
    "MaxCandidatesReached",
    "ModelDeploymentError",
    "ModelInsightsError",
    "ModelTuning",
    "Starting",
    "Stopped",
    "Stopping",
]
AutoMLJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
AutoMLMetricEnumType = Literal[
    "AUC",
    "Accuracy",
    "BalancedAccuracy",
    "F1",
    "F1macro",
    "MAE",
    "MSE",
    "Precision",
    "PrecisionMacro",
    "R2",
    "RMSE",
    "Recall",
    "RecallMacro",
]
AutoMLMetricExtendedEnumType = Literal[
    "AUC",
    "Accuracy",
    "BalancedAccuracy",
    "F1",
    "F1macro",
    "InferenceLatency",
    "LogLoss",
    "MAE",
    "MSE",
    "Precision",
    "PrecisionMacro",
    "R2",
    "RMSE",
    "Recall",
    "RecallMacro",
]
AutoMLModeType = Literal["AUTO", "ENSEMBLING", "HYPERPARAMETER_TUNING"]
AutoMLS3DataTypeType = Literal["ManifestFile", "S3Prefix"]
AutoMLSortByType = Literal["CreationTime", "Name", "Status"]
AutoMLSortOrderType = Literal["Ascending", "Descending"]
AwsManagedHumanLoopRequestSourceType = Literal[
    "AWS/Rekognition/DetectModerationLabels/Image/V3", "AWS/Textract/AnalyzeDocument/Forms/V1"
]
BatchStrategyType = Literal["MultiRecord", "SingleRecord"]
BooleanOperatorType = Literal["And", "Or"]
CandidateSortByType = Literal["CreationTime", "FinalObjectiveMetricValue", "Status"]
CandidateStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
CandidateStepTypeType = Literal[
    "AWS::SageMaker::ProcessingJob", "AWS::SageMaker::TrainingJob", "AWS::SageMaker::TransformJob"
]
CapacitySizeTypeType = Literal["CAPACITY_PERCENT", "INSTANCE_COUNT"]
CaptureModeType = Literal["Input", "Output"]
CaptureStatusType = Literal["Started", "Stopped"]
ClarifyFeatureTypeType = Literal["categorical", "numerical", "text"]
ClarifyTextGranularityType = Literal["paragraph", "sentence", "token"]
ClarifyTextLanguageType = Literal[
    "af",
    "ar",
    "bg",
    "bn",
    "ca",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "ga",
    "gu",
    "he",
    "hi",
    "hr",
    "hu",
    "hy",
    "id",
    "is",
    "it",
    "kn",
    "ky",
    "lb",
    "lij",
    "lt",
    "lv",
    "mk",
    "ml",
    "mr",
    "nb",
    "ne",
    "nl",
    "pl",
    "pt",
    "ro",
    "ru",
    "sa",
    "si",
    "sk",
    "sl",
    "sq",
    "sr",
    "sv",
    "ta",
    "te",
    "tl",
    "tn",
    "tr",
    "tt",
    "uk",
    "ur",
    "xx",
    "yo",
    "zh",
]
CodeRepositorySortByType = Literal["CreationTime", "LastModifiedTime", "Name"]
CodeRepositorySortOrderType = Literal["Ascending", "Descending"]
CompilationJobStatusType = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
CompressionTypeType = Literal["Gzip", "None"]
ConditionOutcomeType = Literal["False", "True"]
ContainerModeType = Literal["MultiModel", "SingleModel"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
DataDistributionTypeType = Literal["FullyReplicated", "ShardedByS3Key"]
DetailedAlgorithmStatusType = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DetailedModelPackageStatusType = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DeviceDeploymentStatusType = Literal[
    "DEPLOYED", "FAILED", "INPROGRESS", "READYTODEPLOY", "STOPPED", "STOPPING"
]
DeviceSubsetTypeType = Literal["NAMECONTAINS", "PERCENTAGE", "SELECTION"]
DirectInternetAccessType = Literal["Disabled", "Enabled"]
DirectionType = Literal["Ascendants", "Both", "Descendants"]
DomainStatusType = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
EdgePackagingJobStatusType = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
EdgePresetDeploymentStatusType = Literal["COMPLETED", "FAILED"]
EdgePresetDeploymentTypeType = Literal["GreengrassV2Component"]
EndpointConfigSortKeyType = Literal["CreationTime", "Name"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointInServiceWaiterName = Literal["endpoint_in_service"]
EndpointSortKeyType = Literal["CreationTime", "Name", "Status"]
EndpointStatusType = Literal[
    "Creating",
    "Deleting",
    "Failed",
    "InService",
    "OutOfService",
    "RollingBack",
    "SystemUpdating",
    "Updating",
]
ExecutionRoleIdentityConfigType = Literal["DISABLED", "USER_PROFILE_NAME"]
ExecutionStatusType = Literal[
    "Completed", "CompletedWithViolations", "Failed", "InProgress", "Pending", "Stopped", "Stopping"
]
FailureHandlingPolicyType = Literal["DO_NOTHING", "ROLLBACK_ON_FAILURE"]
FeatureGroupSortByType = Literal["CreationTime", "FeatureGroupStatus", "Name", "OfflineStoreStatus"]
FeatureGroupSortOrderType = Literal["Ascending", "Descending"]
FeatureGroupStatusType = Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
FeatureStatusType = Literal["DISABLED", "ENABLED"]
FeatureTypeType = Literal["Fractional", "Integral", "String"]
FileSystemAccessModeType = Literal["ro", "rw"]
FileSystemTypeType = Literal["EFS", "FSxLustre"]
FlowDefinitionStatusType = Literal["Active", "Deleting", "Failed", "Initializing"]
FrameworkType = Literal[
    "DARKNET", "KERAS", "MXNET", "ONNX", "PYTORCH", "SKLEARN", "TENSORFLOW", "TFLITE", "XGBOOST"
]
HubContentSortByType = Literal["CreationTime", "HubContentName", "HubContentStatus"]
HubContentStatusType = Literal["Available", "DeleteFailed", "Deleting", "ImportFailed", "Importing"]
HubContentTypeType = Literal["Model", "Notebook"]
HubSortByType = Literal["AccountIdOwner", "CreationTime", "HubName", "HubStatus"]
HubStatusType = Literal[
    "CreateFailed", "Creating", "DeleteFailed", "Deleting", "InService", "UpdateFailed", "Updating"
]
HumanTaskUiStatusType = Literal["Active", "Deleting"]
HyperParameterScalingTypeType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
HyperParameterTuningAllocationStrategyType = Literal["Prioritized"]
HyperParameterTuningJobObjectiveTypeType = Literal["Maximize", "Minimize"]
HyperParameterTuningJobSortByOptionsType = Literal["CreationTime", "Name", "Status"]
HyperParameterTuningJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
HyperParameterTuningJobStrategyTypeType = Literal["Bayesian", "Grid", "Hyperband", "Random"]
HyperParameterTuningJobWarmStartTypeType = Literal["IdenticalDataAndAlgorithm", "TransferLearning"]
ImageCreatedWaiterName = Literal["image_created"]
ImageDeletedWaiterName = Literal["image_deleted"]
ImageSortByType = Literal["CREATION_TIME", "IMAGE_NAME", "LAST_MODIFIED_TIME"]
ImageSortOrderType = Literal["ASCENDING", "DESCENDING"]
ImageStatusType = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
ImageUpdatedWaiterName = Literal["image_updated"]
ImageVersionCreatedWaiterName = Literal["image_version_created"]
ImageVersionDeletedWaiterName = Literal["image_version_deleted"]
ImageVersionSortByType = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"]
ImageVersionSortOrderType = Literal["ASCENDING", "DESCENDING"]
ImageVersionStatusType = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
]
InferenceExecutionModeType = Literal["Direct", "Serial"]
InferenceExperimentStatusType = Literal[
    "Cancelled", "Completed", "Created", "Creating", "Running", "Starting", "Stopping", "Updating"
]
InferenceExperimentStopDesiredStateType = Literal["Cancelled", "Completed"]
InferenceExperimentTypeType = Literal["ShadowMode"]
InputModeType = Literal["File", "Pipe"]
InstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.2xlarge",
    "ml.g5.48xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.16xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.8xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
JobTypeType = Literal["INFERENCE", "NOTEBOOK_KERNEL", "TRAINING"]
JoinSourceType = Literal["Input", "None"]
LabelingJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
]
LastUpdateStatusValueType = Literal["Failed", "InProgress", "Successful"]
LineageTypeType = Literal["Action", "Artifact", "Context", "TrialComponent"]
ListActionsPaginatorName = Literal["list_actions"]
ListAlgorithmsPaginatorName = Literal["list_algorithms"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListAppImageConfigsPaginatorName = Literal["list_app_image_configs"]
ListAppsPaginatorName = Literal["list_apps"]
ListArtifactsPaginatorName = Literal["list_artifacts"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListAutoMLJobsPaginatorName = Literal["list_auto_ml_jobs"]
ListCandidatesForAutoMLJobPaginatorName = Literal["list_candidates_for_auto_ml_job"]
ListCodeRepositoriesPaginatorName = Literal["list_code_repositories"]
ListCompilationJobsPaginatorName = Literal["list_compilation_jobs"]
ListCompilationJobsSortByType = Literal["CreationTime", "Name", "Status"]
ListContextsPaginatorName = Literal["list_contexts"]
ListDataQualityJobDefinitionsPaginatorName = Literal["list_data_quality_job_definitions"]
ListDeviceFleetsPaginatorName = Literal["list_device_fleets"]
ListDeviceFleetsSortByType = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "NAME"]
ListDevicesPaginatorName = Literal["list_devices"]
ListDomainsPaginatorName = Literal["list_domains"]
ListEdgeDeploymentPlansPaginatorName = Literal["list_edge_deployment_plans"]
ListEdgeDeploymentPlansSortByType = Literal[
    "CREATION_TIME", "DEVICE_FLEET_NAME", "LAST_MODIFIED_TIME", "NAME"
]
ListEdgePackagingJobsPaginatorName = Literal["list_edge_packaging_jobs"]
ListEdgePackagingJobsSortByType = Literal[
    "CREATION_TIME", "LAST_MODIFIED_TIME", "MODEL_NAME", "NAME", "STATUS"
]
ListEndpointConfigsPaginatorName = Literal["list_endpoint_configs"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
ListExperimentsPaginatorName = Literal["list_experiments"]
ListFeatureGroupsPaginatorName = Literal["list_feature_groups"]
ListFlowDefinitionsPaginatorName = Literal["list_flow_definitions"]
ListHumanTaskUisPaginatorName = Literal["list_human_task_uis"]
ListHyperParameterTuningJobsPaginatorName = Literal["list_hyper_parameter_tuning_jobs"]
ListImageVersionsPaginatorName = Literal["list_image_versions"]
ListImagesPaginatorName = Literal["list_images"]
ListInferenceExperimentsPaginatorName = Literal["list_inference_experiments"]
ListInferenceRecommendationsJobStepsPaginatorName = Literal[
    "list_inference_recommendations_job_steps"
]
ListInferenceRecommendationsJobsPaginatorName = Literal["list_inference_recommendations_jobs"]
ListInferenceRecommendationsJobsSortByType = Literal["CreationTime", "Name", "Status"]
ListLabelingJobsForWorkteamPaginatorName = Literal["list_labeling_jobs_for_workteam"]
ListLabelingJobsForWorkteamSortByOptionsType = Literal["CreationTime"]
ListLabelingJobsPaginatorName = Literal["list_labeling_jobs"]
ListLineageGroupsPaginatorName = Literal["list_lineage_groups"]
ListModelBiasJobDefinitionsPaginatorName = Literal["list_model_bias_job_definitions"]
ListModelCardExportJobsPaginatorName = Literal["list_model_card_export_jobs"]
ListModelCardVersionsPaginatorName = Literal["list_model_card_versions"]
ListModelCardsPaginatorName = Literal["list_model_cards"]
ListModelExplainabilityJobDefinitionsPaginatorName = Literal[
    "list_model_explainability_job_definitions"
]
ListModelMetadataPaginatorName = Literal["list_model_metadata"]
ListModelPackageGroupsPaginatorName = Literal["list_model_package_groups"]
ListModelPackagesPaginatorName = Literal["list_model_packages"]
ListModelQualityJobDefinitionsPaginatorName = Literal["list_model_quality_job_definitions"]
ListModelsPaginatorName = Literal["list_models"]
ListMonitoringAlertHistoryPaginatorName = Literal["list_monitoring_alert_history"]
ListMonitoringAlertsPaginatorName = Literal["list_monitoring_alerts"]
ListMonitoringExecutionsPaginatorName = Literal["list_monitoring_executions"]
ListMonitoringSchedulesPaginatorName = Literal["list_monitoring_schedules"]
ListNotebookInstanceLifecycleConfigsPaginatorName = Literal[
    "list_notebook_instance_lifecycle_configs"
]
ListNotebookInstancesPaginatorName = Literal["list_notebook_instances"]
ListPipelineExecutionStepsPaginatorName = Literal["list_pipeline_execution_steps"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelineParametersForExecutionPaginatorName = Literal["list_pipeline_parameters_for_execution"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListProcessingJobsPaginatorName = Literal["list_processing_jobs"]
ListSpacesPaginatorName = Literal["list_spaces"]
ListStageDevicesPaginatorName = Literal["list_stage_devices"]
ListStudioLifecycleConfigsPaginatorName = Literal["list_studio_lifecycle_configs"]
ListSubscribedWorkteamsPaginatorName = Literal["list_subscribed_workteams"]
ListTagsPaginatorName = Literal["list_tags"]
ListTrainingJobsForHyperParameterTuningJobPaginatorName = Literal[
    "list_training_jobs_for_hyper_parameter_tuning_job"
]
ListTrainingJobsPaginatorName = Literal["list_training_jobs"]
ListTransformJobsPaginatorName = Literal["list_transform_jobs"]
ListTrialComponentsPaginatorName = Literal["list_trial_components"]
ListTrialsPaginatorName = Literal["list_trials"]
ListUserProfilesPaginatorName = Literal["list_user_profiles"]
ListWorkforcesPaginatorName = Literal["list_workforces"]
ListWorkforcesSortByOptionsType = Literal["CreateDate", "Name"]
ListWorkteamsPaginatorName = Literal["list_workteams"]
ListWorkteamsSortByOptionsType = Literal["CreateDate", "Name"]
MetricSetSourceType = Literal["Test", "Train", "Validation"]
ModelApprovalStatusType = Literal["Approved", "PendingManualApproval", "Rejected"]
ModelCacheSettingType = Literal["Disabled", "Enabled"]
ModelCardExportJobSortByType = Literal["CreationTime", "Name", "Status"]
ModelCardExportJobSortOrderType = Literal["Ascending", "Descending"]
ModelCardExportJobStatusType = Literal["Completed", "Failed", "InProgress"]
ModelCardProcessingStatusType = Literal[
    "ContentDeleted",
    "DeleteCompleted",
    "DeleteFailed",
    "DeleteInProgress",
    "DeletePending",
    "ExportJobsDeleted",
]
ModelCardSortByType = Literal["CreationTime", "Name"]
ModelCardSortOrderType = Literal["Ascending", "Descending"]
ModelCardStatusType = Literal["Approved", "Archived", "Draft", "PendingReview"]
ModelCardVersionSortByType = Literal["Version"]
ModelInfrastructureTypeType = Literal["RealTimeInference"]
ModelMetadataFilterTypeType = Literal["Domain", "Framework", "FrameworkVersion", "Task"]
ModelPackageGroupSortByType = Literal["CreationTime", "Name"]
ModelPackageGroupStatusType = Literal[
    "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
]
ModelPackageSortByType = Literal["CreationTime", "Name"]
ModelPackageStatusType = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
ModelPackageTypeType = Literal["Both", "Unversioned", "Versioned"]
ModelSortKeyType = Literal["CreationTime", "Name"]
ModelVariantActionType = Literal["Promote", "Remove", "Retain"]
ModelVariantStatusType = Literal["Creating", "Deleted", "Deleting", "InService", "Updating"]
MonitoringAlertHistorySortKeyType = Literal["CreationTime", "Status"]
MonitoringAlertStatusType = Literal["InAlert", "OK"]
MonitoringExecutionSortKeyType = Literal["CreationTime", "ScheduledTime", "Status"]
MonitoringJobDefinitionSortKeyType = Literal["CreationTime", "Name"]
MonitoringProblemTypeType = Literal[
    "BinaryClassification", "MulticlassClassification", "Regression"
]
MonitoringScheduleSortKeyType = Literal["CreationTime", "Name", "Status"]
MonitoringTypeType = Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
NotebookInstanceAcceleratorTypeType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
NotebookInstanceDeletedWaiterName = Literal["notebook_instance_deleted"]
NotebookInstanceInServiceWaiterName = Literal["notebook_instance_in_service"]
NotebookInstanceLifecycleConfigSortKeyType = Literal["CreationTime", "LastModifiedTime", "Name"]
NotebookInstanceLifecycleConfigSortOrderType = Literal["Ascending", "Descending"]
NotebookInstanceSortKeyType = Literal["CreationTime", "Name", "Status"]
NotebookInstanceSortOrderType = Literal["Ascending", "Descending"]
NotebookInstanceStatusType = Literal[
    "Deleting", "Failed", "InService", "Pending", "Stopped", "Stopping", "Updating"
]
NotebookInstanceStoppedWaiterName = Literal["notebook_instance_stopped"]
NotebookOutputOptionType = Literal["Allowed", "Disabled"]
ObjectiveStatusType = Literal["Failed", "Pending", "Succeeded"]
OfflineStoreStatusValueType = Literal["Active", "Blocked", "Disabled"]
OperatorType = Literal[
    "Contains",
    "Equals",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEquals",
    "NotExists",
]
OrderKeyType = Literal["Ascending", "Descending"]
ParameterTypeType = Literal["Categorical", "Continuous", "FreeText", "Integer"]
PipelineExecutionStatusType = Literal["Executing", "Failed", "Stopped", "Stopping", "Succeeded"]
PipelineStatusType = Literal["Active"]
ProblemTypeType = Literal["BinaryClassification", "MulticlassClassification", "Regression"]
ProcessingInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
ProcessingJobCompletedOrStoppedWaiterName = Literal["processing_job_completed_or_stopped"]
ProcessingJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
ProcessingS3CompressionTypeType = Literal["Gzip", "None"]
ProcessingS3DataDistributionTypeType = Literal["FullyReplicated", "ShardedByS3Key"]
ProcessingS3DataTypeType = Literal["ManifestFile", "S3Prefix"]
ProcessingS3InputModeType = Literal["File", "Pipe"]
ProcessingS3UploadModeType = Literal["Continuous", "EndOfJob"]
ProcessorType = Literal["CPU", "GPU"]
ProductionVariantAcceleratorTypeType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
ProductionVariantInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.large",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.large",
    "ml.c5d.xlarge",
    "ml.c6g.12xlarge",
    "ml.c6g.16xlarge",
    "ml.c6g.2xlarge",
    "ml.c6g.4xlarge",
    "ml.c6g.8xlarge",
    "ml.c6g.large",
    "ml.c6g.xlarge",
    "ml.c6gd.12xlarge",
    "ml.c6gd.16xlarge",
    "ml.c6gd.2xlarge",
    "ml.c6gd.4xlarge",
    "ml.c6gd.8xlarge",
    "ml.c6gd.large",
    "ml.c6gd.xlarge",
    "ml.c6gn.12xlarge",
    "ml.c6gn.16xlarge",
    "ml.c6gn.2xlarge",
    "ml.c6gn.4xlarge",
    "ml.c6gn.8xlarge",
    "ml.c6gn.large",
    "ml.c6gn.xlarge",
    "ml.c6i.12xlarge",
    "ml.c6i.16xlarge",
    "ml.c6i.24xlarge",
    "ml.c6i.2xlarge",
    "ml.c6i.32xlarge",
    "ml.c6i.4xlarge",
    "ml.c6i.8xlarge",
    "ml.c6i.large",
    "ml.c6i.xlarge",
    "ml.c7g.12xlarge",
    "ml.c7g.16xlarge",
    "ml.c7g.2xlarge",
    "ml.c7g.4xlarge",
    "ml.c7g.8xlarge",
    "ml.c7g.large",
    "ml.c7g.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.2xlarge",
    "ml.g5.48xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.xlarge",
    "ml.inf1.24xlarge",
    "ml.inf1.2xlarge",
    "ml.inf1.6xlarge",
    "ml.inf1.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.m6g.12xlarge",
    "ml.m6g.16xlarge",
    "ml.m6g.2xlarge",
    "ml.m6g.4xlarge",
    "ml.m6g.8xlarge",
    "ml.m6g.large",
    "ml.m6g.xlarge",
    "ml.m6gd.12xlarge",
    "ml.m6gd.16xlarge",
    "ml.m6gd.2xlarge",
    "ml.m6gd.4xlarge",
    "ml.m6gd.8xlarge",
    "ml.m6gd.large",
    "ml.m6gd.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p4d.24xlarge",
    "ml.r5.12xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.r5d.12xlarge",
    "ml.r5d.24xlarge",
    "ml.r5d.2xlarge",
    "ml.r5d.4xlarge",
    "ml.r5d.large",
    "ml.r5d.xlarge",
    "ml.r6g.12xlarge",
    "ml.r6g.16xlarge",
    "ml.r6g.2xlarge",
    "ml.r6g.4xlarge",
    "ml.r6g.8xlarge",
    "ml.r6g.large",
    "ml.r6g.xlarge",
    "ml.r6gd.12xlarge",
    "ml.r6gd.16xlarge",
    "ml.r6gd.2xlarge",
    "ml.r6gd.4xlarge",
    "ml.r6gd.8xlarge",
    "ml.r6gd.large",
    "ml.r6gd.xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
]
ProfilingStatusType = Literal["Disabled", "Enabled"]
ProjectSortByType = Literal["CreationTime", "Name"]
ProjectSortOrderType = Literal["Ascending", "Descending"]
ProjectStatusType = Literal[
    "CreateCompleted",
    "CreateFailed",
    "CreateInProgress",
    "DeleteCompleted",
    "DeleteFailed",
    "DeleteInProgress",
    "Pending",
    "UpdateCompleted",
    "UpdateFailed",
    "UpdateInProgress",
]
RStudioServerProAccessStatusType = Literal["DISABLED", "ENABLED"]
RStudioServerProUserGroupType = Literal["R_STUDIO_ADMIN", "R_STUDIO_USER"]
RecommendationJobStatusType = Literal[
    "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"
]
RecommendationJobTypeType = Literal["Advanced", "Default"]
RecommendationStepTypeType = Literal["BENCHMARK"]
RecordWrapperType = Literal["None", "RecordIO"]
RedshiftResultCompressionTypeType = Literal["BZIP2", "GZIP", "None", "SNAPPY", "ZSTD"]
RedshiftResultFormatType = Literal["CSV", "PARQUET"]
RepositoryAccessModeType = Literal["Platform", "Vpc"]
ResourceTypeType = Literal[
    "Endpoint",
    "Experiment",
    "ExperimentTrial",
    "ExperimentTrialComponent",
    "FeatureGroup",
    "FeatureMetadata",
    "HyperParameterTuningJob",
    "Model",
    "ModelCard",
    "ModelPackage",
    "ModelPackageGroup",
    "Pipeline",
    "PipelineExecution",
    "Project",
    "TrainingJob",
]
RetentionTypeType = Literal["Delete", "Retain"]
RootAccessType = Literal["Disabled", "Enabled"]
RuleEvaluationStatusType = Literal[
    "Error", "InProgress", "IssuesFound", "NoIssuesFound", "Stopped", "Stopping"
]
S3DataDistributionType = Literal["FullyReplicated", "ShardedByS3Key"]
S3DataTypeType = Literal["AugmentedManifestFile", "ManifestFile", "S3Prefix"]
SagemakerServicecatalogStatusType = Literal["Disabled", "Enabled"]
ScheduleStatusType = Literal["Failed", "Pending", "Scheduled", "Stopped"]
SearchPaginatorName = Literal["search"]
SearchSortOrderType = Literal["Ascending", "Descending"]
SecondaryStatusType = Literal[
    "Completed",
    "Downloading",
    "DownloadingTrainingImage",
    "Failed",
    "Interrupted",
    "LaunchingMLInstances",
    "MaxRuntimeExceeded",
    "MaxWaitTimeExceeded",
    "PreparingTrainingStack",
    "Restarting",
    "Starting",
    "Stopped",
    "Stopping",
    "Training",
    "Updating",
    "Uploading",
]
SortActionsByType = Literal["CreationTime", "Name"]
SortArtifactsByType = Literal["CreationTime"]
SortAssociationsByType = Literal[
    "CreationTime", "DestinationArn", "DestinationType", "SourceArn", "SourceType"
]
SortByType = Literal["CreationTime", "Name", "Status"]
SortContextsByType = Literal["CreationTime", "Name"]
SortExperimentsByType = Literal["CreationTime", "Name"]
SortInferenceExperimentsByType = Literal["CreationTime", "Name", "Status"]
SortLineageGroupsByType = Literal["CreationTime", "Name"]
SortOrderType = Literal["Ascending", "Descending"]
SortPipelineExecutionsByType = Literal["CreationTime", "PipelineExecutionArn"]
SortPipelinesByType = Literal["CreationTime", "Name"]
SortTrialComponentsByType = Literal["CreationTime", "Name"]
SortTrialsByType = Literal["CreationTime", "Name"]
SpaceSortKeyType = Literal["CreationTime", "LastModifiedTime"]
SpaceStatusType = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
SplitTypeType = Literal["Line", "None", "RecordIO", "TFRecord"]
StageStatusType = Literal[
    "CREATING",
    "DEPLOYED",
    "FAILED",
    "INPROGRESS",
    "READYTODEPLOY",
    "STARTING",
    "STOPPED",
    "STOPPING",
]
StepStatusType = Literal["Executing", "Failed", "Starting", "Stopped", "Stopping", "Succeeded"]
StudioLifecycleConfigAppTypeType = Literal["JupyterServer", "KernelGateway"]
StudioLifecycleConfigSortKeyType = Literal["CreationTime", "LastModifiedTime", "Name"]
TableFormatType = Literal["Glue", "Iceberg"]
TargetDeviceType = Literal[
    "aisage",
    "amba_cv2",
    "amba_cv22",
    "amba_cv25",
    "coreml",
    "deeplens",
    "imx8mplus",
    "imx8qm",
    "jacinto_tda4vm",
    "jetson_nano",
    "jetson_tx1",
    "jetson_tx2",
    "jetson_xavier",
    "lambda",
    "ml_c4",
    "ml_c5",
    "ml_eia2",
    "ml_g4dn",
    "ml_inf1",
    "ml_m4",
    "ml_m5",
    "ml_p2",
    "ml_p3",
    "qcs603",
    "qcs605",
    "rasp3b",
    "rk3288",
    "rk3399",
    "sbe_c",
    "sitara_am57x",
    "x86_win32",
    "x86_win64",
]
TargetPlatformAcceleratorType = Literal["INTEL_GRAPHICS", "MALI", "NNA", "NVIDIA"]
TargetPlatformArchType = Literal["ARM64", "ARM_EABI", "ARM_EABIHF", "X86", "X86_64"]
TargetPlatformOsType = Literal["ANDROID", "LINUX"]
TrafficRoutingConfigTypeType = Literal["ALL_AT_ONCE", "CANARY", "LINEAR"]
TrafficTypeType = Literal["PHASES"]
TrainingInputModeType = Literal["FastFile", "File", "Pipe"]
TrainingInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5n.18xlarge",
    "ml.c5n.2xlarge",
    "ml.c5n.4xlarge",
    "ml.c5n.9xlarge",
    "ml.c5n.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.2xlarge",
    "ml.g5.48xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.p4d.24xlarge",
    "ml.trn1.2xlarge",
    "ml.trn1.32xlarge",
]
TrainingJobCompletedOrStoppedWaiterName = Literal["training_job_completed_or_stopped"]
TrainingJobEarlyStoppingTypeType = Literal["Auto", "Off"]
TrainingJobSortByOptionsType = Literal[
    "CreationTime", "FinalObjectiveMetricValue", "Name", "Status"
]
TrainingJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TransformInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
]
TransformJobCompletedOrStoppedWaiterName = Literal["transform_job_completed_or_stopped"]
TransformJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TrialComponentPrimaryStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
UserProfileSortKeyType = Literal["CreationTime", "LastModifiedTime"]
UserProfileStatusType = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
VariantPropertyTypeType = Literal["DataCaptureConfig", "DesiredInstanceCount", "DesiredWeight"]
VariantStatusType = Literal["ActivatingTraffic", "Baking", "Creating", "Deleting", "Updating"]
VendorGuidanceType = Literal["ARCHIVED", "NOT_PROVIDED", "STABLE", "TO_BE_ARCHIVED"]
WarmPoolResourceStatusType = Literal["Available", "InUse", "Reused", "Terminated"]
WorkforceStatusType = Literal["Active", "Deleting", "Failed", "Initializing", "Updating"]
SageMakerServiceName = Literal["sagemaker"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "arc-zonal-shift",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "backup",
    "backup-gateway",
    "backupstorage",
    "batch",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codedeploy",
    "codeguru-reviewer",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controltower",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "dax",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "fsx",
    "gamelift",
    "gamesparks",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector2",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot-roborunner",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie",
    "macie2",
    "managedblockchain",
    "marketplace-catalog",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "network-firewall",
    "networkmanager",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "outposts",
    "panorama",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "textract",
    "timestream-query",
    "timestream-write",
    "transcribe",
    "transfer",
    "translate",
    "voice-id",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "list_actions",
    "list_algorithms",
    "list_aliases",
    "list_app_image_configs",
    "list_apps",
    "list_artifacts",
    "list_associations",
    "list_auto_ml_jobs",
    "list_candidates_for_auto_ml_job",
    "list_code_repositories",
    "list_compilation_jobs",
    "list_contexts",
    "list_data_quality_job_definitions",
    "list_device_fleets",
    "list_devices",
    "list_domains",
    "list_edge_deployment_plans",
    "list_edge_packaging_jobs",
    "list_endpoint_configs",
    "list_endpoints",
    "list_experiments",
    "list_feature_groups",
    "list_flow_definitions",
    "list_human_task_uis",
    "list_hyper_parameter_tuning_jobs",
    "list_image_versions",
    "list_images",
    "list_inference_experiments",
    "list_inference_recommendations_job_steps",
    "list_inference_recommendations_jobs",
    "list_labeling_jobs",
    "list_labeling_jobs_for_workteam",
    "list_lineage_groups",
    "list_model_bias_job_definitions",
    "list_model_card_export_jobs",
    "list_model_card_versions",
    "list_model_cards",
    "list_model_explainability_job_definitions",
    "list_model_metadata",
    "list_model_package_groups",
    "list_model_packages",
    "list_model_quality_job_definitions",
    "list_models",
    "list_monitoring_alert_history",
    "list_monitoring_alerts",
    "list_monitoring_executions",
    "list_monitoring_schedules",
    "list_notebook_instance_lifecycle_configs",
    "list_notebook_instances",
    "list_pipeline_execution_steps",
    "list_pipeline_executions",
    "list_pipeline_parameters_for_execution",
    "list_pipelines",
    "list_processing_jobs",
    "list_spaces",
    "list_stage_devices",
    "list_studio_lifecycle_configs",
    "list_subscribed_workteams",
    "list_tags",
    "list_training_jobs",
    "list_training_jobs_for_hyper_parameter_tuning_job",
    "list_transform_jobs",
    "list_trial_components",
    "list_trials",
    "list_user_profiles",
    "list_workforces",
    "list_workteams",
    "search",
]
WaiterName = Literal[
    "endpoint_deleted",
    "endpoint_in_service",
    "image_created",
    "image_deleted",
    "image_updated",
    "image_version_created",
    "image_version_deleted",
    "notebook_instance_deleted",
    "notebook_instance_in_service",
    "notebook_instance_stopped",
    "processing_job_completed_or_stopped",
    "training_job_completed_or_stopped",
    "transform_job_completed_or_stopped",
]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
