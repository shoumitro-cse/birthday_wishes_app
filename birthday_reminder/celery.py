import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_reminder.settings')
celery_app = Celery('birthday_reminder')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# celery_app.conf.beat_schedule = {
#     'send-birthday-emails': {
#         'task': 'customers.tasks.send_birthday_emails',
#         'schedule': crontab(hour=7, minute=39),
#     },
# }
