_A='stepfunctions'
import logging
from typing import Optional
import localstack.config as localstack_config
from localstack.services.stepfunctions import stepfunctions_starter as sfn_starter
from localstack.services.stepfunctions.stepfunctions_starter import start_stepfunctions,wait_for_stepfunctions
from localstack.utils.files import rm_rf
from localstack.utils.net import wait_for_port_closed,wait_for_port_open
from localstack.utils.run import wait_for_process_to_be_killed
from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
LOG=logging.getLogger(__name__)
class StepfunctionsPersistencePlugin(StateLifecyclePlugin):
	name=_A;service=_A
	def reset_state(A):rm_rf(A.get_assets_location());A._restart_and_wait()
	def inject_assets(A,pod_asset_directory):super().inject_assets(pod_asset_directory);A._restart_and_wait()
	@staticmethod
	def _restart_and_wait():restart_stepfunctions();wait_for_stepfunctions()
def restart_stepfunctions(persistence_path=None):
	if not sfn_starter.PROCESS_THREAD or not sfn_starter.PROCESS_THREAD.process:return
	LOG.debug('Restarting StepFunctions process ...');A=sfn_starter.PROCESS_THREAD.process.pid;sfn_starter.PROCESS_THREAD.stop();wait_for_port_closed(localstack_config.LOCAL_PORT_STEPFUNCTIONS,sleep_time=0.5,retries=15)
	try:wait_for_process_to_be_killed(A,sleep=0.3,retries=10)
	except Exception as B:LOG.warning('StepFunctions process not properly terminated: %s',B)
	start_stepfunctions(persistence_path=persistence_path);wait_for_port_open(localstack_config.LOCAL_PORT_STEPFUNCTIONS,sleep_time=0.6,retries=15)