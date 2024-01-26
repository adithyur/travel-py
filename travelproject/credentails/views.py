from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect


def login(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            message.info(request,'invalid login')
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if(password==password2):
            if(User.objects.filter(username=user_name).exists()):
                messages.error(request,'user exist')
                print('user exist')
            elif(User.objects.filter(email=email).exists()):
                messages.error(request,'email exist')
                print('user exist')
            else:
                user=User.objects.create_user(username=user_name,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.warning(request,'password mismatch')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
