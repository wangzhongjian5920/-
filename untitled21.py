# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:46:42 2018

@author: Administrator
"""

#!/user/bin/python

import os

with open("result.txt", "w+") as f:
    for i in range(1000):
        cmd = "./test1 "+ str(i)
        f.writeline(os.system(cmd))
        
if os.system("diff %s code1"):
    print("Right")
else:
    print("Wrong")
    
    
