import os,sys,time
from pyfiglet import Figlet
import webbrowser

#Basic script version=00.1


f = Figlet(font='doom')
print (f.renderText('anonim'))
time.sleep(2)
print('**This is a beta version and currently tested with Linux/ubuntu OS. windows updates coming soon :)\n')
time.sleep(4)
print('**Please send your feedbacks to: --helpttreect@cock.li-- and follow our -github repo- for more info.\n')
time.sleep(4)
print('**Never share security credentials like user-name, password, db security key, private connection name, are never share to public.\n')
time.sleep(2)
print('Done! --------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(3)
print('Reading requirements.txt\n')

try:
	cmd = 'alias python=python3'
	os.system(cmd)
	cmd = 'pip install -r requirements.txt'
	os.system(cmd)
	time.sleep(3)
	print('requirements sucessfully installed..\n')
	time.sleep(3)
	print('done. now please read the informations to chnage anonim settings.')
	webbrowser.open('http://example.com')
except:
	print('Please check your python path! anonim trying to change that. but got error :(')
	time.sleep(3)
	print('please goto project --wiki-- for more info, and install anonim manually')