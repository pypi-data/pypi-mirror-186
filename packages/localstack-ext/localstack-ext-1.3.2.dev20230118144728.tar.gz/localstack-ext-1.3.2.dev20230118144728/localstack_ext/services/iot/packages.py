_B='mosquitto'
_A='latest'
import os
from typing import List
from localstack.packages import InstallTarget,Package,PackageInstaller
from localstack.packages.core import ExecutableInstaller
from localstack.utils.run import run
from localstack_ext.packages.core import OSPackageInstaller
RULE_ENGINE_INSTALL_URL='https://github.com/whummer/serverless-iot-offline'
class MosquittoPackage(Package):
	def __init__(A):super().__init__('Mosquitto',_A)
	def get_versions(A):return[_A]
	def _get_installer(A,version):return MosquittoPackageInstaller(version)
class MosquittoPackageInstaller(OSPackageInstaller):
	def __init__(A,version):super().__init__(_B,version)
	def _debian_packages(A):return[_B]
	def _debian_get_install_marker_path(A,install_dir):return'/usr/sbin/mosquitto'
	def _debian_get_install_dir(A,target):return'/etc/mosquitto'
class IoTRuleEnginePackage(Package):
	def __init__(A):super().__init__('IoTRuleEngine',_A)
	def get_versions(A):return[_A]
	def _get_installer(A,version):return IoTRuleEnginePackageInstaller('iot-rule-engine',version)
class IoTRuleEnginePackageInstaller(ExecutableInstaller):
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'node_modules','serverless-iot-offline','query.js')
	def _install(A,target):B=A._get_install_dir(target);run(['npm','install','--prefix',B,RULE_ENGINE_INSTALL_URL])
iot_rule_engine_package=IoTRuleEnginePackage()
mosquitto_package=MosquittoPackage()