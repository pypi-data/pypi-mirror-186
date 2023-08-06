from localstack.config import is_env_true
from localstack.packages import Package
from localstack_ext.packages.core import pro_package
@pro_package(name='azure',should_load=lambda:is_env_true('AZURE'))
def azure_package():from .packages import azure_api_specs_package as A;return A