"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2h@*khm$wejvlzp_x)*zf1cg2_#0i0ec!$j2v22==-8eccp-$2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'items.apps.ItemsConfig',
    'account.apps.AccountConfig',
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

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# settings.py
AUTH_USER_MODEL = 'account.CUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
 "site_title": "UndrDskM",
 "site_header": "ورود به پنل مدیریت",
 "site_brand": "undrdskm",
 "site_logo": "admin/img/django.png",
 "login_logo": "admin/img/django.png",
 "login_logo_dark": None,
 "site_logo_classes": "img-circle",
 "site_icon": "admin/img/django.png",
 "welcome_sign": "UndrDskM",
 "copyright": "@UndrDskM",
 "search_model": ["auth.User", "shop.ProductModel"],
 "user_avatar": "",
 "topmenu_links": [
     {"name": "خانه", "url": "admin:index", "permissions": ["auth.view_user"]},
     {"model": "auth.User"},
 ],
 "usermenu_links": [],
 "show_sidebar": True,
 "navigation_expanded": False,
 "hide_apps": [],
 "hide_models": [],
 "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
 "custom_links": {
     "books": [{
     "name": "Make Messages",
     "url": "make_messages",
     "icon": "fas fa-comments",
     "permissions": ["books.view_book"]
     }]
 },
 "icons": {
     "auth": "fas fa-users-cog",
     "auth.user": "fas fa-user",
     "auth.Group": "fas fa-users",
 },
 "default_icon_parents": "fas fa-chevron-circle-right",
 "default_icon_children": "fas fa-circle",
 "related_modal_active": True,
 "custom_css": None,
 "custom_js": None,
 "use_google_fonts_cdn": True,
 "show_ui_builder": True,
 "changeform_format": "horizontal_tabs",
 "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
 "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
 "theme": "light",
 "dark_mode_theme": "",
 "navbar_small_text": False,
 "footer_small_text": False,
 "body_small_text": True,
 "brand_small_text": False,
 "brand_colour": False,
 "accent": "accent-primary",
 "navbar": "cyborg",
 "no_navbar_border": False,
 "navbar_fixed": True,
 "layout_boxed": False,
 "footer_fixed": True,
 "sidebar_fixed": True,
 "sidebar": "cyborg",
 "sidebar_nav_small_text": False,
 "sidebar_disable_expand": False,
 "sidebar_nav_child_indent": False,
 "sidebar_nav_compact_style": False,
 "sidebar_nav_legacy_style": False,
 "sidebar_nav_flat_style": False,
 "button_classes": {
     "primary": "btn-primary",
     "secondary": "btn-secondary",
     "info": "btn-info",
     "warning": "btn-warning",
     "danger": "btn-danger",
     "success": "btn-success"
     }
}