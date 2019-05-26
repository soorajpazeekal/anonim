import os,sys,time
from pyfiglet import Figlet
import webbrowser


f = Figlet(font='doom')
print (f.renderText('anonim'))

print('Looking for updates\n')
time.sleep(2)
os.system('git fetch origin master')
os.system('git merge origin master')


print('\n\n\n@SNIP3RS7\n\n--SNIP3RS7@COCK.LI\n\n\n \n***Make sure you have an active network connection:\n')
user_input = input('Press YES to start application!\n')
if user_input == 'yes':
	cmd = 'alias python=python3'
	os.system(cmd)
	webbrowser.open('http://127.0.0.1:8000')
	cmd = 'python manage.py runserver 0:8000'
	os.system(cmd)
else:
	print('Please enter right option:')

				

