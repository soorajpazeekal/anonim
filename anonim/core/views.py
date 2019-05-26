#ViewCode prefly written funcaton based view(FBV). 
#T&C @SN1P3RS7  


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import os.path
from os import path
from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import datetime,socket
from cryptography.fernet import Fernet


def home(request):
    #ip = socket.gethostbyname('www.google.com')
    try:
        local_connection = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
               s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
                socket.SOCK_DGRAM)]][0][1]]) if l][0][0] 
    except:
           exception = 'error'   
           local_connection = 'NO NETWORK. PLEASE CONNECT TO ANY NETWORK!'
    msg_heading = 'INFO'
    messages = 'Use this local ip address to connect localy:'  
#Passing arguments to rendering web-page(if.try mode run)
    currentDT = datetime.datetime.now()
    current_Domain = request.build_absolute_uri('?')
    count = User.objects.count()
    msg_heading = 'Info:'
    key = Fernet.generate_key()
    key_frameLoad = key
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b'key')
    plain_text = cipher_suite.decrypt(cipher_text)
    usernames = User.objects.values_list('username', flat=True)
    return render(request, 'dash.html', {
            'count': count,
            'currentDT' : currentDT,
            'local_connect' : local_connection,
            'msg_heading' : msg_heading,
            'messages' : messages,
            'cipher_text' : cipher_text,
            'usernames' : usernames,
            'saltloadedKEY' : key_frameLoad,
            'current_Domain' : current_Domain,
       
    })





@login_required
def gallery(request):
    if request.user.is_authenticated:
        msg_heading = 'Last Update:'  #Direct message/alert rendering to page.
        messages = ''
        path = "media"  
        img_list = os.listdir(path)    
        currentDT = datetime.datetime.now()  
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(b'key')
        plain_text = cipher_suite.decrypt(cipher_text)
        return render(request, 'gallery.html', {
            'images': img_list,
            'currentDT' : currentDT,
            'msg_heading' : msg_heading,
            'messages' : messages,
            'cipher_text' : cipher_text

            })

@login_required
def connect_wan(request): #connecting to wide area. assigning to .bin file and start the funcation
        error_log =  'zenity --info --text="WAN connection now establishing.\n\nPlease open the current running terminal!\n *make sure you have an active internet connection!\t\t\t" --title="Warning!"'
        os.system (error_log)
        if(os.path.isfile('wanDomainLog.anonimLog')):
            file = open("wanDomainLog.anonimLog", "r")  
            out_file_cont = file.read()
            error_log =  'zenity --info --text="We fount you have aleady use a domain for wan connection.\t\t You can use current or new wan domain now!\t\t" --title="Warning!"'
            get_usr_input = input(out_file_cont +'\t:is your pervious wan domain. \nenter Y for continue > \nC for change! >\n')
            if (get_usr_input == 'y'):
                file = open("wanDomainLog.anonimLog", "r")  
                out_file_cont = file.read()
                somestring = ('ssh -R '+out_file_cont+':80:localhost:8000 serveo.net')
                os.system(somestring)
            if(get_usr_input == 'c'):
                ans_user = input('enter a name:\n')
                file = open('wanDomainLog.anonimLog','w') 
                file.write(ans_user) 
                file.close() 
                somestring = ('ssh -R '+ans_user+':80:localhost:8000 serveo.net')
                os.system(somestring)
                msg_heading = 'Info:'
                messages = 'plesase open the running terminal'
                os.system(somestring)
        else:           
            ans_user = input('enter a name:\n')
            file = open('wanDomainLog.anonimLog','w') 
            file.write(ans_user) 
            file.close() 
            somestring = ('ssh -R '+ans_user+':80:localhost:8000 serveo.net')
            os.system(somestring)
            msg_heading = 'Info:'
            messages = 'plesase open the running terminal'
            os.system(somestring) 
        return render(request, 'gallery.html',{
             'messages' : messages,
             'msg_heading' : msg_heading

        })





#retriting logged-user to redirecting to gallery view.
@login_required
def media(request):
    return redirect('gallery')






#First make sure request is 'post mode'.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Saving directly to db. access via shell
            return redirect('dash.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)




@login_required
def dash(request):
    if request.user.is_authenticated:
        msg_heading = 'Last Update:'  #Direct message/alert rendering to page.
        messages = ''   
        currentDT = datetime.datetime.now()  
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(b'key')
        plain_text = cipher_suite.decrypt(cipher_text)
        return render(request, 'dash.html', {
            'currentDT' : currentDT,
            'msg_heading' : msg_heading,
            'messages' : messages,
            'cipher_text' : cipher_text

            })