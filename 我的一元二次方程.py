# encoding=utf-8
import math 
def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(float,int)):
            raise TypeError('数据类型错误') # 不知道为什么，这条不管用，仍旧是自带的出错提示。
    d = b*b-4*a*c
    if a == 0:
        return '这不是一元二次方程'
    else:
        if d == 0:
            x1=-b/2*a
            x2=x1
            return ('方程只有一个解:',x1)
        if d < 0:
            return '方程无实数根'
        else:
            x1 = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
            x2 = (-b - math.sqrt(b*b-4*a*c)) / (2*a)
            return ('该方程有两个解:', x1,x2)
# 简明python鼓励import文件，然后用文件.函数的形式调用函数。而不是from 文件 import 函数，这条待以后思考。为什么呢？



