import os

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'med_db',
        'USER' : 'root',
        'PASSWORD' : os.environ.get('DB_PASSWORD'),
        #'HOST': os.getenv('DB_HOST', 'localhost'),
        'HOST' : 'db',
        #'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')