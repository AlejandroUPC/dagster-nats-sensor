from dagster import job
from ..ops.create_tenant_ops import create_tenant


@job
def create_tenant_job():
    create_tenant()
