#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json

from webserver_extentions.common.log import get_log

logging = get_log("conf/logging.conf")

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

from flask_restful import Resource
from flask import request

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/../API/" % cur_dir)

from tasks import test


class TestApi1(Resource):
    def get(self, id):
        arg = request.args
        result = test(id, 3)
        return {"id": id, "sum(id + 3)": result}

    def deal(self, params):
        return params


class TestApi2(Resource):
    def get(self):
        logging.error("hahah")
        return {"result": "I am api_2"}
