#!/bin/bash
set -e

psql \
  --set ENVSCHEMA=$ENVSCHEMA \
  -v ON_ERROR_STOP=1 \
  --username "$POSTGRES_USER" \
  --dbname "$POSTGRES_DB" \
  -a -f /db/scripts/init.sql
