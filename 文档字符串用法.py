# encoding=utf-8
def print_max(x,y):# 首行加一个tab可以和后面行对齐，好看。
	'''	这是文档字符串
	should it be blank?
	这是结尾'''
	x=int(x)
	y=int(y)

	if x>y:
		print(x,'is maximum')
	else:
		print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)
