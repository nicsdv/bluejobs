from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import StudentForm, StudentLogin

def index(request):
    return HttpResponse('Hello World! This came from the Landing Page.')

class StudentHomepage(View):
    def get(self, request):
        return render(request, 'landing_page/student-homepage.html', {'name': 'Home'})
    
