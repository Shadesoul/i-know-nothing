# encoding=utf-8
import os
import time

source = ['/home/ice/python']
target_dir = '/home/ice'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('running:')

if os.system(zip_command) == 0:
	print('successful backup to',target)
else:
	print('backup failed')
