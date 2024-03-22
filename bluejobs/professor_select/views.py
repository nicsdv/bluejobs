from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from django.contrib.auth import login, authenticate, logout

from .forms import CourseSelectForm

from .models import Course, CourseSection, ProfessorRating

def course_select_view(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user

        context = {
            'current_user': current_user,
        }

        if request.method == "POST":
            select_course_form = CourseSelectForm(request.POST)

            if select_course_form.is_valid():
                selected_course = select_course_form.save(False)
                selected_course.student = current_user
                selected_course.save()
            
            courses = current_user.student_courses.all()
            context['courses'] = courses

        return render(request, 'professor_select/course-select.html', context)
    else:
        return redirect('landing_page:home')

def professor_list_view(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user

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
    else:
        return redirect('landing_page:home')

def professor_detail_view(request):
    
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
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
    else:
        return redirect('landing_page:home')