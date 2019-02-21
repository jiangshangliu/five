'''

1.用python语句判断所输入的手机号，是否正确
要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
判断手机号码是否是由数字组成的
(总分15分，5分能够判断是否为数字，5分判断是否为有效号段，5分实现)

'''


pho_str = input("请输入手机号：")
b = 0
list1 = [131,132,135,136,138,139]  #号段
try:
    pho_num = int(pho_str)
except ValueError:
    b += 1
    print("请输入数字形式的手机号！")    #判断是否为数字

if b==0:
    if int(pho_str[:3]) in list1 and len(pho_str)==11:   #判断手机号是否正确
        print("手机号输入正确")

