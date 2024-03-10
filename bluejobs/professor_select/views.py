from django.shortcuts import render
from django.http import HttpResponse

from .forms import ProfessorForm
from .forms import SectionForm
from .forms import CourseForm

def index(request):
    return HttpResponse('Hello World! This came from the Professor Select index view.')

def professor_form_view(request):
    form = ProfessorForm()
    return render(request, 'index.html', {'form': form})

def section_form_view(request):
    form = SectionForm()
    return render(request, 'index.html', {'form': form})

def course_form_view(request):
    form = CourseForm()
    return render(request, 'index.html', {'form': form})