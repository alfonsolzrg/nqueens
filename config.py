import logging
import sys

from os import environ


logger = logging.getLogger('default')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Here goes all project-related config
CONFIG = {
  'DB_USERNAME': environ.get('DB_USERNAME'),
  'DB_PASSWORD': environ.get('DB_PASSWORD'),
  'DB_HOST': environ.get('DB_HOST'),
  'DB_NAME': environ.get('DB_NAME'),
}