from __future__ import annotations
_C='pod_version'
_B='Version'
_A='pod_name'
import time
from typing import Dict,Final,List,Optional
from localstack_ext.bootstrap.pods.api_types import BackendStateMutatorDescriptor,BackendStateMutatorDescriptorListType,GetStatusResponse,GetStatusVerboseResponse,MergeStrategy,PodMeta,ServiceSources,ServiceSourcesListType
class MergeStrategyPretty(str):
	OVERWRITE='overwrite';MERGE='merge';DEEP='deep-merge';UNKNOWN='unknown';_FORMAL_BINDINGS={MergeStrategy.MERGE:MERGE,MergeStrategy.OVERWRITE:OVERWRITE,MergeStrategy.DEEP:DEEP};_PRETTY_BINDINGS={B:A for(A,B)in _FORMAL_BINDINGS.items()}
	@classmethod
	def from_merge_strategy(A,merge_strategy):return A(A._FORMAL_BINDINGS.get(merge_strategy,A.UNKNOWN))
	@staticmethod
	def to_merge_strategy(string):return MergeStrategyPretty._PRETTY_BINDINGS.get(string,None)
	@staticmethod
	def help_message(strategy_demeanor='Inject strategy'):return f"{strategy_demeanor} ({MergeStrategyPretty.MERGE}, {MergeStrategyPretty.OVERWRITE}, {MergeStrategyPretty.DEEP})."
def _normalise_merge_strategy_label(merge_strategy):return MergeStrategyPretty.from_merge_strategy(merge_strategy)
def _normalise_status_response_pod_meta(pod_meta):B=pod_meta;A=dict();A['Pod']=B[_A];A[_B]=B[_C];return A
def _normalise_status_response_service_source(service_source):B=service_source;A=dict();A['Service']=B['service'];A['From Cloud Pods']=[_normalise_status_response_pod_meta(A)for A in B['sources']];return A
def _normalise_status_response_service_sources(service_sources):A=list(map(_normalise_status_response_service_source,service_sources));return A
def _normalise_status_response(status_response):B=status_response;A=dict();C=B['service_sources'];A['Active CloudPods']=_normalise_status_response_service_sources(C);D=B['loaded_services'];A['All Active Services']=D;return A
def _normalise_status_response_verbose_modifier_descriptor(mod_des):
	F='merge_strategy';E='epoch_ms';C=mod_des;G=dict({'operation':'Operation',E:'When',_A:'CloudPod',_C:_B,'services':'Services','message':'Message',F:'Strategy','local':'Local','remote':'Remote'});D=dict()
	for (B,H) in G.items():
		if B in C:
			A=C[B]
			if B==E:I,J=divmod(A,1000);A='{}.{:03d}'.format(time.strftime('%d.%m.%Y %H:%M:%S %z',time.gmtime(I)),J)
			elif B==F:A=_normalise_merge_strategy_label(A)
			D[H]=A
	return D
def _normalise_status_response_verbose_modifier_descriptors(mod_des_list):A=list(map(_normalise_status_response_verbose_modifier_descriptor,mod_des_list));return A
def _normalise_status_response_verbose(status_response):A=status_response;B=_normalise_status_response(A);C=A['backend_state_mutator_descriptors'];B['CloudPods Events']=_normalise_status_response_verbose_modifier_descriptors(C);return B