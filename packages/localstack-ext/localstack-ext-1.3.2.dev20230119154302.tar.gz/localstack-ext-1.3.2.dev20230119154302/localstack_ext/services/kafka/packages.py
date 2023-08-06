_A='latest'
from typing import List
from localstack.constants import ARTIFACTS_REPO
from localstack.packages import DownloadInstaller,Package,PackageInstaller
class KafkaPackage(Package):
	def __init__(A):super().__init__(name='Kafka',default_version=_A)
	def get_versions(A):return[_A]
	def _get_installer(A,version):return KafkaPackageInstaller('kafka',version)
class KafkaPackageInstaller(DownloadInstaller):
	def _get_download_url(A):return f"{ARTIFACTS_REPO}/raw/master/kafka-server/build/libs/kafka-server-all.jar"
kafka_package=KafkaPackage()