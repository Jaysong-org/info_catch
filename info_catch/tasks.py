#!/usr/bin/env python3
# encoding: utf-8
# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from common.clienttool import ClientTool
import logging

logger = logging.getLogger(__name__)

#@shared_task(name='info_catch.tasks.save_cell_location', routing_key='test', queue='test')
def save_cell_location(cell_location):
    logger.info(cell_location)
    es = ClientTool.get_es_client()
    ret = es.index(index='cell_location_test', doc_type='cell_location_test', body=cell_location)
    logger.info(ret)
    return 1

@shared_task(name='info_catch.tasks.save_catch_deviceinfo', routing_key='catch_deviceinfo', queue='catch_deviceinfo')
def save_catch_deviceinfo(catch_deviceinfo):
    logger.info(catch_deviceinfo)
    es = ClientTool.get_es_client()
    ret = es.index(index='catch_deviceinfo', doc_type='catch_deviceinfo', body=catch_deviceinfo)
    logger.info(ret)
    return 1

@shared_task(name='info_catch.tasks.save_catch_allinfo', routing_key='catch_allinfo', queue='catch_allinfo')
def save_catch_allinfo(catch_allinfo):
    logger.info(catch_allinfo)
    es = ClientTool.get_es_client()
    ret = es.index(index='catch_allinfo', doc_type='catch_allinfo', body=catch_allinfo)
    logger.info(ret)
    return 1
