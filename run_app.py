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

from webserver_extentions import run
from flask import abort


flaskapp = run.FlaskApp("config")
app = flaskapp.app

if __name__ == '__main__':
    flaskapp.run()
    # flaskapp.aysnc_run()


