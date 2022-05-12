from django.shortcuts import render, redirect
from .models import Session_det
# Create your views here.
def session_get(request):
   # import pdb;
    #pdb.set_trace()
   #if request.method=='POST':
    #   session_post()
   #else:
        seshFetch = Session_det.objects.all()
        return render(request, 'session_get.html',{'seshDet':seshFetch})

def session_post(request):
    return render(request, 'session_post.html')
    if request.method =='POST':
        title=request.POST['title']
        link=request.POST['link']
        date=request.POST['date']
        time=request.POST['time']
        sesh=Session_det.objects.create(title=title,link=link,datee=date,timee=time)
        if sesh is not None:
            print("Success")
            print(sesh.title)
            print(request)
            return render(request,'session.html')
        else:
            print("Failure")

def msession_get(request):
        seshFetch = Session_det.objects.all()
        return render(request, 'msession_get.html',{'seshDet':seshFetch})

def newsess(request):
        seshFetch = Session_det.objects.all()
        return render(request, 'create_session.html',{'seshDet':seshFetch})