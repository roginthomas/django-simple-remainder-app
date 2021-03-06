'''
Production settings

- Set secret key from environment variable
'''

from .common import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['*']

# Configure the production database using dj_database_url
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Address of RedisToGo instance
BROKER_URL = os.environ.get('REDISTOGO_URL')
