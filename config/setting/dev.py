from config.settings import *

SECRET_KEY = 'django-insecure-(5#nlrsms#c1$pczb$)1#m%ugf)ragb!6zp9ydf4yd#i^-p^3='
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