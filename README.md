# Warehouse.Uz

## Quick start
```shell
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec app python manage.py makemigrations # run this only if you change database
$ docker-compose exec app python manage.py migrate
$ docker-compose exec app python manage.py createsuperuser
```

## Installation

First, [install Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/). If you're new to Docker, you might also want to check out the [Hello, world! tutorial](https://docs.docker.com/userguide/dockerizing/).

Next, clone this repo:
```shell
$ git clone https://github.com/KhasanovR/Warehouse-System-Api.git
$ cd Warehouse-System-Api
```

## Configuration

First, [install Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/). If you're new to Docker, you might also want to check out the [Hello, world! tutorial](https://docs.docker.com/userguide/dockerizing/).

Next, clone this repo:
```dotenv
DOCKER_REPOSITORY={{your DOCKER_REPOSITORY}}
DOCKER_APP_VERSION={{your version}}
POSTGRES_USER={{your db user}}
POSTGRES_DB={{your db}}
POSTGRES_PASSWORD={{your db password}}
PRODUCTION_HOST={{your HOST}}
DEBUG=True(optional)
SECRET_KEY={{your secret key}}
ALLOWED_HOSTS={{your allowed host list(e.g.: localhost,127.0.0.1}}
MEDIA_URL=/media/
DATABASE_URL={{your db url}}
GUNICORN_WORKERS=1
```
