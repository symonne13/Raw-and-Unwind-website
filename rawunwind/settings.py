from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-development-only-key"
)

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://raw-and-unwind-website.vercel.app",
]
# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "ckeditor",
    "ckeditor_uploader",

    "app",
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = "rawunwind.urls"


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = "rawunwind.wsgi.application"


# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=True,
    )
}

# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]

# WhiteNoise configuration
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ============================================================
# CLOUDINARY
# ============================================================

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
}
# ============================================================
# CKEDITOR
# ============================================================

CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"

CKEDITOR_CONFIGS = {
    "default": {

        # ----------------------------------------------------
        # TOOLBAR
        # ----------------------------------------------------

        "toolbar": "Custom",

        "toolbar_Custom": [
            ["Styles", "Format", "Font", "FontSize"],

            ["Bold", "Italic", "Underline", "Strike"],

            ["TextColor", "BGColor"],

            [
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],

            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
            ],

            ["Link", "Unlink", "Anchor"],

            ["Image", "Table", "HorizontalRule"],

            ["Blockquote", "CodeSnippet"],

            ["RemoveFormat", "Source"],

            ["Maximize"],
        ],


        # ----------------------------------------------------
        # PLUGINS
        # ----------------------------------------------------

        "extraPlugins": ",".join([
            "image2",
            "codesnippet",
            "justify",
            "autogrow",
            "uploadimage",
        ]),

        "removePlugins": "image",


        # ----------------------------------------------------
        # IMAGE SETTINGS
        # ----------------------------------------------------

        "image2_alignClasses": [
            "image-left",
            "image-center",
            "image-right",
        ],

        "image2_disableResizer": False,


        # ----------------------------------------------------
        # CONTENT CONTROL
        # ----------------------------------------------------

        "allowedContent": True,

        "disallowedContent": "script; *[on*]",

        "forcePasteAsPlainText": True,


        # ----------------------------------------------------
        # TYPOGRAPHY
        # ----------------------------------------------------

        "font_names": (
            "Inter/Inter, sans-serif;"
            "Playfair Display/Playfair Display, serif;"
            "Montserrat/Montserrat, sans-serif;"
            "Arial/Arial, Helvetica, sans-serif;"
            "Georgia/Georgia, serif"
        ),

        "fontSize_sizes": (
            "12/12px;"
            "14/14px;"
            "16/16px;"
            "18/18px;"
            "20/20px;"
            "24/24px;"
            "32/32px"
        ),


        # ----------------------------------------------------
        # AUTO GROW
        # ----------------------------------------------------

        "autoGrow_minHeight": 300,

        "autoGrow_maxHeight": 900,

        "autoGrow_bottomSpace": 50,


        # ----------------------------------------------------
        # UI
        # ----------------------------------------------------

        "height": 400,

        "width": "100%",

        "skin": "moono-lisa",


        # ----------------------------------------------------
        # CODE SNIPPET
        # ----------------------------------------------------

        "codeSnippet_theme": "monokai",


        # ----------------------------------------------------
        # PASTE CLEANUP
        # ----------------------------------------------------

        "pasteFromWordRemoveStyles": True,

        "pasteFromWordRemoveFontStyles": True,
    }
}


# ============================================================
# JAZZMIN ADMIN SETTINGS
# ============================================================

JAZZMIN_SETTINGS = {

    # --------------------------------------------------------
    # SITE IDENTITY
    # --------------------------------------------------------

    "site_title": "Raw Unwind Admin",

    "site_header": "Raw Unwind Admin",

    "site_brand": "Raw Unwind",

    "welcome_sign": "Welcome to Raw Unwind Admin",

    "copyright": "© 2025 Raw Unwind",


    # --------------------------------------------------------
    # LOGOS
    # --------------------------------------------------------

    "login_logo": "images/logo.png",

    "site_icon": "images/logo.png",


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    "search_model": [
        "auth.User",
        "auth.Group",
    ],


    # --------------------------------------------------------
    # TOP MENU
    # --------------------------------------------------------

    "topmenu_links": [
        {
            "name": "Dashboard",
            "url": "admin:index",
        },

        {
            "model": "auth.User",
        },

        {
            "model": "auth.Group",
        },
    ],


    # --------------------------------------------------------
    # USER MENU
    # --------------------------------------------------------

    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://example.com/support",
            "new_window": True,
        },
    ],


    # --------------------------------------------------------
    # ICONS
    # --------------------------------------------------------

    "icons": {
        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",
    },


    # --------------------------------------------------------
    # UI BEHAVIOR
    # --------------------------------------------------------

    "show_ui_builder": True,

    "related_modal_active": True,

    "language_chooser": False,


    # --------------------------------------------------------
    # DEFAULT ICONS
    # --------------------------------------------------------

    "default_icon_parents": (
        "fas fa-chevron-circle-right"
    ),

    "default_icon_children": "fas fa-circle",


    # --------------------------------------------------------
    # CUSTOM CSS
    # --------------------------------------------------------

    "custom_css": "css/admin_custom.css",
}


# ============================================================
# JAZZMIN UI TWEAKS
# ============================================================

JAZZMIN_UI_TWEAKS = {

    # --------------------------------------------------------
    # THEME & FONTS
    # --------------------------------------------------------

    "theme": "flatly",

    "dark_mode_theme": "darkly",

    "font": "Roboto",


    # --------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------

    "layout_boxed": False,

    "fixed_sidebar": True,

    "fixed_navbar": True,

    "fixed_footer": False,


    # --------------------------------------------------------
    # TEXT SIZES
    # --------------------------------------------------------

    "body_small_text": False,

    "footer_small_text": False,

    "brand_small_text": False,

    "navbar_small_text": False,

    "sidebar_nav_small_text": False,


    # --------------------------------------------------------
    # NAVBAR
    # --------------------------------------------------------

    "navbar": "navbar-success navbar-dark",

    "no_navbar_border": False,


    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    "sidebar": "sidebar-dark-success",

    "brand_colour": "navbar-success",

    "accent": "accent-success",


    # --------------------------------------------------------
    # SIDEBAR BEHAVIOR
    # --------------------------------------------------------

    "sidebar_nav_flat_style": True,

    "sidebar_nav_child_indent": True,

    "sidebar_disable_expand": False,


    # --------------------------------------------------------
    # BUTTONS
    # --------------------------------------------------------

    "button_classes": {
        "primary": "btn btn-success",

        "secondary": "btn btn-outline-success",

        "info": "btn btn-outline-success",

        "warning": "btn btn-warning",

        "danger": "btn btn-danger",

        "success": "btn btn-success",
    },
}


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"