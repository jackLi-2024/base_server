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

from celery import Celery
from werkzeug.utils import import_string

from webserver_extentions.extention import celeryTask

task = celeryTask.Task(config_name="task.celeryconfig").task_from_config()

@task.task
def test():
    pass

