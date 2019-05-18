import os,sys,time
import webbrowser

#Basic script version=00.1



print('Reading requirements.txt\n')
time.sleep(1)

try:
	cmd = 'alias python=python3'
	os.system(cmd)
	cmd = 'alias pip=pip3'
	os.system(cmd)
	cmd = 'pip install -r requirements.txt'
	os.system(cmd)
	time.sleep(3)
	print('requirements sucessfully installed..\n')
	time.sleep(3)
	print('done. now please read the informations to chnage anonim settings.')
	webbrowser.open('https://github.com/soorajpazeekal/anonim/wiki/Wiki-First-use!')
except:
	print('Please check your python path! anonim trying to change that. but got error :(')
	time.sleep(3)
	print('please goto project --wiki-- for more info, and install anonim manually')


from tqdm import tqdm
from pyfiglet import Figlet

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

print('**This is a beta version and currently tested with Linux/ubuntu OS. windows updates coming soon :)\n')
time.sleep(4)
print('**Please send your feedbacks to: --helpttreect@cock.li-- and follow our -github repo- for more info.\n')
time.sleep(4)
print('**Never share security credentials like user-name, password, db security key, private connection name, are never share to public.\n')
time.sleep(2)
print('Done! --------------------------------------------------------------------------------------------------------------------------------------------\n')
time.sleep(3)
