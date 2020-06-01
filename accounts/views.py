from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login-user')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
    
    
def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('posts:index')
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('accounts:login-user')
    context = {}
    return render(request, 'accounts/login.html', context)
    
def logout_user(request):
    logout(request)
    return redirect('accounts:login-user')
    
    
def delete_user(request):
    pk = request.user.id
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('accounts:register-user')