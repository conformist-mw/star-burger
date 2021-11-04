from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    'rest_framework',
    'phonenumber_field',
]

PROJECT_APPS = [
    'foodcartapp.apps.FoodcartappConfig',
    'places.apps.PlacesConfig',
    'restaurateur.apps.RestaurateurConfig',
]

INSTALLED_APPS = DEFAULT_APPS + THIRDPARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS.extend([
        'debug_toolbar',
    ])
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

ROOT_URLCONF = 'star_burger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'star_burger.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DATABASES = {'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite')}

password_validation = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{password_validation}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{password_validation}.MinimumLengthValidator',
    },
    {
        'NAME': f'{password_validation}.CommonPasswordValidator',
    },
    {
        'NAME': f'{password_validation}.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INTERNAL_IPS = ['127.0.0.1', 'localhost']

STATICFILES_DIRS = [
    BASE_DIR / 'assets',
    BASE_DIR / 'frontend' / 'bundles',
]

YANDEX_GEO_API_KEY = env('YANDEX_GEO_API_KEY')
