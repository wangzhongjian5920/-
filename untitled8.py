# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:26:38 2018

@author: Administrator
"""

import datetime

t1 = datetime.datetime(2017,10,10,21,40)
t2 = datetime.datetime(2017,10,8,23,40)
tt1 = datetime.timedelta(seconds=1200)
tt2 = datetime.timedelta(weeks=3)
print(t1 - t2)