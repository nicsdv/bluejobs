from django.shortcuts import render, redirect
from landing_page.models import Student
from django.db.models import Avg
from .forms import CourseSelectForm, ProfessorFavoriteForm
from .models import Course, Professor


'''
The following code declares the different Professor Select views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics and Lex
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

        added_courses = [course.course for course in student.courses.all()] 
        args['added_courses'] = added_courses

        # filters the selected courses for the course select form options
        course_selection = []
        for course in Course.objects.all():
            if course not in added_courses:
                course_selection.append(course)
        
        args['course_selection'] = course_selection

        return render(request, 'professor_select/course-select.html', args)
    
    else:
        return redirect('landing_page:home')

def remove_course(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
        
        course = Course.objects.get(pk=kwarg['pk'])

        course_delete = student.courses.get(course=course)
        course_delete.delete()

        # delete list of professor favorites for the course
        for favorite in student.favorites.filter(course = course):
            favorite.delete()
        
        # also course as in required courses
        required = student.required_courses.filter(course = course)
        required.delete()


        return redirect('professor_select:course_select')
    else:
        return redirect('landing_page:home')


def professor_list_view(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        course_selected = Course.objects.get(pk=kwarg['pk'])
        professors = list(dict.fromkeys([course.professor for course in course_selected.classes.all()]))
    
        args = {
            'course_selected': course_selected,
            'professors': professors,
            'user': student,
            'selected': [favorite.professor for favorite in student.favorites.filter(course = course_selected)]
        }
        return render(request, 'professor_select/professor-list.html', args)
    
    else:
        return redirect('landing_page:home')

def professor_detail_view(request, course, **kwarg) :
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user

        student = Student.objects.get(pk = current_user.pk)
        professor = Professor.objects.get(pk=kwarg['pk'])
        course = Course.objects.get(pk=course)

        args = {
            'professor': professor,
            'user': student,
            'course_selected': course
        }

        if len(professor.professor_ratings.all()) > 0:
            comment = professor.professor_ratings.all()[0].comment
            scores = professor.professor_ratings.aggregate(Avg('subject_matter_expertise'), 
                    Avg('workload_management'), Avg('grading_leniency'),
                    Avg('approachability'), Avg('friendliness'))
            
            args['comment'] = comment            
            args['expertise'] =  round(scores['subject_matter_expertise__avg'], 2)
            args['workload'] = round(scores['workload_management__avg'], 2)
            args['grading'] = round(scores['grading_leniency__avg'], 2)
            args['approachability'] = round(scores['approachability__avg'], 2)
            args['friendliness'] = round(scores['friendliness__avg'], 2)
        
        else:
            args['comment'] = "No Ratings for this professor."

        ''' 
        the try-except fragment bellow checks if the professor has been added to student's favorites,
        catches when an empty query exception is raised 
        '''
        try:
            if student.favorites.get(professor=professor, course=course) is not None:
                args['is_added'] = True

        except Exception as x:
            print(x)
            args['is_added'] = False

        return render(request,'professor_select/professor-details.html', args)
    
    else:
        return redirect('landing_page:home')
    

def add_professor(request, course, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        course = Course.objects.get(pk=course)
        professor = Professor.objects.get(pk=kwarg['pk'])
 
        favorite = ProfessorFavoriteForm().save(False)
        favorite.student = student
        favorite.course = course
        favorite.professor = professor
        favorite.save()
        
        # reload the professsor details after setting professor as favorite
        return redirect('professor_select:professor_details', course.pk, professor.pk)

    else:
        return redirect('landing_page:home')

def remove_professor(request, course, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        course = Course.objects.get(pk=course)
        professor = Professor.objects.get(pk=kwarg['pk'])

        query = student.favorites.get(course = course, professor = professor)
        query.delete()

        # redirect to professor list after removing professor as favorite
        return redirect('professor_select:professor_details', course.pk, professor.pk)
    
    else:
        return redirect('landing_page:home')
