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
from werkzeug.utils import import_string


def test_flask():
    config = import_string("config")
    run.flask_run(config=config)


if __name__ == '__main__':
    test_flask()
