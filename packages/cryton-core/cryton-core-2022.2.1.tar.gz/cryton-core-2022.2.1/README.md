[[_TOC_]]

![Coverage](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core/badges/master/coverage.svg)

# Cryton Core

## Description
Cryton Core is the center point of the Cryton toolset. It is used for:
- Creating, planning, and scheduling attack scenarios.
- Generating reports from attack scenarios.
- Controlling Workers and scenarios execution.

To be able to execute the attack scenarios, you 
also need to install the **[Cryton Worker](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-worker)** 
and **[Cryton CLI](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-cli)** package. Optionally you can install
[Cryton Frontend](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-frontend) for non-command line experience.

Cryton toolset is tested and targeted primarily on **Debian** and **Kali Linux**. Please keep in mind that 
**only the latest version is supported** and issues regarding different OS or distributions may **not** be resolved.

[Link to the documentation](https://beast-public.gitlab-pages.ics.muni.cz/cryton/cryton-documentation/).

## Settings
Cryton Core uses environment variables for its settings. Please update them to your needs.

| name                                      | value                              | example                      | description                                                                                                                                                                                                                                                         |
|-------------------------------------------|------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRYTON_CORE_RABBIT_HOST                   | string                             | 127.0.0.1                    | RabbitMQ server host.                                                                                                                                                                                                                                               |
| CRYTON_CORE_RABBIT_PORT                   | int                                | 5672                         | RabbitMQ server port.                                                                                                                                                                                                                                               |
| CRYTON_CORE_RABBIT_USERNAME               | string                             | admin                        | Username for RabbitMQ server login.                                                                                                                                                                                                                                 |
| CRYTON_CORE_RABBIT_PASSWORD               | string                             | mypass                       | Password for RabbitMQ server login.                                                                                                                                                                                                                                 |
| CRYTON_CORE_DB_HOST                       | string                             | 127.0.0.1                    | Postgres server host.                                                                                                                                                                                                                                               |
| CRYTON_CORE_DB_PORT                       | int                                | 5432                         | Postgres server port.                                                                                                                                                                                                                                               |
| CRYTON_CORE_DB_NAME                       | string                             | cryton                       | Used Postgres database name. **(do not change, if you don't know what you're doing)**                                                                                                                                                                               |
| CRYTON_CORE_DB_USERNAME                   | string                             | cryton                       | Username for Postgres server login.                                                                                                                                                                                                                                 |
| CRYTON_CORE_DB_PASSWORD                   | string                             | cryton                       | Password for Postgres server login.                                                                                                                                                                                                                                 |
| CRYTON_CORE_Q_ATTACK_RESPONSE             | string                             | cryton_core.attack.response  | Queue name for processing attack responses. **(do not change, if you don't know what you're doing)**                                                                                                                                                                |
| CRYTON_CORE_Q_AGENT_RESPONSE              | string                             | cryton_core.agent.response   | Queue name for processing agent responses. **(do not change, if you don't know what you're doing)**                                                                                                                                                                 |
| CRYTON_CORE_Q_EVENT_RESPONSE              | string                             | cryton_core.event.response   | Queue name for processing event responses. **(do not change, if you don't know what you're doing)**                                                                                                                                                                 |
| CRYTON_CORE_Q_CONTROL_REQUEST             | string                             | cryton_core.control.request  | Queue name for processing control requests. **(do not change, if you don't know what you're doing)**                                                                                                                                                                |
| CRYTON_CORE_DEBUG                         | boolean                            | false                        | Make Core run with debug output.                                                                                                                                                                                                                                    |
| CRYTON_CORE_TZ                            | string                             | UTC                          | Internally used timezone. **(do not change, if you don't know what you're doing)**                                                                                                                                                                                  |
| CRYTON_CORE_DEFAULT_RPC_TIMEOUT           | int                                | 120                          | Timeout (in seconds) for RabbitMQ RPC requests.                                                                                                                                                                                                                     |
| CRYTON_CORE_API_SECRET_KEY                | string                             | XF37..56 chars..6HB3         | Key (64 chars) used by REST API for cryptographic signing. More information can be found [here](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key).                                                                                                    |
| CRYTON_CORE_API_PUBLIC_PORT               | int                                | 8000                         | Port on which the Apache reverse proxy will be served (this only affects the *cryton_apache* Compose configuration).                                                                                                                                                |
| CRYTON_CORE_API_ALLOWED_HOSTS             | list of strings separated by space | *                            | Domain names that the site can serve. **(do not change, if you don't know what you're doing)** <br> More information can be found [here](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts).                                                        |
| CRYTON_CORE_API_STATIC_ROOT               | string                             | /var/www/example.com/static/ | Directory for storing static files. **(do not change, if you don't know what you're doing)** <br> More information can be found [here](https://docs.djangoproject.com/en/4.0/ref/settings/#static-root).                                                            |
| CRYTON_CORE_API_USE_STATIC_FILES          | boolean                            | true                         | Whether to serve static files or not. **(do not change, if you don't know what you're doing)**                                                                                                                                                                      |
| CRYTON_CORE_CPU_CORES                     | int                                | 3                            | The maximum number of CPU cores (processes) Cryton Core can utilize. **(do not change/set/export, if you don't know what you're doing)** <br> This affects the speed of starting/consuming Steps/Rabbit requests. Set value to `auto` for the best CPU utilization. |
| CRYTON_CORE_EXECUTION_THREADS_PER_PROCESS | int                                | 7                            | How some payloads or Rabbit's channel consumers should be distributed. **(do not change/set/export, if you don't know what you're doing)** <br> This affects the speed of starting/consuming Steps/Rabbit requests.                                                 |
| CRYTON_CORE_APP_DIRECTORY                 | string                             | ~/.local/cryton-core/        | Path to the Cryton Core directory. **(do not change/set/export, if you don't know what you're doing)** <br> If changed, update the commands in this guide accordingly.                                                                                              |

To save the settings **create an app directory**:
```shell
mkdir ~/.local/cryton-core/
```
The directory will be also used to store logs and other data created by Cryton Core.  
**This doesn't apply to the Docker installation.** It will be available in the same directory as the Dockerfile 
(`/path/to/cryton-core/cryton-core`).

To make the installation easier, we need to set our target version first. Versions can be found [here](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core/-/tags).
Export the $C_VERSION variable to match the desired version:
```shell
export C_VERSION=version
```

Next, we download example settings:
```shell
curl -o ~/.local/cryton-core/.env https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core/-/raw/$C_VERSION/.env
```
Update these settings to your needs.

### Overriding the settings
**NOTICE: This doesn't apply to the Docker Compose installation.**

To override the persistent settings, you can set/export the variables yourself using the **export** command 
(use **unset** to remove the variable). For example:
```shell
export CRYTON_CORE_DEBUG=false
```

## Prerequisites
Install these prerequisites before running Cryton Core. Feel free to use our [Compose configuration](#using-compose-configuration).

- [PostgreSQL database](https://www.postgresql.org/download/) (optionally, use a [Docker image](https://hub.docker.com/_/postgres))
- [RabbitMQ server](https://www.rabbitmq.com/download.html) (optionally, use a [Docker image](https://hub.docker.com/_/rabbitmq))
- [PgBouncer](https://www.pgbouncer.org/install.html) (optionally, use a [Docker image](https://hub.docker.com/r/edoburu/pgbouncer))

### Using Compose configuration
The easiest way to satisfy the prerequisites is to use our predefined Compose configuration. To do so, you need to 
install [Docker Compose](https://docs.docker.com/compose/install/).

Now, continue to the installation, where you'll find a guide on how to install the prerequisites using Compose:

- [using pipx](#installation--using-pippipx-)
- [using Docker Compose](#installation--using-docker-compose-)
- [development](#development)

## Installation (using pip/pipx)
Cryton Core is available in the [PyPI](https://pypi.org/project/cryton-core/) and can be installed using *pip* (`pip install --user cryton-core`). 
However, we **highly recommend** installing the app in an isolated environment using [pipx](https://pypa.github.io/pipx/).

### Requirements
Install the following requirements:
- [Python](https://www.python.org/about/gettingstarted/) >=3.8
- [pipx](https://pypa.github.io/pipx/)

### Install prerequisites for pipx installation using Compose config
**Only perform this step if you want to install the prerequisites mentioned [here](#prerequisites) using Docker Compose.**

First, make sure you have:

- installed [Docker Compose](https://docs.docker.com/compose/install/)
- correctly set the [settings](#settings), you can't change the settings on a running container

To install the prerequisites simply use:
```shell
cd ~/.local/cryton-core/
curl -o ~/.local/cryton-core/docker-compose.prerequisites.yml https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core/-/raw/$C_VERSION/docker-compose.prerequisites.yml
curl -o ~/.local/cryton-core/docker-compose.prerequisites.override.yml https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core/-/raw/$C_VERSION/docker-compose.prerequisites.override.yml
docker compose -f docker-compose.prerequisites.yml -f docker-compose.prerequisites.override.yml up -d --build
```

Update the settings accordingly:
```
CRYTON_CORE_RABBIT_HOST=localhost
CRYTON_CORE_DB_HOST=localhost
CRYTON_CORE_DB_PORT=16432
```

### Installing with pipx
Once you have *pipx* ready on your system, you can start the installation:
```shell
pipx install cryton-core
```

Make sure you've correctly set the [settings](#settings).

If you're not using a reverse proxy, set `CRYTON_CORE_API_USE_STATIC_FILES=false`.

Everything should be set. Check out the [usage section](#usage).

## Installation (using Docker Compose)
Cryton Core can be installed using Docker Compose.

First, we have to clone the repo and switch to the correct version.
```shell
git clone https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core.git
cd cryton-core
git checkout $C_VERSION
```

### Requirements
- [Docker Compose](https://docs.docker.com/compose/install/)

Add yourself to the group *docker*, so you can work with Docker CLI without *sudo*:
```shell
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

### Install prerequisites for Compose deployment using Compose config
**Only perform this step if you want to install the prerequisites mentioned [here](#prerequisites) using Docker Compose.**

First, make sure you have:

- installed [Docker Compose](https://docs.docker.com/compose/install/)
- correctly set the [settings](#settings), you can't change the settings on a running container

To install the prerequisites simply use:
```shell
docker compose -f docker-compose.prerequisites.yml up -d --build
```

Update the settings accordingly:
```
CRYTON_CORE_RABBIT_HOST=cryton_rabbit
CRYTON_CORE_DB_HOST=cryton_pgbouncer
```

### Installing and running with Docker Compose
Make sure you've correctly set the [settings](#settings). You can't change the settings on a running container.

Finally, copy your settings:
```shell
cp ~/.local/cryton-core/.env .env
```

We are now ready to build and start the Core:
```shell
docker compose up -d --build
```

After a while you should see a similar output:
```
[+] Running 6/6                                                                                                                                                                   
 ⠿ Container cryton_rabbit     Started
 ⠿ Container cryton_apache     Started
 ⠿ Container cryton_db         Healthy
 ⠿ Container cryton_pgbouncer  Started
 ⠿ Container cryton_app        Started
 ⠿ Container cryton_listener   Started
```

Everything should be set. Check if the installation was successful and the Core is running by either installing Cryton CLI or testing REST API 
with curl:
```
curl localhost:8000/api/
```

Expected result:
```
{"runs":"http://localhost:8000/cryton/api/v1/runs/","plans":"http://localhost:8000/cryton/api/v1/plans/",
"plan_executions":"http://localhost:8000/cryton/api/v1/plan_executions/","stages":"http://localhost:8000/cryton/api/v1/stages/",
"stage_executions":"http://localhost:8000/cryton/api/v1/stage_executions/","steps":"http://localhost:8000/cryton/api/v1/steps/",
"step_executions":"http://localhost:8000/cryton/api/v1/step_executions/","workers":"http://localhost:8000/cryton/api/v1/workers/"}
```

Docker can sometimes create dangling (`<none>:<none>`) images which can result in high disk space usage. You can remove them using: 
```shell
docker image prune
```

## Development
To install Cryton Core for development, you must install [Poetry](https://python-poetry.org/docs/).

Clone the repository and then go to the correct directory:
```shell
git clone https://gitlab.ics.muni.cz/beast-public/cryton/cryton-core.git
cd cryton-core
```

### Install prerequisites for development using Compose config
**Only perform this step if you want to install the prerequisites mentioned [here](#prerequisites) using Docker Compose.**

First, make sure you have:

- installed [Docker Compose](https://docs.docker.com/compose/install/)
- correctly set the [settings](#settings), you can't change the settings on a running container

To install the prerequisites simply use:
```shell
docker compose -f docker-compose.prerequisites.yml -f docker-compose.prerequisites.override.yml up -d --build
```

Update the settings accordingly:
```
CRYTON_CORE_RABBIT_HOST=localhost
CRYTON_CORE_DB_HOST=localhost
CRYTON_CORE_DB_PORT=16432
```

### Installation and setup with Poetry
Now we can install the project:
```shell
poetry install
```

To spawn a shell use:
```shell
poetry shell
```

Make sure you've correctly set the [settings](#settings).  
To override the settings quickly, you can use this handy one-liner:
```shell
export $(grep -v '^#' .env | xargs)
```

If you're not using a reverse proxy, set `CRYTON_CORE_API_USE_STATIC_FILES=false`.

Everything should be set, check out the [usage section](#usage).

## Usage
**NOTICE: If you're using Docker Compose to install the app, you don't need to migrate the database or start 
the services mentioned in this section.**

Move to the app directory, since some files and directories can be spawned in a relative path
```shell
cd ~/.local/cryton-core/
```

Use the following to invoke the app:
```shell
cryton-core
```

You should see a help page:
```
Type 'cryton-core help <subcommand>' for help on a specific subcommand.

Available subcommands:
...
```

**To learn about each command's options use**:
```shell
cryton-core help <your command>
```

Before we do anything, **we need to migrate the database**:
```shell
cryton-core migrate
```

To be able to use Cryton Core, we need to start the application and its RabbitMQ listener (start each in a separate shell or use the `nohup` command).

First, **start the application**:
```shell
cryton-core runserver 0.0.0.0:8000
```

Use the Gunicorn server for the production deployment:
```shell
cryton-core startgunicorn
```

**Start the RabbitMQ listener**:
```shell
cryton-core startlistener
```

### REST API and control
REST API is the only way to communicate with Cryton Core. It is by default running at 
[http://0.0.0.0:8000](http://0.0.0.0:8000). Interactive documentation can be found at 
[http://0.0.0.0:8000/doc](http://0.0.0.0:8000/doc).

To be able to control Cryton Core, you have to send requests to its REST API. This can be done manually, or via 
[Cryton CLI](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-cli) or 
[Cryton Frontend](https://gitlab.ics.muni.cz/beast-public/cryton/cryton-frontend).

### Execution example
Every Run can be described by a simple formula:
```
Plan template + inventory = Plan instance
Plan instance + Worker = Plan execution
Plan instance + Workers = Run
```

**1. Choose or design plan template**  
Choose one of the YAML plan templates (in the `examples` directory) or design your own.

**2. Create Plan instance**  
Plan templates can utilize a number of variables that need to be provided during the instantiation process. Do this by 
specifying an inventory file.

**3. Create Worker**  
Define Worker(s) that will be used to execute the Plan instance.

**4. Create Run**  
Create a Run by choosing the Plan instance and providing a list of Workers for execution.

**5. Schedule or execute Run**  
You can either schedule Run for a specific date/time, or execute it directly. Run will then be executed on every 
Worker simultaneously.

**6. Read Run Report**  
A report can be generated anytime during the execution (also compliant with YAML format). It contains a list of 
Stages/Steps and their results.

## Rabbit API
Core utilizes RabbitMQ to communicate with its Workers.

It awaits responses on these queues (can be changed environment variables):
- `cryton_core.attack.response`: awaits responses from attack tasks (for example an attack module execution)
- `cryton_core.agent.response`: awaits responses from agent tasks (for example an Empire agent deployment)
- `cryton_core.event.response`: awaits responses from events, that have an influence on Plan execution (for example triggers)
- `cryton_core.control.request`: awaits control requests (for example scheduling tasks in the main scheduler)

More information about the requests themselves can be found in the 
[documentation](https://beast-public.gitlab-pages.ics.muni.cz/cryton/cryton-documentation/).
