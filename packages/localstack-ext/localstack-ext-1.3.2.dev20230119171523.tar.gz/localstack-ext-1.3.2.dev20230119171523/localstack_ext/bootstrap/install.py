import logging,os,traceback
from contextlib import contextmanager
from localstack import constants
from localstack.constants import ARTIFACTS_REPO
from localstack.packages import InstallTarget,PackageException
from localstack.utils.http import download
from localstack.utils.time import now
from localstack_ext.bootstrap.licensing import is_enterprise
LOG=logging.getLogger(__name__)
SSL_CERT_URL=f"{ARTIFACTS_REPO}/raw/master/local-certs/server.key"
SSL_CERT_URL_FALLBACK='{api_endpoint}/proxy/localstack.cert.key'
@contextmanager
def log_package_exception():
	try:yield
	except PackageException:LOG.exception('Package installation failed.')
def install_libs():
	from localstack_ext.packages.postgres import postgresql_package as B;from localstack_ext.services.elasticache.packages import redis_package as C;from localstack_ext.services.iot.packages import iot_rule_engine_package as D,mosquitto_package as E;from localstack_ext.services.stepfunctions.packages import stepfunctions_pro_package as F;from localstack_ext.services.timestream.packages import timescaledb_package as G;A=InstallTarget.STATIC_LIBS
	with log_package_exception():D.install(target=A)
	with log_package_exception():B.install(target=A)
	with log_package_exception():G.install(target=A)
	with log_package_exception():C.install(target=A)
	with log_package_exception():E.install(target=A)
	with log_package_exception():F.install(target=A)
def setup_ssl_cert():
	from localstack.services import generic_proxy as C;A=C.get_cert_pem_file_path()
	if os.path.exists(A):
		if is_enterprise():LOG.debug('Avoiding to update SSL certificate.');return
		D=6*60*60;E=os.path.getmtime(A)
		if E>now()-D:LOG.debug('Using cached SSL certificate (less than 6hrs since last update).');return
	LOG.debug('Attempting to download local SSL certificate file');F=3;G=5
	try:return download_github_artifact(SSL_CERT_URL,A,timeout=F)
	except Exception:
		B=SSL_CERT_URL_FALLBACK.format(api_endpoint=constants.API_ENDPOINT)
		try:return download(B,A,timeout=G)
		except Exception as H:LOG.info('Unable to download local test SSL certificate from %s to %s (using self-signed cert as fallback): %s',B,A,H);raise
def download_github_artifact(url,target_file,timeout=None):
	B=target_file;A=url
	def C(url,print_error=False):
		try:download(url,B,timeout=timeout);return True
		except Exception as A:
			if print_error:LOG.info('Unable to download Github artifact from from %s to %s: %s %s'%(url,B,A,traceback.format_exc()))
	D=C(A)
	if not D:A=A.replace('https://github.com','https://cdn.jsdelivr.net/gh');A=A.replace('/raw/master/','@master/');C(A,True)