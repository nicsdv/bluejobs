from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from .forms import ProfessorForm
from .forms import SectionForm
from .forms import CourseForm

from .models import Course, CourseSection, ProfessorRating

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

def course_select_view(request):
    course_selected = None
    courses = Course.objects.all()

    if request.method == "POST":
        course_selected = request.POST.get('courseSelected')
        courses = Course.objects.filter(course_code__exact=course_selected)

    context = {
        'course_selected': course_selected,
        'courses': courses
    }

    return render(request, 'professor_select/course-select.html', context)

def professor_list_view(request):
    course_selected = None
    professors = CourseSection.objects.all()
    professor_rating = ProfessorRating.objects.all()

    if request.method == 'POST':
        course_selected = request.POST.get('courseSelected')
        professors = CourseSection.professor_classes.filter(course__exact=course_selected)
        professor_rating = ProfessorRating.professor_ratings.get_average().filter(course__exact=course_selected)
    
    context = {
        'course_selected': course_selected,
        'professors': professors,
        'professor_rating': professor_rating
    }

    return render(request, 'professor_select/professor-list.html', context)

def professor_detail_view(request):
    professor_selected = None
    detail = ProfessorRating.objects.all()

    if request.method == 'POST':
        professor_selected = request.POST.get('professorSelected')
        detail = ProfessorRating.objects.filter(professor__exact=professor_selected)
        
    context = {
        'professor_selected': professor_selected,
        'detail': detail
    }

    return render(request,'professor_select/professor-details.html', context)