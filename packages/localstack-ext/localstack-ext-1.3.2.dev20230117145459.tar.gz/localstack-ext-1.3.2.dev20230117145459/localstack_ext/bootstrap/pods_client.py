_I='git://'
_H='merge_strategy'
_G='pod_version'
_F='services'
_E='api_states'
_D='pod_name'
_C=False
_B=True
_A=None
import io,json,logging,os,re,zipfile
from abc import ABCMeta,abstractmethod
from collections import defaultdict
from enum import Enum
from pathlib import Path
from shutil import make_archive
from typing import Callable,Dict,List,NamedTuple,Optional,Set,Union
from urllib.parse import urlparse
import requests
from localstack import config
from localstack.utils.files import cp_r,disk_usage,load_file,new_tmp_dir,new_tmp_file,rm_rf,save_file
from localstack.utils.http import download,safe_requests
from localstack.utils.strings import to_str
from localstack.utils.sync import retry
from localstack_ext.bootstrap.licensing import get_auth_headers
from localstack_ext.bootstrap.pods.api_types import DEFAULT_MERGE_STRATEGY,GetStatusResponse,GetStatusVerboseResponse,MergeStrategy,NotifyOperationType,PodMeta,StateMergeRequest,StateResetRequest,StatusGetRequest,StatusNotifyEventRequest
from localstack_ext.bootstrap.pods.client_api import CloudPodsClientApi
from localstack_ext.bootstrap.pods.models import Serialization,Version
from localstack_ext.bootstrap.pods.remote import CloudPodsRemote,CloudPodsRemoteGithub,CloudPodsRemotePlatform
from localstack_ext.bootstrap.pods.service_state.service_state import ServiceState
from localstack_ext.bootstrap.pods.utils.adapters import ServiceStateMarshaller
from localstack_ext.bootstrap.pods.utils.common import PodsConfigContext
from localstack_ext.bootstrap.pods.utils.metamodel_utils import CommitMetamodelUtils
from localstack_ext.bootstrap.pods.utils.persistence import marshall_object
from localstack_ext.bootstrap.state_utils import DYNAMODB_DIR,KINESIS_DIR
from localstack_ext.constants import API_PATH_PODS,API_STATES_DIR
LOG=logging.getLogger(__name__)
PERSISTED_FOLDERS=[API_STATES_DIR,DYNAMODB_DIR,KINESIS_DIR]
POD_INJECT_CLI_TIMEOUT=7
REGEX_POD_NAME_GITHUB='^[^/]+/[^/]+(/[^/]+)?$'
class PodInfo:
	def __init__(A,name=_A,pod_size=0):A.name=name;A.pod_size=pod_size;A.pod_size_compressed=0;A.persisted_resource_names=[]
class PodLocation(Enum):REMOTE='remote';LOCAL='local'
def get_state_zip_from_instance(get_content=_C,services=_A):
	B=services;C=f"{get_pods_endpoint()}/state";E=','.join(B)if B else'';A=requests.get(C,params={_F:E})
	if A.status_code>=400:raise Exception(f"Unable to get local pod state via management API {C} (code {A.status_code}): {A.content}")
	if get_content:return A.content
	D=f"{new_tmp_file()}.zip";save_file(D,A.content);return D
class CloudPodsManager(metaclass=ABCMeta):
	def __init__(A,pod_name):B=pod_name;A.pod_name=B;C=PodsConfigContext(pod_name=B);A.pods_api=CloudPodsClientApi(C)
	@abstractmethod
	def init(self):...
	@abstractmethod
	def delete(self,remote):...
	@abstractmethod
	def push(self,comment=_A,services=_A):...
	@abstractmethod
	def push_overwrite(self,version,comment=_A,services=_A):...
	@abstractmethod
	def pull(self,inject=_B,merge_strategy=_A):...
	@abstractmethod
	def commit(self,message,services=_A):...
	@abstractmethod
	def inject(self,version,merge_strategy=_A):...
	@abstractmethod
	def get_version_summaries(self):...
	@abstractmethod
	def version_metamodel(self,version):...
	@abstractmethod
	def set_version(self,version,inject_version_state,reset_state,commit_before):...
	@abstractmethod
	def list_version_commits(self,version):...
	@abstractmethod
	def get_commit_diff(self,version,commit):...
	@abstractmethod
	def register_remote(self,ci_pod=_A):...
	@abstractmethod
	def rename_pod(self,current_pod_name,new_pod_name):...
	@abstractmethod
	def list_pods(self):...
	@staticmethod
	def restart_container():
		LOG.info('Restarting LocalStack instance with updated persistence state - this may take some time ...');B={'action':'restart'};A=f"{config.get_edge_url()}/_localstack/health"
		try:requests.post(A,data=json.dumps(B))
		except requests.exceptions.ConnectionError:pass
		def C():LOG.info('Waiting for LocalStack instance to be fully initialized ...');B=requests.get(A);C=json.loads(to_str(B.content));D=[A for(B,A)in C[_F].items()];assert set(D)=={'running'}
		retry(C,sleep=3,retries=10)
	def get_pod_info(C,pod_data_dir=_A):
		A=pod_data_dir;B=PodInfo(C.pod_name)
		if A:B.pod_size=disk_usage(A);B.persisted_resource_names=get_persisted_resource_names(A)
		return B
class CloudPodsVersionManager(CloudPodsManager):
	def __init__(A,pod_name):super().__init__(pod_name)
	@staticmethod
	def parse_pod_name_from_qualifying_name(qualifying_name):return qualifying_name.split(PODS_NAMESPACE_DELIM,1)[1]
	def _add_state_to_cloud_pods_store(A,extract_assets=_C,services=_A):
		if not A.pods_api.config_context.is_initialized():LOG.debug('No Cloud Pod instance detected in the local context - unable to add state');return
		E=get_state_zip_from_instance(get_content=_B,services=services);C=ServiceStateMarshaller.unmarshall(E,raw_bytes=_B)
		for (B,F) in C.state.items():
			for (G,H) in F.backends.items():A.pods_api.create_state_file_from_fs(file_name=G,service=B.service,region=B.region,root=_E,account_id=B.account_id,serialization=Serialization.MAIN,object=H)
		if extract_assets:
			for (I,J) in C.assets.items():
				for (D,K) in J.items():A.pods_api.create_state_file_from_fs(rel_path=D,file_name=os.path.basename(D),service=I,region='NA',root='assets',account_id='NA',serialization=Serialization.MAIN,object=K)
		L=CommitMetamodelUtils.get_metamodel_from_instance();A.pods_api.add_metamodel_to_current_revision(L)
	def init(A):A.pods_api.init(pod_name=A.pod_name)
	def delete(A,remote):
		C=A.pods_api.config_context.cloud_pods_root_dir;B=os.path.join(C,A.pod_name)
		if os.path.isdir(B):rm_rf(B);return _B
		if remote:return A.remote.delete_pod(A.pod_name)
		return _C
	def push(A,comment=_A,services=_A):
		D=comment;A.pods_api.set_pod_context(A.pod_name);A._add_state_to_cloud_pods_store(extract_assets=_B,services=services);B:bool;C=A.pods_api.get_head().version_number
		if A.pods_api.is_remotely_managed():
			E=A.remote.get_max_version(pod_name=A.pod_name);B=C<E
			if B:A.pull()
			A.pods_api.push(comment=D);A.remote.push_pod(A.pod_name,version=C)
		else:F=A.pods_api.get_max_version_no();B=C<F;G=A.pods_api.push(comment=D);LOG.debug("Created new version %s for pod '%s'",G.version_number,A.pod_name)
		return PodInfo()
	def push_overwrite(A,version,comment=_A,services=_A):
		B=version;A.pods_api.set_pod_context(pod_name=A.pod_name)
		if B>A.pods_api.get_max_version_no():LOG.warning(f"Version {B} does not exist");return _C
		A._add_state_to_cloud_pods_store(services=services);A.pods_api.push_overwrite(version=B,comment=comment)
		if A.pods_api.is_remotely_managed():A.remote.push_pod(A.pod_name,version=B,overwrite=_B)
		return _B
	def pull(A,inject=_B,merge_strategy=_A):
		C=merge_strategy
		if C is _A:C=DEFAULT_MERGE_STRATEGY
		D=0;B=A.pod_name
		if B in A.pods_api.list_locally_available_pods():A.pods_api.set_pod_context(B);D=A.pods_api.get_max_version_no()
		else:A.pods_api.init(pod_name=B)
		E=A.remote.get_max_version(B)
		if not E:return _C
		if E>D:F=list(range(D+1,E+1));A.remote.pull_versions(pod_name=B,required_versions=F)
		else:LOG.info('No new version available remotely')
		if inject:LOG.info('Injecting the cloud pod state into the running instance');return A.inject(version=-1,merge_strategy=C)
		return _B
	def commit(A,message=_A,services=_A):C=services;B=message;A.pods_api.set_pod_context(A.pod_name);A._add_state_to_cloud_pods_store(services=C);D=A.pods_api.commit(message=B);notify_status_event(StatusNotifyEventRequest(operation=NotifyOperationType.COMMIT,pod_meta=PodMeta(pod_name=A.pod_name,pod_version=A.pods_api.get_max_version_no()),services=C or _A,message=B));LOG.debug('Completed revision: %s',D.hash_ref)
	@staticmethod
	def deploy_pod_into_instance(pod_name,pod_version,pod_path,merge_strategy):
		A=pod_path
		if not A:raise Exception(f"Unable to restore pod state via local pods management API: Pod Path {A} not valid")
		D=_C
		if os.path.isdir(A):
			B=new_tmp_dir()
			for E in PERSISTED_FOLDERS:
				F=os.path.join(A,E)
				if not os.path.exists(F):continue
				H=os.path.join(B,E);cp_r(F,H,rm_dest_on_conflict=_B)
			make_archive(f"{B}.zip",'zip',root_dir=B);rm_rf(B);D=_B
		try:
			I=load_file(A,mode='rb');G=get_pods_endpoint();J={_D:pod_name,_G:pod_version,_H:merge_strategy};C=requests.post(G,data=I,params=J,timeout=POD_INJECT_CLI_TIMEOUT)
			if C.status_code>=400:raise Exception(f"Unable to restore pod state via local pods management API {G} (code {C.status_code}): {C.content}")
		except requests.exceptions.ReadTimeout:LOG.debug('Returning from cloud pod inject operation - continues to run in the background...')
		finally:
			if D:rm_rf(A)
	def inject(A,version=-1,merge_strategy=_A):
		F='Unable to find a local version of pod %s';D=merge_strategy;C=version
		if D is _A:D=MergeStrategy.MERGE
		if not A.pods_api.config_context.pod_exists_locally(A.pod_name):raise Exception(F,A.pod_name)
		A.pods_api.set_pod_context(A.pod_name)
		if C==-1:C=A.pods_api.get_max_version_no(require_state_archive=_B)
		B=A.pods_api.config_context.get_version_state_archive(C);E=_C
		try:
			if not B and A.pods_api.is_remotely_managed():raise Exception(F,A.pod_name)
			if not B and C<=Version.DEFAULT_INITIAL_VERSION_NUMBER:B=new_tmp_file();G=A.pods_api.get_state_archive_from_state_files();save_file(B,G);E=_B
			B=merge_local_state_with(merge_strategy=D,state_archive_path=B)
			if not B:raise Exception(f"Unable to find state archive for cloud pod '{A.pod_name}' version {C}")
			A.deploy_pod_into_instance(pod_name=A.pods_api.config_context.pod_name,pod_version=C,pod_path=B,merge_strategy=D);return _B
		except Exception as H:LOG.debug('An exception occurred while trying to load Cloud Pod %s: "%s"',A.pod_name,H);return _C
		finally:
			if E:rm_rf(B)
	def get_version_summaries(A):A.pods_api.set_pod_context(A.pod_name);B=A.pods_api.get_version_summaries();return B
	def version_metamodel(A,version):
		B=version;A.pods_api.set_pod_context(A.pod_name)
		if B==-1:B=A.pods_api.get_max_version_no(require_state_archive=_B)
		D=A.pods_api.get_version_by_number(B);E=D.get_latest_revision(with_commit=_B);C=A.pods_api.commit_metamodel_utils.reconstruct_metamodel(version=D,revision=E)
		if not C and A.pods_api.is_remotely_managed():A.remote.pull_versions(A.pod_name,required_versions=[B]);C=A.pods_api.commit_metamodel_utils.create_metamodel_from_state_files(version=B)
		return C
	def set_version(A,version,inject_version_state,reset_state,commit_before):
		B=version;A.pods_api.set_pod_context(A.pod_name);C=A.pods_api.set_active_version(version_no=B,commit_before=commit_before)
		if not C:LOG.warning(f"Could not find version {B}")
		if inject_version_state:A.inject(version=B,merge_strategy=MergeStrategy.OVERWRITE)
		return C
	def list_version_commits(A,version):A.pods_api.set_pod_context(A.pod_name);B=A.pods_api.list_version_commits(version_no=version);C=[A.get_summary()for A in B];return C
	def get_commit_diff(A,version,commit):A.pods_api.set_pod_context(A.pod_name);B=A.pods_api.commit_metamodel_utils.get_commit_diff(version_no=version,commit_no=commit);return B
	def rename_pod(A,current_pod_name,new_pod_name):
		C=current_pod_name;B=new_pod_name;A.pods_api.set_pod_context(C)
		if B in A.pods_api.list_locally_available_pods():LOG.warning(f"{B} already exists locally");return _C
		if A.pods_api.is_remotely_managed():
			D=A.remote.rename_pod(C,B)
			if not D:return D
		A.pods_api.rename_pod(B);return _B
	def register_remote(A,ci_pod=_A):return A.remote.register_remote(A.pod_name,ci_pod=ci_pod)
	def list_pods(B):
		D={A:{PodLocation.LOCAL.value}for A in B.pods_api.list_locally_available_pods()};C=D or defaultdict(set);E=B.remote.list_pods()
		for A in E or[]:F=A.get(_D)if isinstance(A,dict)else A;C.setdefault(F,set()).add(PodLocation.REMOTE.value)
		return C
	@property
	def remote(self):
		A=self;B=A.pod_name or''
		if re.match(REGEX_POD_NAME_GITHUB,B):return CloudPodsRemoteGithub(A.pods_api.config_context)
		return CloudPodsRemotePlatform(A.pods_api.config_context)
class PodConfigManagerMeta(type):
	def __getattr__(C,attr):
		def A(*D,**E):
			A=_A
			for F in C.CHAIN:
				try:
					B=getattr(F,attr)(*(D),**E)
					if B:
						if not A:A=B
						elif isinstance(B,list)and isinstance(A,list):A.extend(B)
				except Exception:
					if LOG.isEnabledFor(logging.DEBUG):LOG.exception('error during PodConfigManager call chain')
			if A is not _A:return A
			raise Exception(f'Unable to run operation "{attr}" for local or remote configuration')
		return A
class PodConfigManager(metaclass=PodConfigManagerMeta):
	CHAIN=[]
	@classmethod
	def pod_config(D,pod_name):
		A=pod_name;C=PodConfigManager.list_pods();B=[B for B in C if B[_D]==A]
		if not B:raise Exception(f'Unable to find config for pod named "{A}"')
		return B[0]
def get_pods_manager(pods_name):return CloudPodsVersionManager(pod_name=pods_name)
def init_cloudpods(pod_name):A=get_pods_manager(pods_name=pod_name);A.init()
def delete_pod(pod_name):A=get_pods_manager(pods_name=pod_name);B=A.delete(remote=_B);return B
def register_remote(pod_name,ci_pod=_A):A=get_pods_manager(pods_name=pod_name);B=A.register_remote(ci_pod=ci_pod);return B
def rename_pod(current_pod_name,new_pod_name):A=new_pod_name;B=get_pods_manager(pods_name=A);C=B.rename_pod(current_pod_name=current_pod_name,new_pod_name=A);return C
def list_pods():A=get_pods_manager(pods_name='');B=A.list_pods();return B
def list_public_pods():
	B=CloudPodsRemotePlatform.create_platform_url('public');C=get_auth_headers();A=safe_requests.get(B,headers=C)
	if not A.ok:raise Exception(to_str(A.content))
	D=json.loads(A.content);return[A[_D]for A in D]
def set_public(pod_name,public):
	A=pod_name;B=get_pods_manager(A);B.pods_api.set_pod_context(A)
	if not B.pods_api.is_remotely_managed():return _C
	C=CloudPodsRemotePlatform.create_platform_url(f"{A}");D=get_auth_headers();E=safe_requests.patch(C,headers=D,data=json.dumps({'is_public':public}));return E.ok
def commit_state(pod_name,message=_A,services=_A,**C):
	B=pod_name;A=get_pods_manager(pods_name=B)
	if not A.pods_api.config_context.is_initialized():A.init()
	A.pods_api.set_pod_context(pod_name=B);A.commit(message=message,services=services)
def inject_state(pod_name,version,merge_strategy=_A,**C):A=get_pods_manager(pods_name=pod_name);B=A.inject(version=version,merge_strategy=merge_strategy);return B
def get_version_summaries(pod_name):B=get_pods_manager(pods_name=pod_name);A=B.get_version_summaries();A=A[::-1];return A
def get_version_metamodel(version,pod_name,**C):A=get_pods_manager(pods_name=pod_name);B=A.version_metamodel(version=version);return B
def set_version(version,inject_version_state,reset_state,commit_before,pod_name,**C):A=get_pods_manager(pods_name=pod_name);B=A.set_version(version=version,inject_version_state=inject_version_state,reset_state=reset_state,commit_before=commit_before);return B
def list_version_commits(version,pod_name):A=get_pods_manager(pods_name=pod_name);B=A.list_version_commits(version=version);return B
def get_commit_diff(version,commit,pod_name):A=get_pods_manager(pods_name=pod_name);B=A.get_commit_diff(version=version,commit=commit);return B
def push_overwrite(version,pod_name,comment,services=_A):D=services;C=comment;B=pod_name;A=version;E=get_pods_manager(pods_name=B);E.push_overwrite(version=A,comment=C,services=D);notify_status_event(StatusNotifyEventRequest(operation=NotifyOperationType.PUSH,pod_meta=PodMeta(pod_name=B,pod_version=A),services=D or _A,message=C))
def push_state(pod_name,comment=_A,services=_A,local=_C):
	D=comment;C=pod_name;B=services
	if B is _A:B=[]
	A=get_pods_manager(pods_name=C)
	if not A.pods_api.config_context.is_initialized():A.init()
	A.pods_api.set_pod_context(pod_name=C);A.push(comment=D,services=B);notify_status_event(StatusNotifyEventRequest(operation=NotifyOperationType.PUSH,pod_meta=PodMeta(pod_name=C,pod_version=A.pods_api.get_max_version_no()-1),services=B or _A,message=D))
	if local:return _B
	return A.register_remote()
def get_pods_endpoint():A=config.get_edge_url();return f"{A}{API_PATH_PODS}"
def pull_state(pod_name,merge_strategy=_A):
	A=pod_name
	if not A:raise Exception('Need to specify a pod name')
	B=get_pods_manager(pods_name=A);return B.pull(inject=_B,merge_strategy=merge_strategy)
def get_status(verbose):A=f"{get_pods_endpoint()}/status";B=StatusGetRequest(verbose=verbose);C=requests.get(A,data=marshall_object(B));D=json.loads(C.content);return D
def export_pod(target):
	D=get_state_zip_from_instance(get_content=_B);A=urlparse(target);B=os.path.abspath(os.path.join(A.netloc,A.path));C=Path(B).parent.absolute()
	if not os.path.exists(C):raise Exception(f"{C} is not a valid path")
	save_file(file=B,content=D);return _B
def import_pod(source,merge_strategy):A=source;B=get_protocol_access(A);C=B(A);return inject_pod_endpoint(content=C,merge_strategy=merge_strategy)
def inject_pod_endpoint(content,pod_name='community_pod',pod_version=1,merge_strategy=DEFAULT_MERGE_STRATEGY):A=get_pods_endpoint();B={_D:pod_name,_G:str(pod_version),_H:merge_strategy};C=requests.post(A,data=content,params=B,timeout=POD_INJECT_CLI_TIMEOUT);return C.ok
def get_git_base_url(user,repo):return f"https://raw.githubusercontent.com/{user}/{repo}/main"
def notify_status_event(notify_request):A=f"{get_pods_endpoint()}/status/notify";requests.post(A,data=marshall_object(notify_request))
def reset_local_state(reset_persistence=_C,services=_A):
	B=f"{get_pods_endpoint()}/state/reset";C=StateResetRequest(persistence=reset_persistence,services=services);LOG.debug(f"Sending request to reset the service states in local instance with params {json.dumps(C)}.");D=marshall_object(C);A=requests.delete(B,data=D)
	if A.status_code>=400:raise Exception(f"Unable to reset service state via local management API {B} (code {A.status_code}): {A.content}")
class States(NamedTuple):state:Optional[ServiceState];inject:ServiceState;ancestor:Optional[ServiceState]
def _merge_states_into_zip(states):
	A=io.BytesIO()
	with zipfile.ZipFile(A,'a')as C:
		for (D,B) in states._asdict().items():
			if not B:continue
			C.writestr(f"{D}.zip",ServiceStateMarshaller.marshall(B))
	A.seek(0);return A.getvalue()
def merge_states_via_endpoint(merge_strategy,injecting,state=_A,ancestor=_A):
	C=_merge_states_into_zip(States(state,injecting,ancestor));D=StateMergeRequest(merge_strategy=merge_strategy,data=C);B=f"{get_pods_endpoint()}/merge";E=marshall_object(D);A=requests.post(url=B,data=E)
	if A.status_code>=400:raise Exception(f"Unable to merge state via merge API {B} (code {A.status_code})")
	return A.content
def merge_local_state_with(merge_strategy,state_archive_path):
	B=state_archive_path;A=merge_strategy
	if A==MergeStrategy.OVERWRITE:reset_local_state(reset_persistence=_B);return B
	D=ServiceStateMarshaller.unmarshall_zip_archive(B);E=merge_states_via_endpoint(merge_strategy=A,injecting=D);C=new_tmp_file();ServiceStateMarshaller.marshall_zip_archive(C,ServiceStateMarshaller.unmarshall(E,raw_bytes=_B));return C
def is_initialized(pod_name):A=get_pods_manager(pods_name=pod_name);return A.pods_api.config_context.is_initialized()
def get_protocol_access(url):
	A=url
	if A.startswith('file://'):return get_zip_content_from_file
	elif A.startswith(('https://','http://')):return get_zip_content_from_http
	elif A.startswith(_I):return get_zip_content_from_git
	raise Exception('Protocol not valid: %s',A)
def get_zip_content_from_file(url):
	B=url;B=urlparse(B);A=os.path.abspath(os.path.join(B.netloc,B.path))
	if not os.path.isfile(A):raise Exception(f"Path {A} is not a file")
	if not os.path.exists(A):raise Exception(f"Path {A} does not exist")
	return load_file(A,mode='rb')
def get_zip_content_from_http(url):
	A=requests.get(url)
	if not A.ok:raise Exception('Unable to fetch Cloud Pod from URL %s: %s %s',url,A.status_code,A.content)
	return A.content
def get_zip_content_from_git(url):
	D=url[len(_I):];A=D.split('/');E,F,G=A[0],A[1],A[2];H=f"{get_git_base_url(E,F)}";B=f"{H}/{G}";C=new_tmp_file()
	try:download(B,C)
	except Exception as I:LOG.error('Failed to download Cloud Pod from url %s: %s',B,I)
	return load_file(C,mode='rb')
def get_persisted_resource_names(data_dir):
	D=data_dir;B=[]
	with os.scandir(D)as C:
		for A in C:
			if A.is_dir()and A.name!=_E:B.append(A.name)
	with os.scandir(os.path.join(D,_E))as C:
		for A in C:
			if A.is_dir()and len(os.listdir(A.path))>0:B.append(A.name)
	LOG.debug(f"Detected state files for the following APIs: {B}");return B
PODS_NAMESPACE_DELIM='-'