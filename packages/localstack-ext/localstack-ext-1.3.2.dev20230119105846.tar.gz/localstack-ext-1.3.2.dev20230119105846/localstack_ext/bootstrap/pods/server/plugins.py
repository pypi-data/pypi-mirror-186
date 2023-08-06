import logging,os
from typing import Dict,Optional
from localstack import config
from localstack.utils.files import cp_r,rm_rf
from plugin import Plugin
LOG=logging.getLogger(__name__)
class StateLifecyclePlugin(Plugin):
	namespace='localstack.state.lifecycle';service:str
	def get_assets_location(A):B=config.dirs.data;return os.path.join(B,A.service)
	def has_assets(B):
		A=B.get_assets_location()
		if os.path.exists(A)and len(os.listdir(A))>0:return True
		return False
	def retrieve_assets(G):
		A=G.get_assets_location();B={}
		if not os.path.isdir(A):return B
		for (D,L,H) in os.walk(A,topdown=True):
			for C in H:
				E=os.path.relpath(D,A);I=os.path.join(E,C)if E!='.'else C;F=os.path.join(D,C)
				if os.path.isfile(F):J=I;K=_load_asset_binary(F);B[J]=K
		return B
	def inject_assets(A,pod_asset_directory):
		B=A.get_assets_location();C=os.path.join(pod_asset_directory,A.service);rm_rf(B)
		if os.path.exists(C):cp_r(C,B)
	def reset_state(A):A.on_after_reset()
	def on_after_reset(A):0
def _load_asset_binary(file_path):
	A=file_path
	try:
		with open(A,'rb')as B:return B.read()
	except Exception as C:LOG.warning(f"Could not load assets binary for file {A} due to {C}.");return None