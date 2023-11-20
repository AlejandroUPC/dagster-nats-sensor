# Dagster jobs on events

## Description

This project is designed to react to run some jobs based on events from a message bus, like NATS in this example. In this case it simply will triger a job to create
a tenant or delete it based on some of the payload recieved from the NATS message.

## Requirements

To run this project, you will need:

- [Python 3.9+](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

## Installation

To install this project, follow these steps:

1. Install the dependencies. 
```sh
poetry install --no-root
```
2. Run the docker-compose file.
```sh
docker-compose up -d
```


## How to Run

To run this project, follow these steps

1. Recommended to run as debug mode on Dagster, so your file `launch.json` could look something like:
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Dagster Dev Local",
            "type": "python",
            "request": "launch",
            "module": "dagster",
            "console": "integratedTerminal",
            "justMyCode": false,
            "args": [
                "dev",
            ]
        }
    ]
}
```
2. Start a simple debug session on vs code.
3. Access to your dagster environment on http://localhost:3000, check the sensors section.
4. Create and config (important, subject must be tenants) the stream tenants:
```sh
nats stream create tenants
```
5. Trigger messages on NATS, you can use the following command as example:
```sh
nats pub tenants "{\"action\":\"CREATE\",\"tenant_name\":\"tenant_1\",\"configuration\":{\"config_value\":\"1\"}}"
```

## Disclaimer

There are some things that obviously need to be improved, e.g if you check the sensor it ack the message even before triggering the run (should the message not be acked after the run is completed?).
This is by no means an intended production ready project but an attempt to implement a very simple functionality.
