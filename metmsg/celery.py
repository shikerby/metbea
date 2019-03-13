from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import solar
from celery.schedules import crontab
from celery.schedules import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metmsg.settings')

app = Celery('metmsg')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'add-every-30-seconds': {
            "task": "blog.tasks.update_post_status",
            "schedule":timedelta(seconds=30),
            "args": (),
        },
        # 'add-every-monday-morning': {
        #     'task': 'demoapp.tasks.mul',
        #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
        #     'args': (2, 5),
        # },
        # 下面的这个根据经纬度,太阳日出日落等等来定时, 似乎不好永,会引发错误
        # 'add-at-melbourne-sunset': {
        #     'task': 'tasks.add',
        #     'schedule': solar('sunset', -37.81753, 144.96715),
        #     'args': (16, 16),
        # },
    }
)