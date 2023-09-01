import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_reminder.settings')
celery_app = Celery('birthday_reminder')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
