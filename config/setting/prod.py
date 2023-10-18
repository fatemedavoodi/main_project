from config.settings import *

SECRET_KEY = 'django-insecure-fn9&719gwc(cm$2f0s(w_-do&p^cyje%4l-ig#lhr6wm-oxnnz'
DEBUG = False

ALLOWED_HOSTS = ['projectdjango.ir','www.projectdjango.ir']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


#STATIC_ROOT = BASE_DIR/'/static'
#MEDIA_ROOT = BASE_DIR/'media'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.projectdjango.ir'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'admin@projectdjango.ir'
EMAIL_HOST_PASSWORD = '096165976Fd*'
DEFAULT_FROM_EMAIL = 'admin@projectdjango.ir'



CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)