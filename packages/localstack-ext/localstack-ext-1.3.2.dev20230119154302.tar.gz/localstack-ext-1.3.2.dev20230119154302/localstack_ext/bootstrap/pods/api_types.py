from typing import Final,List,Optional,TypedDict
class MergeStrategy(str):OVERWRITE='OVERWRITE';MERGE='MERGE';DEEP='DEEP'
DEFAULT_MERGE_STRATEGY=MergeStrategy(MergeStrategy.MERGE)
class PodMeta(TypedDict):pod_name:str;pod_version:Optional[int]
class StateGetRequest(TypedDict):services:Optional[List[str]]
class StateResetRequest(TypedDict):services:Optional[List[str]];persistence:bool
class StateInjectRequest(TypedDict):pod_meta:PodMeta;merge_strategy:MergeStrategy;data:bytes
class StateMergeRequest(TypedDict):merge_strategy:MergeStrategy;data:bytes
class StatusGetRequest(TypedDict):verbose:bool
class OperationType(str):INJECT='INJECT';RESET='RESET'
class NotifyOperationType(OperationType):COMMIT='COMMIT';PUSH='PUSH'
class BackendStateMutatorDescriptor(TypedDict):operation:OperationType;epoch_ms:int;pod_name:Optional[str];pod_version:Optional[int];services:Optional[List[str]];message:Optional[str];local:Optional[bool];remote:Optional[bool];merge_strategy:Optional[MergeStrategy]
SourceListType=List[PodMeta]
class ServiceSources(TypedDict):service:str;sources:SourceListType
ServiceSourcesListType=List[ServiceSources]
class GetStatusResponse(TypedDict):service_sources:ServiceSourcesListType;loaded_services:List[str]
BackendStateMutatorDescriptorListType=List[BackendStateMutatorDescriptor]
class GetStatusVerboseResponse(GetStatusResponse):backend_state_mutator_descriptors:BackendStateMutatorDescriptorListType
class StatusNotifyEventRequest(TypedDict):operation:NotifyOperationType;pod_meta:PodMeta;services:List[str];message:Optional[str]