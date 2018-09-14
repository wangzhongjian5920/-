# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:04:55 2018

@author: Administrator
"""

from collections import deque

def check(q):
    count = 0
    while (len(q) != 0):
        left = q.popleft()
        if len(q) == 0:
            return count
        else:
            right = q.pop()
            if left < right:
                count += 1
                if len(q) != 0:
                    left += q.popleft()
                    q.append(right)
                    q.appendleft(left)
            elif left > right:
                count += 1
                if len(q) != 0:
                    right += q.pop()
                    q.appendleft(left)
                    q.append(right)
    return count


if __name__ == "__main__":
    b = int(input())
    a = list(map(int, input().strip().split( )))
    q = deque()
    for i in a:
        q.append(i)
    print(check(q))