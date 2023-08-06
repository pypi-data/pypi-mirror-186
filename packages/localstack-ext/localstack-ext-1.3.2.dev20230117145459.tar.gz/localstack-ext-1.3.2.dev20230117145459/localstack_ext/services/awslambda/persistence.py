_H='layers'
_G='S3Bucket'
_F='functions'
_E='_is_restoring_state'
_D='zip_dir'
_C=False
_B=None
_A='lambda'
import base64,glob,hashlib,logging,os,os.path
from typing import Dict,List,Optional,Tuple
from localstack import config
from localstack import config as localstack_config
from localstack.services.awslambda import lambda_api
from localstack.services.awslambda.event_source_listeners.event_source_listener import EventSourceListener
from localstack.services.awslambda.lambda_api import LAMBDA_ZIP_FILE_NAME
from localstack.services.awslambda.lambda_models import awslambda_stores
from localstack.services.awslambda.lambda_utils import get_lambda_extraction_dir,get_zip_bytes
from localstack.utils.aws.aws_models import LambdaFunction
from localstack.utils.files import cp_r,file_exists_not_empty,load_file,mkdir,rm_rf,save_file
from localstack.utils.patch import patch
from localstack.utils.persistence import is_persistence_enabled
from localstack.utils.strings import short_uid
from localstack_ext.bootstrap.aws_models import LambdaLayer
from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
from localstack_ext.bootstrap.pods.service_state.service_state_types import AssetByNameType
LOG=logging.getLogger(__name__)
LAMBDA_ASSETS_ROOT=_A
class LambdaPersistenceLifeCycle(StateLifecyclePlugin):
	name=_A;service=_A;TMP_LAMBDA_ARCHIVE_NAME='original_lambda_archive.zip'
	def retrieve_assets(C):
		B={}
		for (I,D) in awslambda_stores.items():
			for (J,E) in D.items():
				for (K,A) in E.lambdas.items():
					if isinstance(A,LambdaLayer):
						F=_get_details_for_lambda_layer_versions(A)
						for (L,G,H) in F:C._populate_assets(assets=B,zip_dir=G,asset_path=_asset_path_layer(H))
					else:C._populate_assets(assets=B,zip_dir=A.zip_dir,asset_path=_asset_path_function(A.arn()))
		return B
	def _populate_assets(C,assets,zip_dir,asset_path):
		A=zip_dir
		if not A:return
		B=os.path.join(A,C.TMP_LAMBDA_ARCHIVE_NAME)
		if not os.path.isfile(B):return
		D=load_file(B,mode='rb');assets[asset_path]=D
	def reset_state(B):
		def A(path):A=glob.glob(path);[rm_rf(B)for B in A]
		A(f"{localstack_config.dirs.tmp}/zipfile.*");A(f"{localstack_config.dirs.tmp}/layer.*");A(f"{localstack_config.dirs.tmp}/lambda")
	def has_assets(D):
		A=_C
		for B in ['*.zipfile.*','layer.*',_A]:C=glob.glob(f"{localstack_config.dirs.tmp}/{B}");A|=len(C)>0
		return A
	def inject_assets(D,pod_asset_directory):
		J='Could not restore asset for lambda ARN "%s": absolute path not found';H=os.path.join(pod_asset_directory,D.name);B=D.get_assets_location();rm_rf(B)
		if os.path.exists(H):cp_r(src=H,dst=B)
		for (Q,K) in awslambda_stores.items():
			for (R,L) in K.items():
				for (S,A) in L.lambdas.items():
					if isinstance(A,LambdaLayer):
						M=_get_details_for_lambda_layer_versions(A)
						for (N,O,P) in M:
							F=_asset_path_layer(arn=P);C=os.path.join(B,F)
							if not os.path.exists(C):LOG.info(J,A.arn());continue
							if not os.path.exists(O):E=f"layer.zipfile.{short_uid()}";A.versions[N][_D]=I=os.path.join(get_lambda_extraction_dir(),E);mkdir(I);G=os.path.join(I,D.TMP_LAMBDA_ARCHIVE_NAME);os.rename(C,G)
					else:
						F=_asset_path_function(A.arn());C=os.path.join(B,F)
						if not os.path.exists(C):LOG.info(J,A.arn());continue
						if not os.path.exists(A.zip_dir):E=f"function.zipfile.{short_uid()}";A.cwd=os.path.join(get_lambda_extraction_dir(),E);A.zip_dir=os.path.join(config.dirs.tmp,E);mkdir(A.cwd);mkdir(A.zip_dir)
						G=os.path.join(A.zip_dir,D.TMP_LAMBDA_ARCHIVE_NAME);os.rename(C,G)
		restore_backend_state()
		if not is_persistence_enabled():rm_rf(B)
def restore_backend_state(*J):
	A=[]
	for (K,D) in awslambda_stores.items():
		for (L,B) in D.items():
			A.append(B)
			for E in B.event_source_mappings:EventSourceListener.start_listeners(E)
	C=[C for B in A for C in B.lambdas.values()];F=[A for A in C if not isinstance(A,LambdaLayer)];G=[A for A in C if isinstance(A,LambdaLayer)]
	for H in G:do_restore_backend_state(H)
	for I in F:do_restore_backend_state(I)
def do_restore_backend_state(function_or_layer):
	A=function_or_layer
	try:
		A._is_restoring_state=True
		if isinstance(A,LambdaLayer):
			for B in A.versions.values():store_and_get_layer_code_archive(lambda_layer=A,layer_version=B,code={},zip_file_content=_B)
		else:A.state='Pending';lambda_api.set_function_code(A)
	except Exception as C:LOG.info('Unable to load user code for Lambda function %s: %s',A.arn(),C)
	finally:delattr(A,_E)
def _get_details_for_lambda_layer_versions(lambda_layer):return[(B,C,A.get('LayerVersionArn'))for(B,A)in lambda_layer.versions.items()if(C:=A.get(_D))]
def _asset_path_layer(arn):A=arn.split(':');B=A[-1];C=f"{A[-2]}_{B}";D=A[3];return os.path.join(_H,D,C)
def _asset_path_function(arn):A=arn.split(':');B=A[-1];C=A[3];return os.path.join(_F,C,B)
def store_and_get_layer_code_archive(lambda_layer,layer_version,code,zip_file_content=_B):
	E=zip_file_content;D=layer_version;B=lambda_layer;A=f"{get_persistent_zip_file_path(B,_H)}_{D['Version']}";G=code.get(_G)==localstack_config.BUCKET_MARKER_LOCAL;H=getattr(B,_E,_C)
	if H and A and file_exists_not_empty(A):E=load_file(A,mode='rb')
	C=store_layer_archive(code,layer=B,layer_version=D,zip_file_content=E)
	if C and A and not G:
		F=os.path.join(C,LAMBDA_ZIP_FILE_NAME)
		if F:cp_r(F,A)
	return C
def store_layer_archive(code,layer,layer_version,zip_file_content=_B):
	F='S3Key';D=layer_version;B=code;A=zip_file_content;E=B.get(_G)==config.BUCKET_MARKER_LOCAL
	if E and config.LAMBDA_REMOTE_DOCKER:G='Please note that Lambda Layer mounts (bucket name "%s") cannot be used with LAMBDA_REMOTE_DOCKER=1';raise Exception(G%config.BUCKET_MARKER_LOCAL)
	if E:layer.cwd=B.get(F);return B[F]
	A=A or get_zip_bytes(B)
	if not A:return
	C=os.path.join(config.dirs.tmp,f"layer.zipfile.{short_uid()}");mkdir(C);H=os.path.join(C,LAMBDA_ZIP_FILE_NAME);I=base64.standard_b64encode(hashlib.sha256(A).digest());save_file(H,A);D[_D]=C;D['CodeSize']=len(A);D['CodeSha256']=I.decode('utf-8');return C
def get_persistent_zip_file_path(lambda_function,subdir=_F):A=lambda_function;C=A.region();B=os.path.join(config.dirs.data,LAMBDA_ASSETS_ROOT,subdir,C);mkdir(B);D=os.path.join(B,A.name());return D
@patch(lambda_api.store_and_get_lambda_code_archive)
def store_and_get_lambda_code_archive(fn,lambda_function,zip_file_content=_B):
	E=zip_file_content;B=lambda_function;A=get_persistent_zip_file_path(B,_F);F=B.code.get(_G)==localstack_config.BUCKET_MARKER_LOCAL;G=getattr(B,_E,_C)
	if G and A and file_exists_not_empty(A):E=load_file(A,mode='rb')
	C=fn(B,E)
	if C and A and not F:
		D=C[1]
		if D and os.path.exists(D):cp_r(D,A)
	return C