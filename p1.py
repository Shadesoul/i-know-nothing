#encoding=utf-8
class robot:
    '''表示一个带有名字的机器人'''
    renkou=0
    def __init__(self,name):
        '''初始化数据'''
        self.name=name
        print('(creat {})'.format(self.name))
        robot.renkou+=1
        '''机器人数量+1'''
    def die(self):
        '''我挂了'''
        print('{} is being destroyed!'.format(self.name))
        robot.renkou-=1
        if robot.renkou==0:
            print('{} was the last one.'.format(self.name))
        else:
            print('there are still {} robots working.'.format(robot.renkou))
            
    def sayhi(self):
        '''机器人问候'''
        print('greetings,i got my name {}.'.format(self.name))
        
    @classmethod
    def how_many(cls):
        '''打印当前人口'''
        print('we have {:d} robots.'.format(cls.renkou))
       
droid1=robot('t100')
droid1.sayhi()
robot.how_many()

droid2=robot('t800')
droid2.sayhi()
robot.how_many()

print('robots can do some work here.\n')
print('robots have finished.destory.')

droid1.die()
droid2.die()

robot.how_many()

#this is different
#hot fix
