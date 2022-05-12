from django.shortcuts import render, redirect

# Create your views here.
def student(request):
    return render(request,'dashboards/student.html')

def mentor(request):
    return render(request,'dashboards/mentor/mentor.html')

def collaborator(request):
    return render(request,'dashboards/collaborator.html')

def volunteer(request):
    return render(request,'dashboards/volunteer.html')

def manager(request):
    return render(request,'dashboards/managers/manager.html')

def forum(request):
    return render(request,'dashboards/mentor/forum.html')

def visual(request):
    return render(request,'visual.html')