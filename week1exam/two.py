'''
2. 编写程序，生成一个包含50个随机整数的列表，
随机整数的范围是从-10到10，
然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。
（15分：生成随机列表5分，得出正负数新列表各5分）

'''
import random

list1 = []
for i in range(50):
    list1.append(random.randint(-10,11))

# print(list1)
# print(len(list1))

listZ = [] #存储正数
listF = [] #存储负数

for i in list1:
    if i > 0:
        listZ.append(i)
    elif i < 0:           #不包括0，所以不能使用else
        listF.append(i)
print(listZ)
print(listF)


