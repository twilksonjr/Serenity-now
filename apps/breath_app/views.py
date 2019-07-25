from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
import bcrypt
from datetime import datetime


def Index(request):
    return render(request, "breath_app/index.html")


def Registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        registeredUser = User.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=hash1)
        request.session["user_id"] = registeredUser.id
        return redirect('serenity_now/')


def Login(request):
    errors = User.objects.login_validator(request.POST)
    if not len(errors):
        user = User.objects.get(email=request.POST['login_email'])
        request.session["user_id"] = user.id
        return redirect("serenity_now/")
    # if the login information is NOT correct
    else:
        print("*"*80)
        print('validation failed on login')
        print("*"*80)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')


# def Serenity(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     context = {
#         "logged_in_user": User.objects.get(id=request.session["user_id"]),
#     }
#     return render(request, "breath_app/serenity.html", context)

def Logout(request):
    request.session.clear()
    return redirect('/')

# 1234