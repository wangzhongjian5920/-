# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:26:30 2018

@author: Administrator
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
 
class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        #检查之后是否还有k个数
        def check(head,k):
            for i in range(k):
                if(head.next==None):return False
                head=head.next
            return True
 
 
        def reverse(dummy,k):
    
            #输入的dummy为要反转的序列的前一个node
            #即输入的时候为 dummy [1,2,3,4...k]
            #最终return时候为 dummy [k,k-1,...,3,2,1] .   return 1
            head=dummy.next
            save=dummy
            result=dummy.next
           
            i=0
            while (True):
                pre = head.next
                head.next = dummy
                dummy = head
                head = pre
                i=i+1
                result.next = pre
                if (i >=k): break
            #return的是反转后的尾巴
            save.next=dummy
 
            return result
 
        if(k==1):return head
        dummy = ListNode(None)
        result=dummy
        dummy.next = head
        while(check(dummy,k)):
            dummy=reverse(dummy,k)
 
        return result.next

node = list(input().strip().split( ))
new_node = []
for i in range(len(node)):
    new_node.append(ListNode(node(i)))
for i in range(len(node) - 1):
    new_node[i].next = new_node[i+1]
# node4.next = node5
s = Solution()
result = s.reverseKGroup(node1,4)
while (result != None):
    print(result.val)
    result = result.next