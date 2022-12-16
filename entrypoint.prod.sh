#!/bin/sh

if ["$DATABASE" = "postgres"]
then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

#python manage.py ensure_adminuser \
#      --username=user1 \
#      --email=user1@user.com \
#      --password=user1
#
#python manage.py ensure_adminuser \
#      --username=user2 \
#      --email=user2@user.com \
#      --password=user2

exec "$@"