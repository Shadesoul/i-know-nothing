# encoding=utf-8
Flask Web开发：基于Python的Web应用开发实战
《程序员修炼之道》（The Pragmatic Programmer）
《代码大全》（Code Complete）
《人月神话》（The Mythical Man-Month: Essays on Software Engineering）

os.system('notepad 1.txt') # 打开1.txt文件,如果不存在，则创建.这个os块暂时不知道怎么用，以后再说
os.getcwd()# ：获得当前工作目录
os.chdir(r'D:\python') # 改变工作目录到……
# cmd下切换工作目录，直接输入d:。然后cd 文件名，文件就打开了。cd D:/ 可以从python文件夹中退回到d盘。

# 格式化字符串的方法，廖雪峰的在字符串和编码一节，byte of python的如下：
# \表示换行继续，但不添加新的一行。


age=20
name = 'rick'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python?'.format(name))
print('{name} wrote {book}'.format(name='rick', book='a byte of python'))
#这大概是关键词参数的用法？


a = input('first:')
b = input('second:')
if a != b:
    print('good')
else:
    print('perfect')# 不能用return，函数会报错。可能不等式不算函数？
print('end')


x=30
def func():# 这个函数的作用就是先打印出现x的值，然后全局一下x，把全局x改成2.
    global x
    print('x is',x)
    x=2
    print('changed global x to',x)
    
func()
print('value of x is',x)
print('end')


#默认参数
def say(message,times=1):
    print(message*times)
say('hello')
say('world',5)#给数的话就不是默认的1了。很简单


#关键字参数
def func(a,b=5,c=10):
    print(a,b,c)
    
func(3,7)
func(25,c=24)
func(c=50,a=100)#感觉没什么意思，就是提前给默认值，然后选择性地赋值而已。


#可变参数
def total(a=5,*numbers,**phonebook):
	print('a',a)
	for i in numbers:
		print('i',i)
	for x in phonebook.items():#为什么必须加上一个items？其他的都会出错。可能因为phonebook的性质？它的参数属于一个字典。
		print(x)
print(total(10,1,2,3,jack=1123,john=2231,inge=1570))

#字典
ab={
    'swaroop':'swaroop@swaroopch.com',
    'larry':'larry@wall.org',
    'matsumoto':'matz@ruby-lang.org',
    'spammer':'spammer@hotmail.com'
}

print("swaroop's address is",ab['swaroop'])
del ab['spammer']
ab['guido'] = 'guido@python.org'
print('\nthere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('contact {} at {}'.format(name,address))

#区别：围绕函数处理数据，即面向过程；
#数据和功能整合起来，包装为一个对象，即面向对象。

#面向对象编程的两个主要方面：类与对象
#类创建类型（class创建type）。对象是类的实例
#类型为int的变量，a=50，也可以看作储存整数的变量a是int类的实例。a是int类的对象。
#整数也会被视作对象。

#从属于对象或类的变量叫做字段。字段又可以分为两种：实例变量与类变量。对象还可以使用属于类的函数来实现功能，这种函数叫类的方法。
#字段和方法通称类的属性。
#总结：类→对象\实例，字段和方法为类的属性，两种字段。

#用class创建一个类，后接字段和方法。类与函数在用法上的区别在于要多加一个self参数，不用赋值。
#例：myobject.method(arg1,arg2) = myclass.method(myobject,arg1,arg2)


class person: #类 
	def say_hi(self): #类的方法
		print('hello,how are you?') #

p = person() 
p.say_hi() #=类.方法 如果不这样的话，只能输入person().say_hi()

class jisuan:
    def __init__(self,a)
        a+10=a 
        print a #自造失败，a定义通不过
        
class person:
    def __init__(self,nam):
        self.nam=nam
    def sayhi(self):
        print('hello',self.nam)#name只是一个变量？可以替换为nam。
person('rui').sayhi()

   













