from dagster import op


@op
def delete_tenant(context):
    context.log.info(f"Deleting tenant {context.dagster_run[9]['dagster/run_key'].split('|')[0]}...")
