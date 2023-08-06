import io,logging
from typing import List,Optional
from zipfile import ZipFile
from localstack.utils.files import new_tmp_dir,rm_rf
from localstack_ext.bootstrap.pods.api_types import StateInjectRequest
from localstack_ext.bootstrap.pods.server.persistence import unmarshall_backend
from localstack_ext.bootstrap.pods.server.states import ServiceStateManager
from localstack_ext.bootstrap.pods.service_state.service_state import ServiceState
from localstack_ext.bootstrap.pods.utils.adapters import ServiceStateMarshaller
from localstack_ext.bootstrap.state_utils import cleanse_keep_files
LOG=logging.getLogger()
def handle_pod_state_injection(inject_request):
	from localstack.services.plugins import SERVICE_PLUGINS as F;B=inject_request['data'];C=ServiceStateMarshaller.unmarshall(B,unmarshall_function=unmarshall_backend);D=C.get_services();LOG.debug('Injecting state for the following services into the current instance: %s',','.join(D));E=_extract_pod_zip(pod_data=B)
	for A in D:
		try:F.get_service_container(A);G=ServiceStateManager(service=A);G.inject_service_state(pod_state=C,pod_tmp_dir=E)
		except Exception as H:LOG.debug('Unable to inject pod state for service %s: %s',A,H)
	rm_rf(E);return{}
def _extract_pod_zip(pod_data):
	A=new_tmp_dir()
	try:
		with ZipFile(io.BytesIO(pod_data),'r')as B:B.extractall(A);cleanse_keep_files(A)
	except Exception as C:LOG.exception('Failed to extract cloud pods zip data from payload: %s',C);rm_rf(A);return
	return A