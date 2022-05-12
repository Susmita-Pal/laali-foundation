from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Reg
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        reg=Reg.objects.get(username=uname, password=pwd)
        #print(reg.name)'

        #print(reg.name)
        #if uname==reg.username and pwd==reg.password:
         #   print("Success")
        #user = auth.authenticate(username=uname, password=pwd)
        if reg is not None:
            print("Success")
            print(reg.designation)
            temp = ''
            if reg.designation == 'Fellow':
                temp = 'student'
            elif reg.designation == 'Mentor':
                temp = 'mentor'
            elif reg.designation == 'program-manager':
                temp = 'manager'
            elif reg.designation == 'collaborator':
                temp = 'collaborator'
            print(temp)
            return redirect('/dashboard/'+temp)
        else:
            print("Failed")
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        uname = request.POST['uname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        desg=request.POST['desg']
        cpwd = request.POST['cpwd']
        gen=request.POST['gen']
        if pwd == cpwd:
            if Reg.objects.filter(username=uname).exists():
                print('Username exists')
                messages.info(request, "Username has been taken")
                return redirect('register')
            elif Reg.objects.filter(email=email).exists():
                print('Email has been taken by other user')
                messages.info(request, "Email has been taken")
                return redirect('register')
            else:
                user = Reg.objects.create(username=uname, email=email, password=pwd, name=name, gender=gen,designation=desg, confirm_password=cpwd)
                user.save()
                print('User created')
                success(user)
                return redirect('/accounts/login')
        else:
            print('Passwords do not match')
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def success(request):
    template=render_to_string('email_template.html',{'name':request.name})
    email=EmailMessage(
        'Welcome Email',
        template,
        settings.EMAIL_HOST_USER,
        ['gurtevarzi@vusra.com'],
    )
    print('welcome email sent ')
    email.fail_silently=False
    email.send()