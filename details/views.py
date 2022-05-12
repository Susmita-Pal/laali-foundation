from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request,'dashboards/details.html')
    return render(request, 'sessions_get.html')

def mdetails(request):
    return render(request,'dashboards/mentor/mentor_profile.html')

def addetails(request):
    return render(request,'dashboards/managers/manager_profile.html')