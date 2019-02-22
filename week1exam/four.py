'''

4.随机生成一个包含1000个字母的字符串，然后统计该字符串中每个字母的数量，
并输出结果（要求结果以字典方式存储）（
20分：随机生成字符串5分，统计字母数量8分，以字典方式存储5分，输出结果2分）

'''

import random

str = ''
for i in range(1000):
    str+=random.choice("bcdefghijklmnopqrstuvwxyz")    #随机生成一个包含1000个字母的字符串

d = {}
for i in str:
    d[i] = str.count(i)
print(d)    #并输出结果（要求结果以字典方式存储）



