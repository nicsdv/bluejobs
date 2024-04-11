from django.shortcuts import render, redirect
from landing_page.models import Student
from professor_select.models import Course
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
        for course in student.courses.all():
            if course not in added_courses:
                course_selection.append(course.course)
        
        args['course_selection'] = course_selection

        return render(request, 'schedule_maker/schedule-courses.html', args)
    
    else:
        return redirect('landing_page:home')