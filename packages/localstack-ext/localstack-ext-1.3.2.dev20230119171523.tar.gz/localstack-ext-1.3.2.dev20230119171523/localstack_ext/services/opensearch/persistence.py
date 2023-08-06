_A='opensearch'
import logging
from urllib.parse import urlparse
from localstack import config
from localstack.aws.accounts import get_aws_account_id
from localstack.services.opensearch.cluster_manager import DomainKey
from localstack.services.opensearch.models import opensearch_stores
from localstack.services.opensearch.provider import create_cluster
from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
LOG=logging.getLogger(__name__)
OPENSEARCH_ASSETS_ROOT=_A
def restore_backend_state(*K):
	E='Endpoint'
	for (L,F) in opensearch_stores.items():
		for (B,G) in F.items():
			for (C,A) in G.opensearch_domains.items():
				LOG.info(f"Restoring domain {C} in region {B}.")
				try:
					D=None
					if config.OPENSEARCH_ENDPOINT_STRATEGY=='port':
						if E in A:D=urlparse(f"http://{A[E]}").port
					H=DomainKey(C,B,get_aws_account_id());I=A.get('EngineVersion');J=A.get('DomainEndpointOptions',{});create_cluster(H,I,J,D)
				except Exception:LOG.exception(f"Could not restore domain {C} in region {B}.");pass
class OpenSearchPersistenceLifeCycle(StateLifecyclePlugin):
	name=_A;service=_A
	def inject_assets(A,pod_asset_directory):super().inject_assets(pod_asset_directory);restore_backend_state()