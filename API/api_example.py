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


class TestApi1(Resource):
    def get(self, id):
        return id

    def deal(self, params):
        return params


class TestApi2(Resource):
    def get(self):
        logging.error("hahah")
        return {"result": "I am api_2"}
