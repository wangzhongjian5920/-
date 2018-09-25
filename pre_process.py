#!usr/bin/python
"""
Created on Thu Sep 20 23:40:08 2018

@author: Administrator
"""
import re
import sys

##This is a python function
def process(text, width):
    ## right strip and find all words
    text_after_strip = text.rstrip()
    pattern = re.compile('[A-Za-z]+')
    words = pattern.findall(text_after_strip)
    ## formatted text
    formed_text = []
    line_num = len(text_after_strip)//width
    for i in range(line_num):
        formed_text.append(text_after_strip[i * width: (i+1) * width] + '\n')
    if line_num * width < len(text_after_strip):
        formed_text.append(text_after_strip[line_num * width: len(text_after_strip)])
    return ''.join(formed_text)


if __name__ == "__main__":
    text = input('Please input the text: ')
    width = int(input('Please input the width: '))
    try:
        text = text.rstrip()
        for i in text:
            if not(i.isalpha() or i.isspace()):
                raise IOError
        if not (10 <= width <= 80):
            raise myError
        print(process(text, width))
    except IOError:
        print("ERROR: Invalid character detected!")
        sys.exit()
    except myError:
        print('ERROR: Width out of range!')
        sys.exit()
        
