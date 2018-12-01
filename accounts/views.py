from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'User does not exist')
            return redirect('login')
        return
    else:
        return render(request,'accounts/login.html')
def register(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
             if User.objects.filter(username=username).exists():
                messages.error(request,'User already esists')
                return redirect('register')
             else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            messages.error(request,'Password does not match !!!!')
            return redirect('register')



    else:
        return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
