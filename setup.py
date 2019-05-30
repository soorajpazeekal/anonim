import os,sys,time
import webbrowser

#Basic script version=0.02



print('Reading requirements.txt\n')
time.sleep(1)

try:
	cmd = 'alias python=python3'
	os.system(cmd)
	cmd = 'alias pip=pip3'
	os.system(cmd)
	cmd = 'pip3 install -r requirements.txt'
	os.system(cmd)
	time.sleep(3)
	print('requirements sucessfully installed..\n')
	time.sleep(3)
except:
	print('Please check your python path! anonim trying to change that. but got error :(')
	time.sleep(3)
	print('please goto project --wiki-- for more info, and install anonim manually')


from tqdm import tqdm
from pyfiglet import Figlet

def stop_running():
	time.sleep(1)


def localip():
	cmd = 'python findlocalip.py'
	os.system(cmd)	


f = Figlet(font='doom')
print (f.renderText('anonim'))
time.sleep(3)


print('Creating media folder!\n')
time.sleep(2)
for i in tqdm(range(100)):
	time.sleep(0.100)
os.mkdir('media')
print('--------------media folder created!\n----------------')
time.sleep(2)


print('Creating Datebase!\n')
time.sleep(2)
for i in tqdm(range(100)):
	time.sleep(0.100)
os.system('python manage.py migrate')

print('Please follow following informations. --Press enter key to continue--\n')
get_usr = input('')
time.sleep(2)

print('1) >> First open settings.py file and set-up a powerful SECRET_KEY variable!\n')
stop_running()
get_usr = input('Done? Please press enter key!\n')
stop_running()

print('Inside settings.py go to line 18: --ALLOWED_HOSTS =-- variable. here you will need to add your connection address.\n')
stop_running()
localip()
stop_running()

print('Copy your system local ip address and paste to --ALLOWED_HOSTS =--.\n')
stop_running()
get_usr = input('Done? Press enter key!')
stop_running()

print('Done! Now run anoim.py to begin')



print('done. now please read the informations to change anonim settings.(Browser Opening)')
webbrowser.open('https://github.com/soorajpazeekal/anonim/wiki/Wiki-First-use!')
