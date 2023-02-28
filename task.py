# -*- coding: utf-8 -*-
"""
@Auth ： 江宇旭
@Email ：jiang.yuxu@mech-mind.net
@Time ： 2023/2/28 13:20
"""
from celery import Task
import random
import time
from pool import mysql_pool


class AddTask(Task):
    """
    官方文档说不会为每个请求实例化实例，而是作为全局实例在任务注册表中注册
    也就是说, 这个AddTask类只会实例化一次, 每一次请求进来将会调用一次run方法
    """
    name = "AddTask"

    def __init__(self):
        self.random_id = random.randint(1, 100)  # 在[1, 100]范围内随机生产random_id

    def run(self, x, y, table_name, *args, **kwargs):
        print('模拟io, random_id:{}'.format(self.random_id))  # 证明多次请求用的都是一个实例
        time.sleep(2)
        result = x + y
        db = mysql_pool.get_connection()
        with db.cursor() as cur:
            cur.execute("select * from steel_original_info limit 10")
            res = cur.fetchall()
            print(res)

        return result



