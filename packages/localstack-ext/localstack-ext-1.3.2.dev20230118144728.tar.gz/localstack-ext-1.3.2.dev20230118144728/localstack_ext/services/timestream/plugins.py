from localstack.packages import Package
from localstack_ext.packages.core import pro_package
@pro_package(name='timescaledb')
def timestream_query_packages():from .packages import timescaledb_package as A;return A