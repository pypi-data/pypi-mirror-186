from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
class S3PersistencePlugin(StateLifecyclePlugin):
	name='s3';service='s3'
	def on_after_reset(B):from localstack_ext.services.s3.s3_extended import apply_model_patches as A;A()