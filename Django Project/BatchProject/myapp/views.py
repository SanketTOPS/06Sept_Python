from django.shortcuts import render,redirect
from .forms import signupForm,notesForm
from .models import usersignup
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from BatchProject import settings
import random
import requests

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            username=""
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get('username')
                try:
                    un=usersignup.objects.get(username=username)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except usersignup.DoesNotExist:
                    newuser.save()
                    print("User created successfully!")
                    messages.success(request,"User created successfully!")

                    #Email Sending Code
                    #send_mail(subject="Welcome!",message=f"Hello User!\nYour account has been created with us!\nEnjoy our services\n\nIf need any help, contact on\n+9197247 99469 | help@notesapp.com",from_email=settings.EMAIL_HOST_USER,recipient_list=["angelraninga0206@icloud.com","kashyapsorathiya14@gmail.com","alishpanara4412@gmail.com","aazammorvadiya890@gmail.com","anjukakran999@gmail.com","shyampabari02@gmail.com"])
                    otp=random.randint(1111,9999)
                    sub="Welcome!"
                    msg=f"Hello User!\nYour account has been created with us!\nEnjoy our services\nYour Verification code is {otp}\nIf need any help, contact on\n+9197247 99469 | help@notesapp.com"
                    from_ID=settings.EMAIL_HOST_USER
                    to_ID=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                    return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm,password=pas)
            uid=usersignup.objects.get(username=unm)
            print("UserID:",uid.id)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm
                request.session['userid']=uid.id

                #MSG Sending Code
                """otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"9726860911,9328627721,8155894412,7228021405,9737538995,9638888719"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""    
                
                """url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":"Hi Aazam, this message is to confirm that we received a deposit of 350000 in your account ending in 5909 on 10/01/2023. ","language":"english","route":"q","numbers":"7228021405,9737538995,9726860911"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""
                
                return redirect('notes')
            else:
                print("Error! Username or Password does't match.")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesForm(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been uploaded!")
            messages.success(request,"Your notes has been uploaded!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=signupForm(request.POST)
        if updateuser.is_valid():
            updateuser=signupForm(request.POST,instance=cuser)
            updateuser.save()
            print('Your profile has been updated!')
            return redirect('notes')
        else:
            print(updateuser.errors)
    return render(request,'updateprofile.html',{'user':user,'cuser':usersignup.objects.get(id=uid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')