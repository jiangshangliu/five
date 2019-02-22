'''

5.实现以下功能：（30分）
	s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \
对这段文字中的单词进行数字统计，并且进行个数升序
（能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）

'''

# d = {}
# list0 = []
# list1 = []
# d2 = {}
# s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python '
#
# s1 = s.replace(",","").replace(".","")
# list0 = s.split(" ",s.count(" ")-1)     #字符串结尾多一个空格，消除空格
# print('list0',list0)
#
# for i in list0:
#     d[i] = list0.count(i)   #生成字典并统计次数
#     x = (i,list0.count(i))
#     list1.append(x)
# print('d:',d)
# print("list1:",list1)
#
#
# L = sorted(list1, key=lambda x:x[1])   #指定按那个元素进行排序
# print(L)
#
# for i in L:
#     j = i[0]
#     d2[j] = i[1]
# print('d2:',d2)

#-----------------------------------
#方法2：

d = {}
list0 = []

d2 = {}
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '

s1 = s.replace(",","").replace(".","")
list0 = s.split(" ",s.count(" ")-1)     #字符串结尾多一个空格，消除空格
print('list0',list0)

for i in list0:
    d[i] = list0.count(i)   #生成字典并统计次数
print('d:',d)

L = sorted(d.items(), key=lambda x:x[1])   #指定按那个元素进行排序
print('L:',L)

for i in L:
    j = i[0]
    d2[j] = i[1]
print('d2:',d2)
