"""
Created on Tue Sep 18 16:45:12 2018

@author: Administrator
"""

"""
某餐馆有n张桌子，每张桌子有一个参数：a 可容纳的最大人数； 
有m批客人，每批客人有两个参数:b人数，c预计消费金额。 
在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大
输入描述:
输入包括m+2行。 
第一行两个整数n(1 <= n <= 50000),m(1 <= m <= 50000) 
第二行为n个参数a,即每个桌子可容纳的最大人数,以空格分隔,范围均在32位int范围内。 
接下来m行，每行两个参数b,c。分别表示第i批客人的人数和预计消费金额,以空格分隔,范围均在32位int范围内。
输出描述:
输出一个整数,表示最大的总预计消费金额
"""
def search(nums, target):
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return -1
    l, r = 0, len(nums)-1
    while l+1 != r:
        m = (l+r) // 2
        if target <= nums[m]:
            r = m
        else:
            l = m
    return r

if __name__ == "__main__":
    customers = []
    n, m = map(int, input().strip().split(' '))
    tables = list(map(int, input().strip().split(' ')))
    for _ in range(m):
        people, money = map(int, input().strip().split(' '))
        customers.append([people, money])
    tables.sort()
    customers.sort(key=lambda k:k[1], reverse = True)
    fin = 0
    for customer in customers:
        if len(tables) == 0:
            break
        index = search(tables, customer[0])
        if index >= 0:
            del tables[index]
            fin += customer[1]
    print(fin)