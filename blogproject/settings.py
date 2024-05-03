
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f2y53mk$^$0aqt$w+51n_am15^y@)q69$+7d=cx=#s8m@24s=m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp',

    "crispy_forms",
    "crispy_bootstrap4",

    # The following apps are required for allauth:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
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

AUTHENTICATION_BACKENDS = [
 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


#EMAIL_BACKEND ='django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = BASE_DIR / 'emails'

#ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True # This option allows you to set whether the email address should be verified to register
ACCOUNT_EMAIL_VERIFICATION = 'optional' # This option can be used to set whether an email verification is necessary for a user to log in after he registers an account. You can also set none to send no verification email. (Not Recommended)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
#ACCOUNT_RATE_LIMITS  = 5 # The maximum number of login attempts can be set, and the user gets blocked from logging back in until a timeout
#ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT= 86400 # 1 day in seconds
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 # Sets the number of days within which an account should be activated. 
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
#ACCOUNT_SESSION_REMEMBER = None
#ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
#ACCOUNT_TEMPLATE_EXTENSION = "html"
ACCOUNT_UNIQUE_EMAIL = True
#ACCOUNT_SIGNUP_FORM_CLASS = 'blogapp.forms.SignupForm'
#ACCOUNT_USER_MODEL_USERNAME_FIELD = True
ACCOUNT_EMAIL_NOTIFICATIONS = True

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'  # default to /accounts/profile 
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'

#email setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #new
EMAIL_HOST = 'smtp.gmail.com' #new
EMAIL_PORT = 465 #new
EMAIL_HOST_USER = 'charlespeter142@gmail.com'  #new
EMAIL_HOST_PASSWORD = "isvm sipz kgsy pjwc" #new
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

'''ACCOUNT_FORMS = {
'signup': 'blogapp.forms.CustomSignupForm',
}'''

#ACCOUNT_ADAPTER='blogapp.adapter.RestrictEmailAdapter'
#ACCOUNT_ADAPTER = 'blogapp.adapter.UsernameMaxAdapter'


'''ACCOUNT_FORMS = {
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'login': 'allauth.account.forms.LoginForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'allauth.account.forms.SignupForm',
    'user_token': 'allauth.account.forms.UserTokenForm',

    "signup": "blogapp.users.forms.CustomSignupForm",
}'''
