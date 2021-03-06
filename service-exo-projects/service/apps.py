# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'auth_uuid.apps.AuthConfig',
    'rest_framework',
    'health_check',
    'corsheaders',
    'django_celery_results',
    'django_extensions',
    'reversion',
    'populate',
    'exo_changelog',
    'guardian',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'drf_yasg',
    'actstream',
    'typeform_feedback',
    'exo_role',
    # Local apps,
    'project',
    'assignment',
    'data',
    'learning',
    'team',
    'communication',
    'opportunities',
    'utils',
    'files',
    'typeform',
    'ratings',
    'jobs',
    'dj_anonymizer',
]
