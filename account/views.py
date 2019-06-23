from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect

from django.contrib import sessions,messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from account.forms import Userform

def special(request):
    return HttpResponse('You\'re loggeddin!!')

def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form = Userform()
    return render(request,'auth/signup.html',{'user_form':user_form,
                                            'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'auth/login.html', {})