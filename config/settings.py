"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import pymysql
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tvtqncq4dc@na5(qz0=tu#=dfp8^i%aivz*j2t%4a%x7o^+6ja'

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
    'shop',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.naver',
    'cart',
    'coupon',
    'order',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases기

#장고랑 호환되게 버젼 맞춰주
pymysql.version_info=(1,4,2,"final",0)
pymysql.install_as_MySQLdb()

from password import dbpassword
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'onlineshop.cybfeux9ym55.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'onlineshop',
        'USER':'admin',
        'PASSWORD':dbpassword,
        'PORT':'3306',

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID=1
#장고 컨트립 사이트 1번 인스턴스 정보를가져와 쓴다.
LOGIN_REDIRECT_URL ='/'

from password import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'onlineshop-static-hyunsik'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_FILE_OVERWRITE =False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400',
}
#안쓰면 파일 외부접근 안될수있
AWS_DEFAULT_ACL='public-read'
AWS_LOCATION='static'
STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'#장고에서 S3 연결
DEFAULT_FILE_STORAGE='config.s3media.MediaStorage'#장고에서 S3 연결

CART_ID='cart_item'
from password import IAMPORT_KEY,IAMPORT_SECRET
IAMPORT_KEY=IAMPORT_KEY
IAMPORT_SECRET=IAMPORT_SECRET

# 별도의 static file root 추가
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')

]