# encoding=utf-8
number = 764
running = True

while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('congratulations!')
        running = False # 循环直到猜中的while用法
    elif guess < number:
        print('no,higher than that')
    else:
        print('no,lower than that')
else:
    print('the loop is over.')
    print('the end')

while True:
    s=input('Enter something:')
    if s == 'quit':
        break #break语句 
    print('Length of the string is',len(s))
    print('The end')

while True:
    s=input('enter something:')
    if s == 'quit':
        break
    if len(s)<3:
        print('too small')
        continue #continue语句用法
    print('input is good')
    print('the end')
