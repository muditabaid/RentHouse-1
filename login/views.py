from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
# Create your views here.
def login(request):
     return render(request,'login/login.html')
def modal(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('login')
    else: 
        form = AuthenticationForm()
    return render(request,'login/modal.html',{'form': form})