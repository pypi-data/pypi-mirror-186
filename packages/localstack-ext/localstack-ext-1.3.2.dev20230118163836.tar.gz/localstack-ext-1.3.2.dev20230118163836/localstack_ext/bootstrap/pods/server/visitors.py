_A=None
import inspect,logging
from functools import singledispatchmethod
from typing import Any
from localstack.services.stores import AccountRegionBundle
from localstack.services.visitors import StateVisitor
from moto.core import BackendDict
from moto.core.base_backend import BaseBackend
from localstack_ext.bootstrap.pods.service_state.service_state import ServiceState
from localstack_ext.bootstrap.state_utils import get_object_dict
from localstack_ext.constants import MOTO_BACKEND_STATE_FILE,STORE_STATE_FILE
LOG=logging.getLogger(__name__)
class PodStateLoaderVisitor(StateVisitor):
	pod_state:ServiceState;service:str
	def __init__(A,pod_state,service):A.pod_state=pod_state;A.service=service
	@singledispatchmethod
	def visit(self,state_container):LOG.info('Cannot load state from Cloud pod into state container of type %s',type(state_container))
	def _iterate_pod_state(A):
		for (B,C) in A.pod_state.state.items():
			if B.service!=A.service:continue
			yield(B,C)
	@visit.register(AccountRegionBundle)
	def _(self,state_container):
		C=state_container
		for (A,D) in self._iterate_pod_state():
			try:
				B=D.backends.get(STORE_STATE_FILE)
				if B is _A:return
				C[A.account_id][A.region]=B;C[A.account_id]._global=B._global
			except Exception as E:LOG.debug('Error while visiting AccountRegionBundle: %s',E)
	@visit.register(BackendDict)
	def _(self,state_container):
		for (A,D) in self._iterate_pod_state():
			try:
				B=D.backends.get(MOTO_BACKEND_STATE_FILE)
				if B is _A:return
				E,F=A.account_id,A.region;C=get_object_dict(state_container[E][F]);G=get_object_dict(B);C.clear();C.update(G)
			except Exception as H:LOG.debug('Error while visiting BackendDict: %s',H)
	@visit.register(dict)
	def _(self,state_container):A=state_container;B=get_object_dict(A);C=get_object_dict(A);B.clear();B.update(C)
class ResetStateVisitor(StateVisitor):
	@singledispatchmethod
	def visit(self,state_container):LOG.info('Cannot reset state container of type %s',type(state_container))
	@visit.register(AccountRegionBundle)
	def _(self,state_container):state_container.reset()
	@visit.register(BackendDict)
	def _(self,state_container):
		A=state_container
		for (E,B) in A.items():
			for C in B.keys():
				try:reset_moto_backend_state(B,C)
				except Exception as D:LOG.warning('Failed to reset the state for BackendDict %s: %s',A,D)
	@visit.register(BaseBackend)
	def _(self,state_container):A=state_container;B=getattr(A,'region_name',getattr(A,'region',_A));A.__dict__={};A.__init__(*([B]if B else[]))
def reset_moto_backend_state(state_container,region_key):
	D=state_container;B=region_key;from moto.applicationautoscaling.models import ApplicationAutoscalingBackend as G;from moto.autoscaling.models import AutoScalingBackend as H;from moto.redshift.models import RedshiftBackend as I;A=D.get(B);E=getattr(A,'reset',_A)
	if E and callable(E):E();return A
	F=type(A);C=[B]if len(inspect.signature(F.__init__).parameters)>1 else[]
	if isinstance(A,G):C.append(A.ecs_backend)
	elif isinstance(A,I):C.insert(0,A.ec2_backend)
	elif isinstance(A,H):C=[A.ec2_backend,A.elb_backend,A.elbv2_backend]
	D[B]=F(*(C));return D[B]