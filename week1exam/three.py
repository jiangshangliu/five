'''

编写程序，生成一个包含20个随机整数的列表，
然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
奇数下标的元素不变。
（提示：使用切片。） (20分：生成列表5分，找到偶数下标8分，降序7分)

'''

import random

list0 = []

for i in range(20):
    list0.append(random.randint(1,50))  #生成一个包含20个随机整数的列表

print('原始序列：',list0)
# print(len(list0))

for i in range(0,len(list0),2):
    for j in range(i+2,len(list0),2):
        if i < len(list0)-2:           #防止下标越界

            if list0[i]<list0[j]:       #对所有偶数元素降序排序
                temp = list0[i]
                list0[i] = list0[j]
                list0[j] = temp

print("对偶数元素排序后的序列：",list0)






