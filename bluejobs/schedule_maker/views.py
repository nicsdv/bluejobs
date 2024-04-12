from django.shortcuts import render, redirect
from landing_page.models import Student
from django.db.models import Avg
from professor_select.models import Course, Professor
from .models import StudentSchedule
from .forms import CourseSelectForm

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
        
        print(added_courses)
        for course in student.courses.all():
            print(course.course)
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

        for favorite in student.favorites.filter(course = course):
            favorite.delete()
        
        return redirect('schedule_maker:course_select')
    else:
        return redirect('landing_page:home')
    
def create_schedule(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        args = { 'student':student }

        if request.method  == "POST":
            course = request.POST['class_select']
            
            course_form = CourseSelectForm()
            
            course_selected = course_form.save(False)
            course_selected.course = Course.objects.get(course_code=course)
            course_selected.student = student
            course_selected.save()



        return render(request, 'schedule_maker/schedule-create.html', args)
    
    else:
        return redirect('landing_page:home')
    