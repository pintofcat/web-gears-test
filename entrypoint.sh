#!/bin/bash
set -e


up_monolith_backend () {
 python manage.py runserver 0.0.0.0:8000
}


case "$1" in
  up_monolith_backend) "$@"; exit;;
  *) exec "$@"; exit;;
esac
