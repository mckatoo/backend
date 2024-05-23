from pathlib import Path
from decouple import Csv, config
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DEV_ENV = config("DEV_ENV", cast=bool, default=False)
SECRET_KEY = config("PRIVATE_KEY")

DEBUG = config("DEBUG", cast=bool, default=False)

APPEND_SLASH = False

CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'allauth',
    'allauth.account',
    'allauth.socialaccount.providers.auth0',
    "corsheaders",
    "django_summernote",
    "rest_framework",
    "rest_framework.authtoken",
    "pages.apps.PagesConfig",
    "projects.apps.ProjectsConfig",
    "skills.apps.SkillsConfig",
    "images.apps.ImagesConfig",
    "mailer.apps.MailerConfig",
    "authentication.apps.AuthenticationConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "webapi.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "webapi.wsgi.application"

DATABASES = {
    "default": (
        {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("POSTGRES_DB"),
            "USER": config("POSTGRES_USER"),
            "PASSWORD": config("POSTGRES_PASSWORD"),
            "HOST": config("POSTGRES_HOSTNAME"),
            "PORT": "5432",
        }
        if DEV_ENV==False
        else {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST
EMAIL_HOST = config("SMTP_SERVER_ADDRESS")
EMAIL_PORT = config("SMTP_SERVER_PORT")
EMAIL_HOST_USER = config("SMTP_USERNAME")
EMAIL_HOST_PASSWORD = config("SMTP_PASSWORD")
# EMAIL_SUBJECT_PREFIX = config("EMAIL_SUBJECT_PREFIX")
# EMAIL_USE_LOCALTIME = True
# EMAIL_USE_TLS = config("SMTP_SECURE")
EMAIL_USE_SSL = config("SMTP_SECURE")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    },
    'auth0': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
