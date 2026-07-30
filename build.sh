#!/usr/bin/env bash

set -o errexit

npm install
npm run build
python manage.py collectstatic --no-input
python manage.py migrate