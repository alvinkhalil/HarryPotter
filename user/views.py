import user
from django import forms
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
# Create your views here.

def userregister(request):
    
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        name = form.cleaned_data.get("name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")

        newUser = User(username = username,first_name = name,last_name = last_name,email = email)
        newUser.set_password(password)
     
        newUser.save()
    
        login(request,newUser)
        messages.success(request,"Qeydiyyat uğurla baş verdi.")

        return redirect("index")
       
          
 
    return render(request,"register.html",{"form":form})

def userlogin(request):
    
    form = LoginForm(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:

            messages.info(request,"İstifadəçi adı və ya şifrə yalnışdır.")
            return render(request,"login.html",{"form":form})

        login(request,user)
        messages.success(request,"Hesabınıza uğulra giriş edildi")
        return redirect("index")


    return render(request, "login.html",{"form":form})

def userlogout(request):
    logout(request)
    messages.success(request,"Hesabdan uğurla çıxıldı.")
    return redirect("index")