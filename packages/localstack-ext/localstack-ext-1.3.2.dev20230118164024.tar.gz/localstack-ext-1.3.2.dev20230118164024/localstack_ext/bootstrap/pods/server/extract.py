from __future__ import annotations
import logging
from typing import List,Optional
from localstack.constants import APPLICATION_OCTET_STREAM
from localstack.http import Response
from localstack_ext.bootstrap.pods.server import persistence
from localstack_ext.bootstrap.pods.server.states import ServiceStateManager
from localstack_ext.bootstrap.pods.service_state.service_state import ServiceState
from localstack_ext.bootstrap.pods.utils.adapters import ServiceStateMarshaller
LOG=logging.getLogger(__name__)
def handle_get_state_request_in_memory(services=None):
	from localstack.services.plugins import SERVICE_PLUGINS as C;D=C.list_loaded_services();B=ServiceState()
	for A in services or D:
		E=C.get_service_container(A)
		if not E:LOG.debug("Can't get service container for service %s while calling handle_get_state_request_in_memory",A)
		try:F=ServiceStateManager(service=A);G=F.get_service_state();B.put_service_state(G)
		except Exception as H:LOG.debug('Unable to retrieve the state for service %s: %s - skipping',A,H)
	if B.is_empty():LOG.debug('Extracted state is empty')
	I=ServiceStateMarshaller.marshall(state=B,marshall_function=persistence.marshall_backend);J=Response(I,mimetype=APPLICATION_OCTET_STREAM);return J