#!/usr/bin/env python3
# encoding: utf-8
#目的是拒绝隐士引入，celery.py和celery冲突。
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Exchange,Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'info_catch.settings')

app = Celery('info_catch')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

default_exchange = Exchange('default', type='direct')
#cell_location_exchange = Exchange('cell_location', type='direct')
catch_deviceinfo_exchange = Exchange('catch_deviceinfo', type='direct')
catch_allinfo_exchange = Exchange('catch_allinfo', type='direct')

app.conf.task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    #Queue('cell_location', cell_location_exchange, routing_key='cell_location'),
    Queue('catch_deviceinfo', catch_deviceinfo_exchange, routing_key='catch_deviceinfo'),
    Queue('catch_allinfo', catch_allinfo_exchange, routing_key='catch_allinfo'),
)


app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))