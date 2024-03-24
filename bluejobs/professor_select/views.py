from django.shortcuts import render, redirect
from django.http import HttpResponse

from landing_page.models import Student
from django.db.models import Avg

from .forms import CourseSelectForm, ProfessorFavoriteForm

from .models import Course, Professor, ProfessorRating

def course_select_view(request):
    if request.user.is_authenticated and request.user.is_student:

        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        if request.method  == "POST":
            course = request.POST['course_list_select']
            
            course_form = CourseSelectForm()
            
            course_selected = course_form.save(False)
            course_selected.course = Course.objects.get(course_code=course)
            course_selected.student = student
            course_selected.save()
        

        args = {
            'current_user': current_user,
            'form': CourseSelectForm
        }

        added_courses = [course.course for course in student.courses.all()] 
        args['added_courses'] = added_courses

        course_selection = []
        for course in Course.objects.all():
            if course not in added_courses:
                course_selection.append(course)
        
        args['course_selection'] = course_selection

        return render(request, 'professor_select/course-select.html', args)
    else:
        return redirect('landing_page:home')

def professor_list_view(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        course_selected = Course.objects.get(pk=kwarg['pk'])
        professors = course_selected.classes.all()
        print(professors)
    
        args = {
            'course_selected': course_selected,
            'professors': professors,
            'user': student
        }

        return render(request, 'professor_select/professor-list.html', args)
    else:
        return redirect('landing_page:home')

def professor_detail_view(request, course, **kwarg) :
    
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        professor = Professor.objects.get(pk=kwarg['pk'])

        args = {
            'professor': professor,
            'user': student,
            'course_selected': Course.objects.get(pk=course)
        }

        if len(professor.professor_ratings.all()) > 0:
            comment = professor.professor_ratings.all()[0].comment
            scores = professor.professor_ratings.aggregate(Avg('subject_matter_expertise'), 
                    Avg('workload_management'), Avg('grading_leniency'),
                    Avg('approachability'), Avg('friendliness'))
            
            args['comment'] = comment,            
            args['expertise'] =  round(scores['subject_matter_expertise__avg'], 2),
            args['workload'] = round(scores['workload_management__avg'], 2),
            args['grading'] = round(scores['grading_leniency__avg'], 2),
            args['approachability'] = round(scores['approachability__avg'], 2),
            args['friendliness'] = round(scores['friendliness__avg'], 2)

        else:
            args['comment'] = "No Ratings for this professor."
            
        return render(request,'professor_select/professor-details.html', args)
    else:
        return redirect('landing_page:home')
    
def add_professor (request, course, **kwarg):
    
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
        
        return redirect('professor_select:course_select')
    else:
        return redirect('landing_page:home')
    