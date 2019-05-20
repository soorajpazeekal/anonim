import os
from pyfiglet import Figlet
import webbrowser


f = Figlet(font='isometric1')
print (f.renderText('anonim'))
print('\n\n\n@SNIP3RS7\n\n--SNIP3RS7@COCK.LI\n\n\n \n***Make sure you have an active internet connection:\n')
user_input = input('Press YES to start application!')
if user_input == 'yes':
	cmd = 'alias python=python3'
	os.system(cmd)
	cmd = 'python manage.py runserver 0:8000'
	os.system(cmd)
	webbrowser.open('http://127.0.0.1:8000')
else:
	print('Please enter right option:')

				

