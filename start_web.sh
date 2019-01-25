#!/bin/bash

python3 manage.py makemigrations selenium_view
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 manage.py shell
python3 manage.py runserver 0.0.0.0:8000
