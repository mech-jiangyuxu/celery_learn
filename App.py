# -*- coding: utf-8 -*-
"""
@Auth ： 江宇旭
@Email ：jiang.yuxu@mech-mind.net
@Time ： 2023/2/28 13:21
"""

from celery import Celery
from task import AddTask

app = Celery()

app.config_from_object('celeryconfig')  # 只要在当前目录中有celeryconfig.py模块就可以加载

app.task.register(AddTask())

if __name__ == '__main__':
    app.start()
