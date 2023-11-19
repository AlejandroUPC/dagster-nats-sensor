from dagster import job
from ..ops.delete_tenant_ops import delete_tenant


@job
def delete_tenant_job():
    delete_tenant()
