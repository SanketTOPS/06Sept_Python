from django.shortcuts import render,redirect
from .forms import signupForm,notesForm
from .models import usersignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")
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