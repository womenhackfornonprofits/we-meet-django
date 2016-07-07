import os
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# Application definition
HTML_MINIFY = True

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False # Timezone support not needed

 TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
- 'DIRS': [],
+ 'DIRS': [
+ os.path.join(BASE_DIR, 'london_cafes/templates')
+ ],
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
WSGI_APPLICATION = 'london_cafes.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'london_cafes',
}
