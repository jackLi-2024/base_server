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

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

flask_route = {
    "bp1":
        {
            "API.api_example:TestApi1": "/test/api/v1",
            "API.api_example:TestApi2": "/test/api/v2",
        }
}

flask_settings = {
    "static_url_path": None,
    "static_folder": "static",
    "template_folder": "templates",
    "host": "0.0.0.0",
    "port": 6000,
    "debug": True
}
