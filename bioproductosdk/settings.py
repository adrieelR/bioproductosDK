from pathlib import Path
import dj_database_url
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIRS = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$ju%-c914jlm7pxha=j#xma&##!y^^yj9ov)ffl-oaat1oh052'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

CSRF_TRUSTED_ORIGINS = []
if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'online',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bioproductosdk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'online.context_processors.carrito_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'bioproductosdk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'test_db.sqlite3',
        }
    }
    #LINEA MODIFICADA
elif os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True,
        )
    }
    #
else:
    DATABASES = {
    "default":{
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bioproductos",
        "USER": "postgres",
        "PASSWORD":"adrieel",
        "HOST":"localhost",
        "PORT":"5432",
    }
}

"""
# ============================================================
# CONFIGURACIÓN ALTERNATIVA: MongoDB (deshabilitada)
# ============================================================
# Opción A: django-mongodb-backend (backend oficial de MongoDB)
# Instalación: pip install django-mongodb-backend
# Requiere Django 5.x y reemplaza la configuración de PostgreSQL.
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django_mongodb_backend",
#         "NAME": "bioproductosdk",
#         "HOST": "mongodb://localhost:27017",
#         # Para MongoDB Atlas:
#         # "HOST": "mongodb+srv://usuario:password@cluster.mongodb.net/",
#     }
# }
#
# DEFAULT_AUTO_FIELD = "django_mongodb_backend.fields.ObjectIdAutoField"

# ------------------------------------------------------------
# Opción B: Djongo
# Instalación: pip install djongo
# Compatible solo con versiones antiguas de Django (3.x).
#
# DATABASES = {
#     "default": {
#         "ENGINE": "djongo",
#         "NAME": "bioproductosdk",
#         "ENFORCE_SCHEMA": False,
#         "CLIENT": {
#             "host": "localhost",
#             "port": 27017,
#             "username": "tu_usuario",
#             "password": "tu_contraseña",
#             "authSource": "admin",
#             "authMechanism": "SCRAM-SHA-1",
#         },
#     }
# }
"""
    

# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'

# LINEAS MODIFICADAS
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGE = {
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    }
}
#
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'inicio'

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
