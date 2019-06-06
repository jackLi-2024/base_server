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

from webserver_extentions.extention import celeryTask
from webserver_extentions.common.log import get_log

logging = get_log("conf/logging.conf")
task = celeryTask.Task(config_name="conf.celeryconfig").task_from_config()


@task.task
def test(a, b):
    return a + b
