'''
3）质数规律判断法

首先看一个关于质数分布的规律：大于等于5的质数一定和6的倍数相邻。例如5和7，11和13,17和19等等；

证明：令x≥1，将大于等于5的自然数表示如下：

······6x-2，6x-1，6x，6x+1，6x+2，6x+3，6x+4，6x+5，6x+6，6x+7······

也就是

······2(3x-1)，6x-1，6x，6x+1，2(3x+1)，3(2x+1)，2(3x+2)，6x+5，6(x+1)，6(x+1)+1······

可以看到，不在6的倍数两侧，即6x两侧的数为6x+2，6x+3，6x+4，由于2(3x+1)，3(2x+1)，2(3x+2)，
所以它们一定不是素数，再除去6x本身，显然，素数要出现只可能出现在6x的相邻两侧。
这里要注意的一点是，在6的倍数相邻两侧并不是一定就是质数。

根据以上规律，判断质数可以6个为单元快进，即将方法（2）循环中i++步长加大为6，加快判断速度，代码如下：
'''

from math import sqrt


def isPrime(num):
    if num == 2 or num == 3:  # 两个较小的数进行处理
        return True
    if num % 6 != 1 and num % 6 != 5:  # 不在6的倍数的两侧的一定不是质数
        return False
    tmp = int(sqrt(num))
    for i in range(5, tmp + 1):  # 在6的倍数两侧的也可能不是质数
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True  # 剩下的全是质数



#-----------practice01------------
# def isPrime(num):
#     if num == 2 or num == 3:
#         return True
#     if num % 6 != 1 and num % 6 != 5:
#         return False
#     temp = int(sqrt(num))
#     for i in range(5,temp+1):
#         if num % i == 0 or num % (i+2) == 0:
#             return False
#     return True
#
# print(isPrime(37))


#-----------practice02------------
# from math import sqrt
#
# def isPrime(num):
#     if num ==2 or num ==3:
#         return True
#     if num % 6 != 1 and num % 6 != 5:
#         return False
#     temp = int(sqrt(num))
#     for i in range(5,temp+1):
#         if num % i == 0 or num % (i+2) ==0:
#             return False
#     return True
#
# print(isPrime(53))





