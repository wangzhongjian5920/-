# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:31:02 2018

@author: Administrator
"""
def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j] for i in range(length) for j in range(i,length)]
string = "up!up!jd"
print(set((get_all_substrings(string))))
print(len(set((get_all_substrings(string)))))