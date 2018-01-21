import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '这不是一元二次方程，请重新输入'
            else:
                return '这不是一元二次方程，请重新输入'
        return '这不是一元二次方程，请重新输入'
    else:
        if d<0:
            return '方程无解'
        if d==0:
            x1=-b/2*a
            x2=x1
            return '方程只有一个解：',x1
        else:
            x1 = (-b + math.sqrt(d))/2/a 
            x2 = (-b - math.sqrt(d))/2/a
            return '方程有两个解：',x1,x2  