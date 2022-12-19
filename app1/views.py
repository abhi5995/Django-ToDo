from django.shortcuts import render, HttpResponseRedirect
from app1.forms import AddStudent
from app1.models import Student
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(req):
    allStudent = Student.objects.all()
    if req.method=='POST':
        fm = AddStudent(req.POST)
        # print(fm)
        if fm.is_valid():
            fm.save()
            messages.add_message(req, messages.SUCCESS, fm.cleaned_data["stuname"])
        fm = AddStudent()
        return HttpResponseRedirect(reverse('home'))
    else:
        fm = AddStudent()
    return render(req, 'crud/home.html', {'form':fm, 'allstu':allStudent, 'action':'Add'})

def delete(req, id):
    stu = Student.objects.get(pk=id)
    nm = stu.stuname
    stu.delete()
    messages.error(req, nm)
    return HttpResponseRedirect(reverse('home'))
def edit(req, id):
    allStudent = Student.objects.all()
    stu = Student.objects.get(pk=id)
    if req.method=='POST':
        fm = AddStudent(req.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            messages.info(req, fm.cleaned_data["stuname"])
        fm = AddStudent()
        return HttpResponseRedirect(reverse('home'))
    else:
        fm = AddStudent(instance=stu)
        action = 'Edit'
    return render(req, 'crud/home.html', {'form':fm, 'allstu':allStudent, 'action':action})