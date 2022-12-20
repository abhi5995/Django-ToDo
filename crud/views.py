from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def sign_up(req):
    if req.method == 'POST':
        fm = UserRegistrationForm(req.POST)
        if fm.is_valid():
            fm.save()
            messages.success(req, f"User {fm.cleaned_data['username']} created successfully.")
            return HttpResponseRedirect(reverse('home'))
        return render(req,'crud/signup.html', {'form':fm})
    fm = UserRegistrationForm()
    return render(req,'crud/signup.html', {'form':fm})

def log_in(req):
    if req.method=='POST':
        fm = LoginForm(request=req, data=req.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request=req, user=user)
                messages.success(request=req, message=f"{uname} logged in successfully!")
                return HttpResponseRedirect(reverse('home'))
    else:
        fm = LoginForm()
    return render(req, 'crud/login.html', {'form':fm})

def log_out(req):
    logout(req)
    return HttpResponseRedirect(reverse('log_in'))