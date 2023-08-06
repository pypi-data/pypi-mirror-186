_B='specification'
_A='latest'
import glob,os
from typing import List
from localstack.packages import InstallTarget,Package,PackageInstaller
from localstack.utils.archives import download_and_extract_with_retry
from localstack.utils.files import mkdir,rm_rf
from localstack.utils.http import download
DOWNLOAD_FULL_SPECS=False
SPEC_ZIP_URL='https://github.com/Azure/azure-rest-api-specs/archive/main.zip'
GITHUB_AZURE_SPECS_URL='https://raw.githubusercontent.com/Azure/azure-rest-api-specs/<branch>/'
SPEC_FILES={}
SPECS={'eventhub-hubs':'eventhub/resource-manager/Microsoft.EventHub/stable/2017-04-01/eventhubs.json','eventhub-namespaces':'eventhub/resource-manager/Microsoft.EventHub/stable/2017-04-01/namespaces.json','eventhub-authrules':'eventhub/resource-manager/Microsoft.EventHub/stable/2017-04-01/AuthorizationRules.json','eventhub-consumergroups':'eventhub/resource-manager/Microsoft.EventHub/stable/2017-04-01/consumergroups.json','storage-accounts':'storage/resource-manager/Microsoft.Storage/stable/2019-06-01/storage.json','storage-blob':'storage/data-plane/Microsoft.BlobStorage/preview/2021-02-12/blob.json','storage-queue':'storage/data-plane/Microsoft.QueueStorage/preview/2018-03-28/queue.json','subscriptions':'subscription/resource-manager/Microsoft.Subscription/stable/2020-09-01/subscriptions.json','web-apps':'web/resource-manager/Microsoft.Web/stable/2020-06-01/WebApps.json','web-resources':'web/resource-manager/Microsoft.Web/stable/2020-06-01/ResourceProvider.json','service-plans':'web/resource-manager/Microsoft.Web/stable/2020-06-01/AppServicePlans.json','resource-groups':'resources/resource-manager/Microsoft.Resources/stable/2020-10-01/resources.json','resource-graph':'resourcegraph/resource-manager/Microsoft.ResourceGraph/stable/2019-04-01/resourcegraph.json','appinsights-components':'applicationinsights/resource-manager/Microsoft.Insights/stable/2015-05-01/components_API.json','devops':'devops/resource-manager/Microsoft.DevOps/preview/2020-07-13-preview/devops.json','servicebus':'servicebus/resource-manager/Microsoft.ServiceBus/stable/2017-04-01/eventhubs.json'}
class AzureApiSpecsPackage(Package):
	def __init__(A):super().__init__('Azure Rest API Specs',_A)
	def get_versions(A):return[_A]
	def _get_installer(A,version):return AzureApiSpecsPackageInstaller()
class AzureApiSpecsPackageInstaller(PackageInstaller):
	def __init__(A):super().__init__('azure-api-specs',_A)
	def _get_install_dir(A,target):return os.path.join(target.value,A.name,'azure-rest-api-specs-main')
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,_B)
	def _install(H,target):
		B=H._get_install_dir(target);mkdir(B);D=os.path.realpath(os.path.join(B,'..'));A=os.path.join(B,'package.json')
		if DOWNLOAD_FULL_SPECS and not os.path.exists(A):E=os.path.join(D,'tmp.azure.specs.zip');download_and_extract_with_retry(SPEC_ZIP_URL,E,D);rm_rf(E)
		A=os.path.join(B,_B,'eventgrid','resource-manager','Microsoft.EventGrid','preview')
		if os.path.exists(A):
			for I in glob.glob('%s/**/preview/'%D,recursive=True):rm_rf(I)
		if not SPEC_FILES:
			for (L,C) in SPECS.items():
				F='main'
				if isinstance(C,dict):F,C=next(iter(C.items()))
				SPEC_FILES.update({C:GITHUB_AZURE_SPECS_URL.replace('<branch>',F)})
		for (G,J) in SPEC_FILES.items():
			A=os.path.join(B,_B,G)
			if not os.path.exists(A):K='%s/specification/%s'%(J,G);download(K,A)
azure_api_specs_package=AzureApiSpecsPackage()