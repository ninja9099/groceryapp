import os

from groceryapp.settings import LOG_DIR

DEBUG = False
ALLOWED_HOSTS = ['www.example.com']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# production database  settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'groceryapp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': ''
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.abspath(os.path.join(LOG_DIR, "app.log")),
            'maxBytes': 5*1024*1024,
            'backupCount': 20,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARN',
            'propagate': False,
        },
        'main': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        }
    }
}
print(f"{'_'* 10} Production settings in use {'_'*10}")
