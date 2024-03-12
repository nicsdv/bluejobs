from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
    return HttpResponse('Hello World! This came from the Landing Page.')

class StudentHomepage(View):
    def get(self, request):
        return render(request, 'landing_page/student-homepage.html', {'name': 'Home'})
    
def home(request):
    return render(request, 'landing_page/home.html')

def student(request):
    return render(request, 'landing_page/student.html')

def department(request):
    return render(request, 'landing_page/department.html')

def login(request):
    return render(request, 'landing_page/login.html')