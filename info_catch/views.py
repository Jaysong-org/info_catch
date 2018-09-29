#!/user/bin/env python3
# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from info_catch.tasks import save_cell_location, save_catch_deviceinfo,save_catch_allinfo
from common.clienttool import ClientTool
import logging

logger = logging.getLogger(__name__)

def test(request):
    logger.info(request.body)
    res = {'code': 200, 'message': 'Success'}
    return HttpResponse(json.dumps(res))

def upload_json_celllocation(request):
    if request.method == 'POST':
        post_body = request.body.decode('utf-8')
        logger.info(post_body)
        if not post_body:
            res = {'returnCode': '000001', 'returnMsg': 'Empty Requet'}
            return HttpResponse(json.dumps(res))
        dict_body = json.loads(post_body)
        print(dict_body)
        if not check_sign(dict_body):
            res = {'returnCode': '000002', 'returnMsg': 'Wrong Sign'}
            return HttpResponse(json.dumps(res))
        dict_args = dict_body['args']

        print(dict_args)
        save_cell_location.delay(dict_args)
        res = {'returnCode': '000000', 'returnMsg': 'Success'}
        return HttpResponse(json.dumps(res))
    else:
        res = {'code': 400, 'message': ' Wrong request Type '}
        json_result = json.dumps(res)
        return HttpResponse(json_result)

def upload_json_deviceinfo(request):
    if request.method == 'POST':
        post_body = request.body.decode('utf-8')
        logger.info(post_body)
        if not post_body:
            res = {'returnCode': '000001', 'returnMsg': 'Empty Requet'}
            return HttpResponse(json.dumps(res))
        dict_body = json.loads(post_body)
        print(dict_body)
        if not check_sign(dict_body):
            res = {'returnCode': '000002', 'returnMsg': 'Wrong Sign'}
            return HttpResponse(json.dumps(res))
        dict_args = dict_body['args']

        print(dict_args)
        save_catch_deviceinfo.delay(dict_args)
        res = {'returnCode': '000000', 'returnMsg': 'Success'}
        return HttpResponse(json.dumps(res))
    else:
        res = {'code': 400, 'message': ' Wrong request Type '}
        json_result = json.dumps(res)
        return HttpResponse(json_result)

def upload_json_allinfo(request):
    if request.method == 'POST':
        post_body = request.body.decode('utf-8')
        logger.info(post_body)
        if not post_body:
            res = {'returnCode': '000001', 'returnMsg': 'Empty Requet'}
            return HttpResponse(json.dumps(res))
        dict_body = json.loads(post_body)
        print(dict_body)
        if not check_sign(dict_body):
            res = {'returnCode': '000002', 'returnMsg': 'Wrong Sign'}
            return HttpResponse(json.dumps(res))
        dict_args = dict_body['args']

        print(dict_args)
        save_catch_allinfo.delay(dict_args)
        res = {'returnCode': '000000', 'returnMsg': 'Success'}
        return HttpResponse(json.dumps(res))
    else:
        res = {'code': 400, 'message': ' Wrong request Type '}
        json_result = json.dumps(res)
        return HttpResponse(json_result)

def check_sign(dict_body):
    ua = dict_body['ua']
    call = dict_body['call']
    sign = dict_body['sign']
    timestamp = dict_body['timestamp']

    data = ua+"&"+call+"&"+str(timestamp)+"&"+'6170702e6c656461696b75616e2e636e'

    md5_data = ClientTool.str_md5(data)

    if sign == md5_data :
        return True
    return False
