def car(*nums):
    sum=0
    for n in nums:
            sum=sum+n*n
            max=sum/n
    return max # 为什么计算car（2，3）等会出现奇怪的结果？它是怎么运算的？遍历吗？
    
def car(*nums):
    sum=1
    for n in nums:
        sum=sum*2/n 
    return sum # 为什么计算car（3，3）结果是0.444444？
    #懂了，只不过是再算一遍。sum=1*2/3,然后这个sum再*2/3就得到了结果。
    #这个运算方法是for in函数的效果。 

# encoding=utf-8
def total(a=5,*numbers,**phonebook):
	print('a',a)
	for i in numbers:
		print('i',i)
	for x in phonebook.items():#为什么必须加上一个items？其他的都会出错。
		print(x)
print(total(10,1,2,3,jack=1123,john=2231,inge=1570))
