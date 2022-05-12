from django.shortcuts import render,redirect
from .models import CreateAssgn

# Create your views here.
def assignments(request):
    return render(request,'dashboards/assignment.html')

def score(request):
    cnt=0
    if request.method =='POST':
        radio=request.POST['rad']
        check=request.POST['chk']
        ta=request.POST['ta']
        print(radio)
        print(check)
        print(ta)
        if radio == 'A':
            cnt = cnt + 1
        if check == 'b':
            cnt = cnt + 1
        if ta is not None:
            cnt = cnt + 1

        ans=CreateAssgn.objects.create(ansRad=radio,andCheck=check,ansTextArea=ta,score=cnt)
        ans.save()
        print("Score in DB success")
        return render(request,'base.html')
    else:
        return render(request,'asgn.html')