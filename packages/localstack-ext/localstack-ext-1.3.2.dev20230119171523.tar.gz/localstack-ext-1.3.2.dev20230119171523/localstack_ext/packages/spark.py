_A='spark-submit'
import glob,logging,os
from typing import Dict,List
from localstack import config
from localstack.constants import MAVEN_REPO_URL
from localstack.packages import InstallTarget,Package,PackageInstaller
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.utils.archives import unzip
from localstack.utils.files import cp_r,file_exists_not_empty,load_file,mkdir,new_tmp_dir,new_tmp_file,rm_rf,save_file
from localstack.utils.http import download
from localstack.utils.run import run
from localstack.utils.testutil import create_zip_file
from localstack_ext import config as ext_config
from localstack_ext.packages.java import java_package
LOG=logging.getLogger(__name__)
SPARK_URL='https://archive.apache.org/dist/spark/spark-{version}/spark-{version}-bin-without-hadoop.tgz'
DEFAULT_SPARK_VERSION='2.4.3'
SPARK_VERSIONS=[DEFAULT_SPARK_VERSION,'2.4.8','3.1.2']
AWS_SDK_VER='1.12.339'
HADOOP_VERSION='2.9.2'
JAR_URLS=[f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk/{AWS_SDK_VER}/aws-java-sdk-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-core/{AWS_SDK_VER}/aws-java-sdk-core-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-glue/{AWS_SDK_VER}/aws-java-sdk-glue-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-s3/{AWS_SDK_VER}/aws-java-sdk-s3-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-dynamodb/{AWS_SDK_VER}/aws-java-sdk-dynamodb-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-lakeformation/{AWS_SDK_VER}/aws-java-sdk-lakeformation-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-bundle/{AWS_SDK_VER}/aws-java-sdk-bundle-{AWS_SDK_VER}.jar",f"{MAVEN_REPO_URL}/org/apache/hadoop/hadoop-hdfs/{HADOOP_VERSION}/hadoop-hdfs-{HADOOP_VERSION}.jar",f"{MAVEN_REPO_URL}/org/apache/hadoop/hadoop-common/{HADOOP_VERSION}/hadoop-common-{HADOOP_VERSION}.jar",f"{MAVEN_REPO_URL}/org/apache/hadoop/hadoop-auth/{HADOOP_VERSION}/hadoop-auth-{HADOOP_VERSION}.jar",f"{MAVEN_REPO_URL}/org/apache/hadoop/hadoop-aws/{HADOOP_VERSION}/hadoop-aws-{HADOOP_VERSION}.jar",f"{MAVEN_REPO_URL}/com/typesafe/config/1.3.3/config-1.3.3.jar",f"{MAVEN_REPO_URL}/com/fasterxml/jackson/dataformat/jackson-dataformat-csv/2.11.4/jackson-dataformat-csv-2.11.4.jar",f"{MAVEN_REPO_URL}/com/fasterxml/jackson/core/jackson-core/2.11.4/jackson-core-2.11.4.jar",f"{MAVEN_REPO_URL}/com/github/tony19/named-regexp/0.2.6/named-regexp-0.2.6.jar",f"{MAVEN_REPO_URL}/com/amazon/emr/emr-dynamodb-hadoop/4.12.0/emr-dynamodb-hadoop-4.12.0.jar",f"{MAVEN_REPO_URL}/de/undercouch/bson4jackson/2.11.0/bson4jackson-2.11.0.jar",f"{MAVEN_REPO_URL}/com/google/guava/guava/30.0-jre/guava-30.0-jre.jar",f"{MAVEN_REPO_URL}/org/apache/commons/commons-configuration2/2.7/commons-configuration2-2.7.jar",f"{MAVEN_REPO_URL}/commons-configuration/commons-configuration/1.10/commons-configuration-1.10.jar",f"{MAVEN_REPO_URL}/org/apache/commons/commons-text/1.9/commons-text-1.9.jar",f"{MAVEN_REPO_URL}/commons-lang/commons-lang/2.6/commons-lang-2.6.jar",f"{MAVEN_REPO_URL}/org/apache/logging/log4j/log4j-api/2.14.0/log4j-api-2.14.0.jar",f"{MAVEN_REPO_URL}/org/postgresql/postgresql/42.3.1/postgresql-42.3.1.jar",f"{MAVEN_REPO_URL}/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar",f"{MAVEN_REPO_URL}/org/apache/hadoop/thirdparty/hadoop-shaded-protobuf_3_7/1.0.0/hadoop-shaded-protobuf_3_7-1.0.0.jar",f"{MAVEN_REPO_URL}/com/google/re2j/re2j/1.5/re2j-1.5.jar"]
REPO_URL_GLUE_LIBS='git+https://github.com/awslabs/aws-glue-libs.git#egg=aws-glue-libs'
REPO_URL_GLUE_LIBS_0_9='git+https://github.com/localstack/aws-glue-libs.git@glue-0.9#egg=aws-glue-libs'
JAR_FOLDER='/usr/local/gluePyspark'
if ext_config.BIGDATA_MONO_CONTAINER:JAR_FOLDER=os.path.join(config.dirs.var_libs,'gluePyspark')
class SparkPackage(Package):
	def __init__(A):super().__init__('Spark',default_version=DEFAULT_SPARK_VERSION)
	def get_versions(A):return SPARK_VERSIONS
	def _get_installer(A,version):return SparkInstaller(version)
class SparkInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='spark',version=version,extract_single_directory=True)
	def get_installed_dir(B):
		A=super().get_installed_dir()
		if A:
			if ext_config.BIGDATA_MONO_CONTAINER:return A
			from localstack_ext.utils import hadoop as C;D=get_spark_home_in_container(B.version)
			if C.path_exists_in_container(D):return A
	def _get_download_url(A):return SPARK_URL.format(version=A.version)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin',_A)
	def _post_process(D,target):
		from localstack_ext.utils import hadoop as B;G=D._get_install_dir(target);K=D._get_install_marker_path(G);A=get_spark_home_in_container(D.version);P=os.path.join(A,'bin',_A)
		if not ext_config.BIGDATA_MONO_CONTAINER and B.path_exists_in_container(P):return
		if not os.path.exists(K):
			LOG.warning("Unable to find 'spark-submit' in the downloaded archive: %s",K)
			if not os.path.exists(G):LOG.warning('Target installation dir does not exist: %s',G)
		if not ext_config.BIGDATA_MONO_CONTAINER:LOG.debug('Copying Spark installation into bigdata container: %s',A);B.copy_into_spark_container(G,A)
		H=[]
		if not ext_config.BIGDATA_MONO_CONTAINER:H.append(['cp',f"{B.DEFAULT_SPARK_HOME}/conf/spark-env.sh",f"{A}/conf/spark-env.sh"])
		H.append(['sed','-ie','$s/^exec "\\${CMD\\[@]}"/if [ -n "$SPARK_OVERWRITE_CP" ]; then CMD[2]="$SPARK_OVERWRITE_CP:${CMD[2]}"; fi\\nCMD=("${CMD[0]}" "-Dcom.amazonaws.sdk.disableCertChecking=true" "${CMD[@]:1}"); exec "${CMD[@]}"/',f"{A}/bin/spark-class"])
		for I in H:B.run_in_presto(I)
		C=new_tmp_file();save_file(C,B.SPARK_DEFAULTS_CONF);B.copy_into_spark_container(C,f"{A}/conf/spark-defaults.conf");rm_rf(C)
		if ext_config.BIGDATA_MONO_CONTAINER:from localstack_ext.packages.hadoop import HadoopInstaller as Q,get_hadoop_home_in_container as R;L=get_hadoop_version_for_spark_version(D.version);Q(L).install();J=new_tmp_file();M=R(L);S=f'\n            export SPARK_DIST_CLASSPATH="$({M}/bin/hadoop classpath)"\n            export HADOOP_CONF_DIR="{M}/etc/hadoop"\n            ';save_file(J,S);B.copy_into_spark_container(J,f"{A}/conf/spark-env.sh");rm_rf(J)
		if ext_config.BIGDATA_MONO_CONTAINER:
			N=REPO_URL_GLUE_LIBS
			if D.version=='2.2.1':N=REPO_URL_GLUE_LIBS_0_9
			I=['pip','install',N];run(I)
		if ext_config.BIGDATA_MONO_CONTAINER:
			download_additional_jar_files();O=f"{A}/conf/spark-defaults.conf";C=load_file(O)
			if'/gluePyspark'not in C:C+=f"\nspark.driver.extraClassPath {JAR_FOLDER}/*\nspark.executor.extraClassPath {JAR_FOLDER}/*\nspark.driver.allowMultipleContexts = true\n";save_file(O,C)
		if ext_config.BIGDATA_MONO_CONTAINER:E=os.path.join(A,'python/lib/py4j-*-src.zip');E=glob.glob(E)[0];F={'from collections import':'from collections.abc import'};replace_in_zip_file(E,'py4j/java_collections.py',F);E=os.path.join(A,'python/lib/pyspark.zip');F={'import collections\n':'import collections.abc\n','collections.Iterable':'collections.abc.Iterable'};replace_in_zip_file(E,'pyspark/resultiterable.py',F);F={'_cell_set_template_code =':'# _cell_set_template_code ='};replace_in_zip_file(E,'pyspark/cloudpickle.py',F)
		if ext_config.BIGDATA_MONO_CONTAINER and D.version.startswith('2.'):java_package._get_installer('8').install()
	def copy_into_container(A):return A._post_process(InstallTarget.VAR_LIBS)
spark_package=SparkPackage()
def replace_in_zip_file(zip_file,file_path,search_replace,raise_if_missing=False):
	C=zip_file;A=new_tmp_dir();unzip(C,A);B=os.path.join(A,file_path)
	if not os.path.exists(B):
		if raise_if_missing:raise Exception(f"Unable to replace content in non-existing file in archive: {B}")
		return
	replace_in_file(B,search_replace);create_zip_file(A,C);rm_rf(A)
def replace_in_file(file_path,search_replace):
	B=file_path;A=load_file(B)
	for (C,D) in search_replace.items():A=A.replace(C,D)
	save_file(B,A)
def get_hadoop_version_for_spark_version(spark_version):
	from localstack_ext.packages.hadoop import HADOOP_DEFAULT_VERSION as A
	if ext_config.BIGDATA_MONO_CONTAINER and spark_version=='2.2.1':return'2.10.2'
	return A
def get_spark_install_cache_dir(spark_version):return spark_package.get_installer(spark_version)._get_install_dir(InstallTarget.VAR_LIBS)
def get_spark_home_in_container(spark_version):
	A=spark_version
	if ext_config.BIGDATA_MONO_CONTAINER:return get_spark_install_cache_dir(A)
	return f"/usr/local/spark-{A}"
def download_additional_jar_files():
	for A in JAR_URLS:download_and_cache_jar_file(A)
	return JAR_FOLDER
def download_and_cache_jar_file(jar_url):
	B=jar_url;mkdir(JAR_FOLDER);C=os.path.join(JAR_FOLDER,B.split('/')[-1])
	if file_exists_not_empty(C):return C
	A=os.path.join(config.dirs.var_libs,'bigdata-jars',B.split('/')[-1])
	if not file_exists_not_empty(A):download(B,A)
	cp_r(A,C);return A