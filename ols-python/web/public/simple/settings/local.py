import json
import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

from .base import *

# FUNCION PARA LEER EL ARCHIVO PRIVATE
with open(PRIVATE_DIR / 'secret.json') as f:
    secret = json.loads(f.read())

#FUNCIÓN PARA LEER VARIABLES DEL ARCHIVO PRIVATE
def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg= "la variable %s no existe " % secret_name
        raise ImproperlyConfigured(msg) 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SQLLITE3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MYSQL DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': get_secret("DB_NAME"),
#         'USER': get_secret("DB_USER"),
#         'PASSWORD': get_secret("DB_PASS"),
#         'HOST': get_secret("DB_HOST"),
#         'PORT': get_secret("DB_PORT"),
#     }
# }


########################################################
# AWS SETTINGS FILES
# AWS_ACCESS_KEY_ID = get_secret("S3_KEY_ID")
# AWS_SECRET_ACCESS_KEY = get_secret("S3_SECRET_KEY")
# AWS_STORAGE_BUCKET_NAME = 'gabitex'
# AWS_S3_ENDPOINT_URL = 'https://fr-par-1.linodeobjects.com'
# AWS_DEFAULT_ACL = None
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.fr-par-1.linodeobjects.com'

########################################################
# STATIC FILES (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# EN EL MISMO SERVIDOR (carpeta static del sistema)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# Cuando desplegamos en servidor de producción (Debug = False)
# Comando: python3 manage.py collectstatic
# STATIC_ROOT = BASE_DIR / 'staticfiles' 

# MEDIANTE S3
# AWS_STATIC_LOCATION = 'localhost/static'
# STATICFILES_STORAGE = 'gabitex.storage.StaticStorage'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'


########################################################
# MEDIA FILES
# GESTIÓN DE ARCHIVOS NO DEL SISTEMA

# EN EL MISMO SERVIDOR (carpeta media del sistema)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
# A través de almacenaje S3
# S3 MEDIA PUBLIC SETTINGS (SI QUERESMOS QUE TODO EL MUNDO SE TENGA ACCESO)
# AWS_MEDIA_LOCATION = 'localhost/media'
# DEFAULT_FILE_STORAGE = 'gabitex.storage.PublicMediaStorage'
# S3 MEDIA PRIVATE SETTINGS (SI QUEREMOS RESTRINGIR EL ACCESO)
# PRIVATE_FILE_STORAGE = 'gabitex.storage.PrivateMediaStorage'
# S3 MEDIA BASE URL
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'

########################################################
# EMAIL MANAGEMENT
# SI LOS QUEREMOS GUARDAR EN UNA CARPETA
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "_emails"

# SI LOS QUEREMOS QUEREMOS ENVIAR A TRAVÉS DE UN SERVIDOR DE SMTP
# EMAIL_HOST = 'mail.smtp2go.com'
# EMAIL_PORT = '2525'
# EMAIL_HOST_USER = '15114.net'
# EMAIL_HOST_PASSWORD = ''



########################################################
# Internationalization and language support
# https://docs.djangoproject.com/en/4.2/topics/i18n/
USE_I18N = True
LANGUAGE_CODE = 'en-us'

# LANGUAGES = (
#     ('es-es', _('Spanish')),
#     ('en-us', _('English')),
# )

# Contains the path list where Django should look into for django.po files for all supported languages
# LOCALE_PATHS =  [ BASE_DIR / "locale" ]



########################################################
# TIMEZONE CONFIGURATION 
TIME_ZONE = 'Europe/Madrid'
USE_TZ = True

########################################################
# FORMAT TIMES CONFIGURATION
# USE_L10N = False
# DATE_INPUT_FORMATS = ['%d-%m-%Y']  
# TIME_INPUT_FORMATS = ['%H:%M:%S']
# DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%M:%S']


########################################################
# CONFIG SESSION COOKIE AND RESET PASSWORD
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_COOKIE_AGE = 7 * 24 * 60 * 60
# PASSWORD_RESET_TIMEOUT = 20 * 60
