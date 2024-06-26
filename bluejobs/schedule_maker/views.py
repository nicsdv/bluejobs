from django.shortcuts import render, redirect
from landing_page.models import *
from django.db.models import Avg
from professor_select.models import *
from .models import *
from .forms import *

# Create your views here.

'''
The following code declares the different Schedule Maker views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics 
'''

def course_select_view(request):
    if request.user.is_authenticated and request.user.is_student:

        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        # checks if a course add form was submitted
        if request.method  == "POST":
            course = request.POST['course_list_select']
            
            course_form = CourseSelectForm()
            
            course_selected = course_form.save(False)
            course_selected.course = Course.objects.get(course_code=course)
            course_selected.student = student
            course_selected.save()
        
        args = {
            'current_user': current_user,
            'form': CourseSelectForm,
            'user': student,
        }

        added_courses = [course.course for course in student.required_courses.all()] 
        args['added_courses'] = added_courses

        # filters the selected courses for the course select form options
        course_selection = []
        
        for course in student.courses.all():
            if course.course not in added_courses:
                course_selection.append(course.course)
        
        args['course_selection'] = course_selection

        if course_selection == []:
            args['disabled'] = True

        return render(request, 'schedule_maker/schedule-courses.html', args)
    
    else:
        return redirect('landing_page:home')
    
def remove_course(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        
        course = Course.objects.get(pk=kwarg['pk'])
        
        # remove course from list of courses for the schedule
        course_delete = student.required_courses.get(course=course)
        course_delete.delete()

        # delete the course in the student's schedule
        [classes.delete() for classes in student.classes.all() if 
            classes.course_section.course == course]
        
        return redirect('schedule_maker:course_select')
    else:
        return redirect('landing_page:home')
    
def create_schedule(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        args = { 'student': student }

        if request.method  == "POST" and request.POST.get('class_select', False):
                class_section = request.POST['class_select']
                
                course_form = SectionSelectForm()
                course_section = CourseSection.objects.get(pk=class_section)
                
                class_selected = course_form.save(False)
                class_selected.student = student
                class_selected.course_section = course_section
                
                # remove previously-selected course section to avoid duplicate classes for one course
                existing_classes = [classes for classes in student.classes.all() 
                                    if classes.course_section.course == course_section.course]
                
                [section.delete() for section in existing_classes if section != class_selected]

                class_selected.save()

                added_classes = [classes.course_section for classes in student.classes.all().order_by('course_section')]
                sections = [classes.section.section_letter for classes in added_classes]

                args['added_classes'] = added_classes
                args['sections'] = sections
            
        else:        
            added_classes = [classes.course_section for classes in student.classes.all().order_by('course_section')]
            sections = [classes.section.section_letter for classes in added_classes]
            args['added_classes'] = added_classes
            args['sections'] = sections
                
        return render(request, 'schedule_maker/schedule-create.html', args)
    
    else:
        return redirect('landing_page:home')

def reset_schedule(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        
        [section.delete() for section in student.classes.all()]
        return redirect('schedule_maker:create-schedule')
    
    else:
        return redirect('landing_page:home')
    
def reset_class(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        course = Course.objects.get(pk=kwarg['pk'])

        [classes.delete() for classes in student.classes.all() if classes.course_section.course == course] 
        
        return redirect('schedule_maker:create-schedule')
    
    else:
        return redirect('landing_page:home')

def display_schedule(request):    
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        args = {}

        for classes in student.classes.all():
            index = classes.course_section.section.section_letter
            args[index] = classes.course_section
        
        return render(request, 'schedule_maker/schedule-display.html', args)

    else:
        return redirect('landing_page:home')
