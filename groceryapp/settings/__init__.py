import os
from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)

if os.environ.get('DJANGO_DEVELOPMENT'):
   from .development import *
else:
   from .production import *
