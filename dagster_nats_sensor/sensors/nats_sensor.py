from dagster import sensor, SkipReason, DefaultSensorStatus
import asyncio
import nats
from nats import errors
from ..utils.message_router import message_router
from ..jobs import create_tenant_job, delete_tenant_job

@sensor(default_status=DefaultSensorStatus.RUNNING,jobs=[create_tenant_job,delete_tenant_job])
def nats_sensor(context):
    async def nats_sensor_async():
        nc = await nats.connect("nats://localhost:4222")
        js = nc.jetstream()
        sub = await js.pull_subscribe("tenants", "MY_STREAM")

        try:
            messages = await sub.fetch(batch=1,timeout=5)
            if messages:
                message = messages[0]
                await message.ack()
            message_data = message.data.decode()
            return message_router(message_data)
        except errors.TimeoutError:
            return SkipReason("Did not receive a message in 5 seconds")
        finally:
            await nc.close()
    return asyncio.run(nats_sensor_async())
