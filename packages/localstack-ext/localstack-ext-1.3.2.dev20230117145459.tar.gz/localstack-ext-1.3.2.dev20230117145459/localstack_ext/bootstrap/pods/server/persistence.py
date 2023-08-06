_A=None
import logging,threading
from collections import defaultdict
from queue import PriorityQueue
from typing import Any,Type
import dill
from dill import _dill
from localstack.services.stores import AccountRegionBundle,BaseStore
from localstack.utils.objects import singleton_factory
from localstack.utils.patch import patch
from moto.core import BackendDict
from localstack_ext.bootstrap.pods.utils.common import LOCK_TYPE,RLOCK_TYPE
from localstack_ext.bootstrap.pods.utils.persistence import marshall_object
from localstack_ext.bootstrap.state_utils import get_object_dict,traverse_object
LOG=logging.getLogger(__name__)
PersistentStoreBaseType=BackendDict|AccountRegionBundle|BaseStore
def marshall_backend(backend):
	A=backend
	if isinstance(A,bytes):return A
	def B(_type):
		C=_type
		if hasattr(C,'_reduce_patched'):return
		def __reduce__(self):
			E='region_name';D='account_id';B=self;A=super(C,B).__reduce__();A=list(A)
			if len(A)>2:
				if A[2]is _A:A[2]=B.__dict__
				if D in B.__dict__ and E in B.__dict__:A[1]=B.__dict__[D],B.__dict__[E]
			return tuple(A)
		C.__reduce__=__reduce__;C._reduce_patched=True
	def C(_obj):
		A=type(_obj)
		if isinstance(_obj,defaultdict)and A!=defaultdict:B(A)
	traverse_object(A,handler=C,safe=True);D=marshall_object(A);return D
def unmarshall_object(blob):return dill.loads(blob)
def unmarshall_backend(backend):
	try:A=unmarshall_object(backend)
	except ModuleNotFoundError as B:LOG.warning('Unable to unmarshall a backend due to a missing module: "%s". This error is likely due to backend changes occurred between the creation and the injection of the Cloud Pod.',B);raise B
	def C(_obj):
		A=get_object_dict(_obj)
		if not A:return
		for (C,B) in A.items():
			if isinstance(B,PriorityQueue):
				try:E=type(B);A[C]=D=E()
				except Exception as F:LOG.warning(f"Could not reinitialise PriorityQueue of subtype {type(B)} with empty constructor: {F}.");A[C]=D=PriorityQueue()
				D.queue=B.queue
			if isinstance(B,RLOCK_TYPE):A[C]=threading.RLock()
			if isinstance(B,LOCK_TYPE):A[C]=threading.Lock()
	traverse_object(A,handler=C,safe=True);return A
@singleton_factory
def patch_cryptography_pickling():
	E='_evp_pkey';B='_rsa_cdata';from cryptography.hazmat.backends.openssl.backend import Backend as A;from cryptography.hazmat.backends.openssl.rsa import _RSAPrivateKey as C
	def D(self,state,*F,**G):A=state;C=A.get('_backend');A[B]=D=C._ffi.from_buffer(A[B]);A[E]=C._rsa_cdata_to_evp_pkey(D);self.__dict__.update(A)
	C.__setstate__=D
	def F(self,*G,**H):C=self;A=C.__dict__.copy();F=C._key_size;D=C._backend._ffi.buffer(A[B],F);D=D[:];A[B]=D;A.pop(E,_A);return A
	C.__getstate__=F
	def G(self,*B,**C):A=self.__dict__.copy();A.pop('_ffi',_A);A.pop('_lib',_A);return A
	A.__getstate__=G
	def H(self,state,*B,**C):A=self;A.__dict__.update(state);A._ffi=A._binding.ffi;A._lib=A._binding.lib
	A.__setstate__=H
@patch(_dill._create_rlock)
def _create_rlock(fn,count,owner,*B,**C):
	A=owner
	if A is not _A:return threading.RLock()
	return fn(count,A,*(B),**C)
patch_cryptography_pickling()