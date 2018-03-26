import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ['DEBUG'] == 'True' # environment vars are strings. "convert" to boolean. lol, Python
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'medi-shop-198920.appspot.com', # must add the app engine (project-id) domain here
    '127.0.0.1', # for local testing 
]

INSTALLED_APPS = [
    'shop_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls' # root is the directory where this settings.py file is
WSGI_APPLICATION = 'root.wsgi.application'

TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [os.path.join(BASE_DIR, 'templates')], # global templates directory (in root directory where manage.py is)
      'APP_DIRS': True,
      'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
      },
    },
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'HOST': os.environ['DB_HOST'],
      'PORT': os.environ['DB_PORT'],
      'NAME': os.environ['DB_NAME'],
      'USER': os.environ['DB_USER'],
      'PASSWORD': os.environ['DB_PASSWORD']
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# BUCKET-NAME is the name of the Google Cloud Storage bucket you created for your project
STATIC_URL = os.environ['STATIC_URL']

# collectstatic directory (located OUTSIDE the base directory so that it is not deployed directly)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'bucket_static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # static directory for local testing
]