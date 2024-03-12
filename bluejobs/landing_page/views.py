from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import StudentSignUpForm

class StudentHomepage(View):
    def get(self, request):
        return render(request, 'landing_page/student-homepage.html', {'name': 'Home'})
    
def about(request):
    return render(request, 'landing_page/about.html')

def help(request):
    return render(request, 'landing_page/help.html')

def developers(request):
    return render(request, 'landing_page/developers.html')

def home(request):
    return render(request, 'landing_page/home.html')

def student(request):
    return render(request, 'landing_page/student.html')

def department(request):
    return render(request, 'landing_page/department.html')

def login(request):
    return render(request, 'landing_page/login.html')

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'landing_page/home.html')
    else:
        form = StudentSignUpForm()
    return render(request, 'landing_page/signup.html', {'form': form})