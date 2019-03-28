from django.shortcuts import render
from django.http import HttpResponse
from.models import Slam

# Create your views here.
name=["mubarak","vinod","rafi","ramana"]

def home(request):
    return render (request, "home.html")
def slam(request):
    a=request.POST["t1"]
    if a in name[0]:
        return render(request,"slam.html")
    elif a in name[1]:
        return render(request,"slam2.html")
    elif a in name[2]:
        return render(request,"slam.html")
    elif a in name[3]:
        return render(request,"slam.html")
    else:
        return HttpResponse("fail")
def insert(request):
    fname1=request.POST['s1']
    sname1=request.POST['s2']
    f=Slam(fname=fname1,sname=sname1)
    f.save()
    return render(request, "thanks.html")


def display(request):
    recs=Slam.objects.all()
    return render(request,'display.html',{'records':recs})
def login(request):
    return render(request,"login.html")
def log(request):
    return render (request,"log.html")



