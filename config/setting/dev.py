from config.settings import *

SECRET_KEY = 'django-insecure-fn9&719gwc(cm$2f0s(w_-do&p^cyje%4l-ig#lhr6wm-oxnnz'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR/'/static'
MEDIA_ROOT = BASE_DIR/'media'
STATICFILES_DIRS =[
    BASE_DIR/'static',
    BASE_DIR/'media',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'