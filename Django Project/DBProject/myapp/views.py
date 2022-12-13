from django.shortcuts import render,redirect
from .forms import StudinfoForm
from .models import studinfo

# Create your views here.

def index(request):
    if request.method=='POST':
        stfrm=StudinfoForm(request.POST)
        if stfrm.is_valid():
            stfrm.save()
            print("Your data has been saved!")
        else:
            print(stfrm.errors)
    return render(request,'index.html')

def showdata(request):
    data=studinfo.objects.all()
    return render(request,'showdata.html',{'dt':data})

def updatedata(request,cid):
    stid=studinfo.objects.get(id=cid)
    if request.method=='POST':
        stupdate=StudinfoForm(request.POST)
        if stupdate.is_valid():
            stupdate=StudinfoForm(request.POST,instance=stid)
            stupdate.save()
            print("Record updated!")
            return redirect("showdata")
        else:
            print(stupdate.errors)
    return render(request,'updatedata.html',{'cid':studinfo.objects.get(id=cid)})

def deletedata(request,cid):
    stid=studinfo.objects.get(id=cid)
    studinfo.delete(stid)
    return redirect('showdata')
    
