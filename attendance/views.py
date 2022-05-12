from django.shortcuts import render

# Create your views here.
def attendance(request):
    return render(request,'dashboards/attendance.html')

def mattendance(request):
    return render(request,'dashboards/mentor/mattendance.html')