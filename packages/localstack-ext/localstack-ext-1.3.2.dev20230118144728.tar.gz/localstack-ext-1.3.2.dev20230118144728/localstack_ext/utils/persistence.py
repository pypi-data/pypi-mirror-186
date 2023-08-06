_F='candidate_matcher'
_E='candidate_extractor'
_D='method'
_C='id_extractor'
_B=False
_A=None
import base64,inspect,logging,os,pickle,re,threading,time,types
from typing import Any,Iterator,Set,Tuple
import requests
from localstack import config
from localstack import config as localstack_config
from localstack.utils.files import load_file,mkdir,save_file
from localstack.utils.functions import empty_context_manager
from localstack.utils.patch import patch
from localstack.utils.persistence import is_persistence_enabled
from localstack.utils.strings import to_bytes,to_str
from localstack_ext import config as ext_config
from localstack_ext.constants import API_STATES_DIR
LOG=logging.getLogger(__name__)
CONTENT_MAPPINGS=[{'src':{'api':'sns',_D:'POST',_E:'.*Action=([^&]+).*',_F:'Subscribe',_C:'.*<SubscriptionArn>\\s*([^<]+)\\s*</SubscriptionArn>.*'},'tgt':{}}]
CONTENT_IDS={}
LOG=logging.getLogger(__name__)
class PersistenceTimer:
	DEFAULT_MIN_DELAY_SECS=30
	def __init__(A,delay_secs=0):A.last_persist_time=0;A.delay_secs=delay_secs or A.DEFAULT_MIN_DELAY_SECS
	def should_persist_now(A):
		def C():return ext_config.PERSIST_FLUSH_STRATEGY=='interval'
		if not C():return True
		B=time.time();D=B-A.last_persist_time
		if D<A.delay_secs:return _B
		A.last_persist_time=B;return True
def replace_extracted_ids(api,data,reverse=_B):
	A=data
	try:A=to_str(A or'');D=True
	except Exception:A=to_bytes(A or'');D=_B
	for (B,C) in CONTENT_IDS.items():
		if reverse:E=B;B=C;C=E
		if not D:B,C=to_bytes(B),to_bytes(C)
		A=A.replace(B,C)
	return A
def extract_id_mappings(command,received_response):
	F='\\1';B=command;I=B['a'];J=B['m'];E=_A;C=_A;D=_A
	for map in CONTENT_MAPPINGS:
		A=map['src']
		if A.get('api')not in[_A,I]or A.get(_D)not in[_A,J]:continue
		try:E=E or to_str(base64.b64decode(B.get('d')));C=C or to_str(base64.b64decode(B.get('rd')));D=D or to_str(received_response.content)
		except Exception:return
		K=re.sub(A[_E],F,E)
		if not re.match(K,A[_F]):return
		G=re.sub(A[_C],F,C);H=re.sub(A[_C],F,D)
		if G!=C and H!=D:CONTENT_IDS[G]=H
def update_persistence_health_info():
	B=f"{config.get_edge_url()}/_localstack/health";C={'features:persistence':'initialized'if is_persistence_enabled()else'disabled'};A=requests.put(B,json=C,verify=_B)
	if not A.ok:LOG.info('Unable to update /_localstack/health endpoint with persistence details: %s %s',A,A.content)
def load_backend_state(state_dir=_A,services=_A):
	C=services;A=state_dir;A=A or get_state_dir_root();mkdir(A)
	for (F,I,G) in os.walk(A):
		B=os.path.basename(F)
		if C and B not in C:continue
		for D in G:
			H=os.path.join(A,B,D);E=load_persisted_backend(H)
			if E is not _A:yield(D,B,E)
def persist_object(file_path,obj):from localstack_ext.bootstrap.pods.server.persistence import marshall_backend as A;save_file(file_path,A(obj))
def load_persisted_backend(state_file):
	A=state_file;from localstack_ext.persistence.utils import unmarshall_backend as B
	if not os.path.isfile(A):return
	try:C=load_file(A,mode='rb');D=B(C);return D
	except Exception as E:LOG.debug('Unable to read pickled persistence file %s: %s',A,E)
def should_persist_assets():return is_persistence_enabled()and ext_config.PERSIST_ALL
def persist_state(state_dir,service_name,state_file,state,rwlock=_A):
	A=rwlock;D=A and A.gen_wlock()or empty_context_manager()
	with D:
		B=os.path.join(state_dir,service_name);mkdir(B);C=os.path.join(B,state_file)
		try:persist_object(C,state)
		except Exception:
			if LOG.isEnabledFor(logging.INFO):LOG.exception('Unable to persist backend state to path %s',C)
def is_generator(o):return isinstance(o,types.GeneratorType)or inspect.isgeneratorfunction(o)
def is_thread(o):return isinstance(o,threading.Thread)
def is_serializable(o):return not is_generator(o)and not is_thread(o)
@patch(pickle._Pickler.save_dict)
def save_dict(fn,self,obj,*B,**C):
	A=obj
	if isinstance(A,dict):A={C:B for(C,B)in A.items()if is_serializable(B)}
	return fn(self,A,*(B),**C)
def get_state_dir_root():return os.path.join(localstack_config.dirs.data,API_STATES_DIR)
def get_state_dir_for_service(service_name):return os.path.join(get_state_dir_root(),service_name)