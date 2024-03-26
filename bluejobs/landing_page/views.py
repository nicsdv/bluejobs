from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentSignUpForm, DepartmentSignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from .models import Student, Department

'''
The following code declares the different Landing Page views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics and Eldon
'''

def home(request):
    logout(request)
    return render(request, 'landing_page/home.html')

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
                    return redirect('landing_page:home')
            else:
                args = {
                    'form':LoginForm(),
                    'error': "Invalid Login credentials. Please try again."  
                }
                return render(request, 'landing_page/login.html', args)

    else:
        form = LoginForm()
        return render(request, 'landing_page/login.html', {'form': form})

class StudentHomepage(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_student:
            student = Student.objects.get(pk = request.user.pk)
            return render(request, 'landing_page/homepage-student.html', { 'user' : student})
        else:
            return redirect('landing_page:home')
    
class DepartmentHomepage(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_department:
            department = Department.objects.get(pk = request.user.pk)
            return render(request, 'landing_page/homepage-department.html', { 'user' : department})
        else:
            return redirect('landing_page:home')

# The following views are currently in progress. They will be developed in the future iterations.

def about(request):
    return render(request, 'landing_page/about.html')

def help(request):
    return render(request, 'landing_page/help.html')

def developers(request):
    return render(request, 'landing_page/developers.html')