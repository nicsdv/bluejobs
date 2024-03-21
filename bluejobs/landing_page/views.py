from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import StudentSignUpForm, DepartmentSignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

class StudentHomepage(View):
    def get(self, request):
        return render(request, 'landing_page/homepage-student.html', {'name': 'Home'})
    
class DepartmentHomepage(View):
    def get(self, request):
        return render(request, 'landing_page/homepage-department.html', {'name': 'Home'})
    
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

def signup(request):
    return render(request, 'landing_page/signup.html')

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            return redirect(reverse_lazy('landing_page:login'))
    else:
        form = StudentSignUpForm()
    return render(request, 'landing_page/signup-student.html', {'form': form})

def department_signup(request):
    if request.method == 'POST':
        form = DepartmentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_department = True
            user.save()
            return redirect('landing_page:login')
    else:
        form = DepartmentSignUpForm()
    return render(request, 'landing_page/signup-department.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate user type's dashboard
                if user.is_student:
                    return redirect('landing_page:homepage-student')
                elif user.is_department:
                    return redirect('landing_page:homepage-department')
    else:
        form = LoginForm()
    return render(request, 'landing_page/login.html', {'form': form})