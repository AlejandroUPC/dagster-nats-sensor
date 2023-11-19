from dagster import RunRequest
from datetime import datetime
import json

NATS_REQUEST_TO_JOB_MAP = {"CREATE": "create_tenant_job", "DELETE": "delete_tenant_job"}


def message_router(nats_message: str) -> RunRequest:
    """
    Given the field "action" in the message payload from NATS returns the appropiate run request.

    Args:
        nats_message (str): NATS original message

    Returns:
        RunRequest: Dagster RunRequest
    """
    try:
        serialized_message = json.loads(nats_message)
        return RunRequest(
            job_name=NATS_REQUEST_TO_JOB_MAP[serialized_message["action"]],
            run_key=f"{serialized_message['tenant_name']}|{int(datetime.now().timestamp())}",
            # run_config=serialized_message['configuration'] comment this temporaly, needs deeper understanding of dagser job_config
        )
    except KeyError:
        raise ValueError(
            f"The action field in the NATS message payload is not valid {nats_message['action']}, should be in {', '.join(NATS_REQUEST_TO_JOB_MAP.keys())}"
        )
