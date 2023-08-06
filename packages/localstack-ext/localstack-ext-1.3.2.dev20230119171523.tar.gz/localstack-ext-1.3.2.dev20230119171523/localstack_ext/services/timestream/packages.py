_A='timescaledb.so'
import os.path
from functools import cached_property
from typing import List
from localstack.packages import InstallTarget,Package,PackageInstaller
from localstack.utils.files import new_tmp_file,rm_rf,save_file
from localstack.utils.http import download
from localstack.utils.run import run
from localstack_ext.packages import OSPackageInstaller
class TimescaleDbPackage(Package):
	def __init__(A):super().__init__('TimescaleDb','2.0.1')
	def get_versions(A):return['2.0.1']
	def _get_installer(A,version):return TimescaleDbPackageInstaller(version)
class TimescaleDbPackageInstaller(OSPackageInstaller):
	def __init__(A,version):super().__init__('timescale-db',version)
	def _debian_prepare_install(E,target):
		B='/etc/apt/sources.list.d/timescaledb.list'
		if not os.path.exists(B):A=new_tmp_file();download('https://packagecloud.io/timescale/timescaledb/gpgkey',A);run(['apt-key','add',A]);rm_rf(A);C=run(['lsb_release','-cs']).strip();D=f"deb https://packagecloud.io/timescale/timescaledb/debian/ {C} main";save_file(B,D)
		super()._debian_prepare_install(target)
	def _debian_packages(A):return[f"timescaledb-2-postgresql-11='{A.version}~debian10'",f"timescaledb-2-loader-postgresql-11='{A.version}~debian10'"]
	def _debian_get_install_marker_path(A,install_dir):return os.path.join(install_dir,_A)
	def _debian_get_install_dir(A,target):return'/usr/lib/postgresql/11/lib/'
	@cached_property
	def redhat_release(self):return run(['rpm','-E','%{rhel}']).strip()
	def _redhat_prepare_install(A,target):B=f"""
[timescale_timescaledb]
name=timescale_timescaledb
baseurl=https://packagecloud.io/timescale/timescaledb/el/{A.redhat_release}/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/timescale/timescaledb/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
""";save_file('/etc/yum.repos.d/timescale_timescaledb.repo',B)
	def _redhat_packages(A):return[f"timescaledb-2-postgresql-11-{A.version}-0.el{A.redhat_release}",f"timescaledb-2-loader-postgresql-11-{A.version}-0.el{A.redhat_release}"]
	def _redhat_get_install_marker_path(A,install_dir):return os.path.join(install_dir,_A)
	def _redhat_get_install_dir(A,target):return'/usr/pgsql-11/lib/'
timescaledb_package=TimescaleDbPackage()