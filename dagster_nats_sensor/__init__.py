from dagster import Definitions
from .sensors.nats_sensor import nats_sensor


defs = Definitions(
    sensors=[nats_sensor],
)
