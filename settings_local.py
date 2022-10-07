from .settings import *
import os

# place to the settings dir override default settings for dev

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['django_extensions']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'


# for jupyter
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

NOTEBOOK_ARGUMENTS = ['--ip', '0.0.0.0', '--port', '8888', '--notebook-dir', 'jupyter']
IPYTHON_KERNEL_DISPLAY_NAME = 'Django Kernel'

# 只在终端起作用，jupyter里面无效
SHELL_PLUS_PRINT_SQL = True


# Email server configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = ''
# EMAIL_HOST_USER = ''
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
