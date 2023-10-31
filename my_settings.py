import os

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'med_db',
        'USER' : 'root',
        'PASSWORD' : 'snewi832#',
        #'HOST': os.getenv('DB_HOST', 'localhost'),
        'HOST' : 'db',
        'PORT' : '3306',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!q7#u-1tucuqadzf7(z6i&ql#qam$=2x(b4p6%3m2fv%j6&cvq'