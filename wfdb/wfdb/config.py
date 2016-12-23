from datetime import timedelta
from celery.schedules import crontab
class Config(object):
    SECRET_KEY = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    DEBUG = False
    WTR_CSRF_ENABLED = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    DEBUG = True
    CACHE_TYPE = 'simple'
    ASSETS_DEBUG = True
    MAIL_SERVER = 'vinagreira.uft.edu.br'
    MAIL_PORT = 25
    MAIL_USERNAME = 'naoresponder@dti.uftedu.br'
    MAIL_PASSWORD = '45F/#A(4'

    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_BACKEND_URL = "redis://localhost:6379/0"

    CELERYBEAT_SCHEDULE = {
        'echo-every-5-seconds': {
            'task': 'wfdb.tasks.echo',
            'schedule': timedelta(seconds=5),
            'args':("Hello World!!",)
        },
        'echo-crontab': {
            'task': 'wfdb.tasks.echo',
            'schedule': crontab(hour='15, 16, 17',minute='*/15'),
            'args':("Hello World!!",)
        },
        'digest-every-sunday': {
            'task': 'wfdb.tasks.digest',
            'schedule': crontab(day_of_week=6, hour=23, minute=30),
            'args':("Hello World!!",)
        },
        
    }
#schedule: hours=,minutes, seconds

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True
    CACHE_TYPE = 'null'
    WTR_CSRF_ENABLED = False
    