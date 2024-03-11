from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, StudentLogin

def index(request):
    return HttpResponse('Hello World! This came from the Landing Page.')
