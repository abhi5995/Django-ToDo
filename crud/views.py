from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def sign_up(req):
    if req.method == 'POST':
        fm = UserCreationForm(req.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('home'))
        return render(req,'crud/signup.html', {'form':fm})
    fm = UserCreationForm()
    return render(req,'crud/signup.html', {'form':fm})