from dagster import op


@op
def create_tenant(context):
    context.log.info(
        f"Creating tenant {context.dagster_run[9]['dagster/run_key'].split('|')[0]}..."
    )
