LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(name)s-%(levelname)s [%(filename)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'service': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'service.log',
            'formatter': 'verbose'
        },
        'auth_uuid': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'auth.log',
            'formatter': 'verbose'
        },
        'mails': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'mails.log',
            'formatter': 'verbose'
        },
        'celery': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'celery.log',
            'formatter': 'verbose',
        },
        'metric': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'metric.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_log': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'service': {
            'handlers': ['service'],
            'level': 'INFO',
            'propagate': True,
        },
        'auth_uuid': {
            'handlers': ['auth_uuid'],
            'level': 'INFO',
            'propagate': True,
        },
        'mails': {
            'handlers': ['mails'],
            'level': 'INFO',
            'propagate': True,
        },
        'celery-task': {
            'handlers': ['celery', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'metric': {
            'handlers': ['metric', 'celery', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
