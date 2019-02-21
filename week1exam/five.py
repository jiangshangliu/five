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

d = {}
list0 = []
list1 = []
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \

s1 = s.replace(",","").replace(".","")
list0 = s.split(" ")
#print(list0)

for i in list0:
    d[i] = list0.count(i)   #生成字典并统计次数
    list1.append(d[i])
print('d:',d)

d2 = []
for i in list1:
    for j in d:
        if list[i]==d[j]:
            d2[d[j]]=list[i]
print('d2:',d2)


