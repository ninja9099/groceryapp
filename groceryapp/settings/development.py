import os

from groceryapp.settings import LOG_DIR

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

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


# logging  while in development
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
print(f"{'_'* 10} Development settings in use {'_'*10}")