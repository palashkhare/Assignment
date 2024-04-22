#! /bin/bash

docker run \
    -e POSTGRES_DB="anz_db" \
    -e POSTGRES_USER="test_user" \
    -e POSTGRES_PASSWORD="psw12345" \
    -p 5430:5432 \
    -v /home/kanika/workspace/anzBooks/tmp/dbFiles:/var/lib/postgresql/data \
    -d postgres:14