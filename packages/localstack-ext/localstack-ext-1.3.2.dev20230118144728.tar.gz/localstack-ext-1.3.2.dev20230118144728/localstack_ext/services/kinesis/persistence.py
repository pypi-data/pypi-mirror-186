_B='kinesis'
_A=False
import logging,os,threading
from localstack.utils.functions import run_safe
from localstack.utils.net import wait_for_port_closed
from localstack.utils.run import run
from localstack.utils.sync import synchronized
from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
LOG=logging.getLogger(__name__)
_LOCK=threading.RLock()
class KinesisPersistencePlugin(StateLifecyclePlugin):
	name=_B;service=_B
	def inject_assets(A,pod_asset_directory):shutdown_kinesis();super().inject_assets(pod_asset_directory)
	def reset_state(A):shutdown_kinesis(reset_state=True);super().reset_state()
@synchronized(lock=_LOCK)
def shutdown_kinesis(reset_state=_A):
	import psutil as G;from localstack.services.kinesis import kinesis_starter as C;D=C._SERVERS.copy().items()
	if not len(D):return _A
	for (H,A) in D:
		B=A.port;A._thread.auto_restart=_A;A.shutdown();A.join(timeout=10)
		try:wait_for_port_closed(B,sleep_time=0.8,retries=10)
		except Exception:LOG.warning('Kinesis server port %s (%s) unexpectedly still open; running processes: %s',B,A._thread,run(['ps','aux']));E=A._thread.process.pid;LOG.info('Attempting to kill Kinesis process %s',E);F=G.Process(E);run_safe(F.terminate);run_safe(F.kill);wait_for_port_closed(B,sleep_time=0.5,retries=8)
		if reset_state:os.unlink(os.path.join(A._data_dir,A._data_filename))
		C._SERVERS.pop(H)
	return True