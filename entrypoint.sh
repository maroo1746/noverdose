#!/bin/bash

python manage.py migrate

from django.contrib.auth.models import User
if User.objects.filter(username='admin').exists():
    user = User.objects.get(username='admin')
    user.set_password('noverdose123')
    user.email = 'seoyeong4700@gmail.com'
    user.save()
else:
    User.objects.create_superuser('admin', 'seoyeong4700@gmail.com', 'noverdose123')