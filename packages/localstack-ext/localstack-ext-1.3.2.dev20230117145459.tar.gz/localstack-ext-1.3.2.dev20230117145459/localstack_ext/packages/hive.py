_A='<version>'
import glob,logging,os,shutil
from typing import List
from localstack import config
from localstack.constants import MAVEN_REPO_URL
from localstack.packages import Package
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.utils.files import cp_r
from localstack.utils.strings import short_uid
from localstack_ext import config as ext_config
from localstack_ext.packages.spark import download_and_cache_jar_file
LOG=logging.getLogger(__name__)
HIVE_REMOVE_JAR_FILES=['hive-jdbc-handler-*.jar']
HIVE_JAR_FILES=[f"{MAVEN_REPO_URL}/org/postgresql/postgresql/42.5.0/postgresql-42.5.0.jar",f"{MAVEN_REPO_URL}/org/apache/hive/hive-jdbc-handler/3.1.3/hive-jdbc-handler-3.1.3.jar"]
HIVE_LEGACY_HOME='/usr/local/apache-hive-<version>-bin'
HIVE_LEGACY_DEFAULT_VERSION='2.3.5'
URL_PATTERN_HIVE='https://dlcdn.apache.org/hive/hive-<version>/apache-hive-<version>-bin.tar.gz'
HIVE_DEFAULT_VERSION='2.3.9'
HIVE_VERSIONS=[HIVE_DEFAULT_VERSION,'3.1.3']
class HiveInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='hive',version=version,extract_single_directory=True)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin','hiveserver2')
	def _get_download_url(A):return URL_PATTERN_HIVE.replace(_A,A.version)
	def is_installed(A):
		if not ext_config.BIGDATA_MONO_CONTAINER:return True
		return super().is_installed()
class HivePackage(Package):
	def __init__(A,default_version=HIVE_DEFAULT_VERSION):super().__init__(name='Hive',default_version=default_version)
	def get_versions(A):return HIVE_VERSIONS
	def _get_installer(A,version):return HiveInstaller(version)
	def install_requirements(Q):
		from localstack_ext.packages.hadoop import hadoop_package as C;from localstack_ext.packages.spark import download_additional_jar_files as I;hive_package.install();I();C.install();D=get_hive_home_dir();A=os.path.join(D,'lib');J=['hadoop-aws-*.jar','aws-java-sdk-bundle-*.jar'];K=C.get_installer().get_hadoop_home();L=os.path.join(K,'share/hadoop/tools/lib')
		for B in J:
			for E in glob.glob(f"{L}/{B}"):
				F=os.path.join(A,os.path.basename(E))
				if not os.path.exists(F):shutil.copy(E,F)
		for M in HIVE_REMOVE_JAR_FILES:
			B=f"{A}/{M}"
			for N in glob.glob(B):os.remove(N)
		for G in HIVE_JAR_FILES:O=os.path.join(A,G.rpartition('/')[2]);P=download_and_cache_jar_file(G);cp_r(P,O)
		H=os.path.join(D,'bin/ext/debug.sh')
		if os.path.exists(H):os.remove(H)
hive_package=HivePackage()
def get_hive_home_dir(version=None):
	if ext_config.BIGDATA_MONO_CONTAINER:A=hive_package.get_installer(version).get_installed_dir();return A
	return HIVE_LEGACY_HOME.replace(_A,HIVE_LEGACY_DEFAULT_VERSION)
def get_hive_warehouse_dir():
	if ext_config.BIGDATA_MONO_CONTAINER:
		if config.PERSISTENCE:A=config.dirs.data
		else:A=os.path.join(config.TMP_FOLDER,f"hive-{short_uid()}")
		return os.path.join(A,'hive-warehouse')
	return'/user/hive/warehouse'
def get_hive_lib_dir(version=None):return os.path.join(get_hive_home_dir(version),'lib')