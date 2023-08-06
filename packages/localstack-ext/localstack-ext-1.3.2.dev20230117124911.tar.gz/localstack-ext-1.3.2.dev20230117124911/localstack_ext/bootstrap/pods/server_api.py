from typing import List
from localstack.http import route
from werkzeug import Request
from localstack_ext.constants import API_PATH_PODS
class CloudPodsPublicApi:
	@route(f"{API_PATH_PODS}",methods=['POST'])
	def pods(self,request):
		A=request;from localstack_ext.bootstrap.pods.api_types import PodMeta as B,StateInjectRequest as C;from localstack_ext.bootstrap.pods.server.inject import handle_pod_state_injection as D
		if A.method=='OPTIONS':return
		E=A.values.get('pod_name');F=A.values.get('pod_version');G=A.values.get('merge_strategy','merge');H=C(pod_meta=B(pod_name=E,pod_version=F),merge_strategy=G,data=A.get_data());return D(H)
	@route(f"{API_PATH_PODS}/state",methods=['GET'])
	def pods_state(self,request):from localstack_ext.bootstrap.pods.server.extract import handle_get_state_request_in_memory as B;A=request.values.get('services','');C=A.split(',')if A else None;return B(C)