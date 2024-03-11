from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')

def student(request):
    return render(request, 'accounts/student.html')

def department(request):
    return render(request, 'accounts/department.html')

def login(request):
    return render(request, 'accounts/login.html')