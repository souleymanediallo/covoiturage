from pathlib import Path
import environ


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)

if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / ".env"))


SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'blog.apps.BlogConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'trips.apps.TripsConfig',
    'homework.apps.HomeworkConfig',
    'phonenumber_field',
    'conversations.apps.ConversationsConfig',
    'cars.apps.CarsConfig',
    'contact.apps.ContactConfig',
    'covoiturages.apps.CovoituragesConfig',
    'aftu.apps.AftuConfig',
    'cities.apps.CitiesConfig',
    'storages',
    'crispy_forms',
    'django_ckeditor_5',
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

# --- CKEditor 5 ---
CKEDITOR_5_FILE_UPLOAD_PATH = "uploads/blog/"  # dossier des uploads
CKEDITOR_5_UPLOAD_FILE_TYPES = [  # types autorisés
    "jpeg", "jpg", "png", "gif", "bmp", "webp", "tiff", "svg", "pdf"
]

CKEDITOR_5_CONFIGS = {
    "blog_ckeditor": {  # <<— la config attendue par ton champ
        "language": "fr",
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "link", "|",
            "bulletedList", "numberedList", "todoList", "|",
            "blockQuote", "horizontalLine", "insertTable", "|",
            "imageUpload", "mediaEmbed", "|",
            "undo", "redo", "|",
            "sourceEditing"
        ],
        # Titres disponibles
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraphe", "class": "ck-heading_paragraph"},
                {"model": "heading2", "view": "h2", "title": "Titre 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Titre 3", "class": "ck-heading_heading3"},
                {"model": "heading4", "view": "h4", "title": "Titre 4", "class": "ck-heading_heading4"},
            ]
        },
        # Outils de tableau (insérer/supprimer lignes/colonnes, fusion…)
        "table": {
            "contentToolbar": [
                "tableColumn", "tableRow", "mergeTableCells",
                "tableCellProperties", "tableProperties"
            ]
        },
        # Outils d’image (alignements, alt, légende…)
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "toggleImageCaption",
                "imageStyle:inline", "imageStyle:block",
                "imageStyle:side"
            ]
        },
        # Prévisualisation des médias embarqués
        "mediaEmbed": {"previewsInData": True},

        # (facultatif) Autoriser du HTML personnalisé — attention sécurité
        # "htmlSupport": { "allow": [ {"name": r".*", "attributes": True, "classes": True, "styles": True} ] },
    },
}

# Custom user model
AUTH_USER_MODEL = "accounts.CustomUser"

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL", default="postgres:///covoiturage")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# createdb covoiturage
# dropdb covoiturage

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurations AWS S3
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# Local development settings (optional)
if env('DJANGO_DEVELOPMENT') == 'True':
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / "mediafiles"
else:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-3'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
    AWS_DEFAULT_ACL = None

    # Static files (CSS, JavaScript, Images)
    STATICFILES_STORAGE = 'utils.storages.StaticRootS3Boto3Storage'
    STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"

    # Media files
    DEFAULT_FILE_STORAGE = 'utils.storages.MediaRootS3Boto3Storage'
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"


LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "login"

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

CRISPY_TEMPLATE_PACK = 'bootstrap4'