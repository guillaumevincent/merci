# Merci

cookiecutter template for docker app :

 * python backend with django rest framework
 * postgresql database
 * javascript frontend with Vuejs + JWT
 * nginx as proxy web


![screenshot](screenshot.png?raw=true "Merci screenshot")

## requirements

 * docker
 * docker-compose
 * python

## install

install cookiecutter

    python -m pip install cookiecutter
    
create your super project

    cookiecutter gh:guillaumevincent/merci

## run

change directory into your project

    cd <project_slug>
    docker-compose up

wait a couple of minute for the install and open [localhost](http://localhost)

## features

### create admin

    docker exec -it <project_slug>_backend_1 bash
    python manage.py createsuperuser
    
### see admin

open [localhost/admin/](http://localhost/admin/)

### see self documented API

open [localhost/api/](http://localhost/api/)