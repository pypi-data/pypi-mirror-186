from localstack.runtime import hooks
from localstack_ext import config
from localstack_ext.plugins import api_key_configured
EXTENSION_HOOK_PRIORITY=-1
@hooks.on_infra_start(priority=EXTENSION_HOOK_PRIORITY,should_load=api_key_configured)
def extensions_on_infra_start():from localstack.services.internal import get_internal_apis as A;from localstack_ext.extensions.platform import run_on_infra_start_hook as B;from localstack_ext.extensions.resource import ExtensionsResource as C;A().add('/extensions',C());B()
@hooks.on_infra_ready(priority=EXTENSION_HOOK_PRIORITY,should_load=api_key_configured)
def extensions_on_infra_ready():from localstack_ext.extensions.platform import run_on_infra_ready_hook as A;A()
@hooks.configure_localstack_container(should_load=api_key_configured and config.EXTENSION_DEV_MODE)
def configure_extensions_dev_container(container):from localstack_ext.extensions.bootstrap import run_on_configure_localstack_container_hook as A;A(container)
@hooks.prepare_host(should_load=api_key_configured and config.EXTENSION_DEV_MODE)
def configure_extensions_dev_host():from localstack_ext.extensions.bootstrap import run_on_configure_host_hook as A;A()