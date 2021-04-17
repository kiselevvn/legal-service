DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "constance",
    "constance.backends.database",
    "ckeditor",
    "ckeditor_uploader",
]

PROJECT_APPS = [
    "backend.apps.services",
    "backend.apps.users",
    "backend.apps.news",
    "backend.apps.legal_service",
    "backend.apps.comments",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
