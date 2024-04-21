from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Sum
from .forms import ProfessorRatingForm, ProfessorUpvoteForm
from professor_select.models import Professor, ProfessorRating
from landing_page.models import Student
from .models import *

'''
The following code declares the different Rate A Professor views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics, Lex, and Eldon
'''

def professor_list(request):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user

        professors = Professor.objects.all()
        return render(request, 'rate_a_professor/professor_list.html', {'professors': professors})

    else:
        return redirect('landing_page:home')
    
def rate_professor(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        professor = Professor.objects.get(pk=kwarg['pk'])
        if request.method == 'POST':
            form = ProfessorRatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.professor = professor
                rating.student = student
                rating.save()
                return redirect('rate_a_professor:rating_list', professor.pk)
        else:
            form = ProfessorRatingForm()
        return render(request, 'rate_a_professor/rating_form.html', {'professor': professor, 'form': form})
    
    else:
        return redirect('landing_page:home')
    
def rating_list(request, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        professor = Professor.objects.get(pk=kwarg['pk'])
        ratings = professor.ratings.all()

        sort_by = request.GET.get('sort_by')
        if sort_by == 'date_newest':
            ratings = ratings.order_by('-rating_date_time')
        elif sort_by == 'date_oldest':
            ratings = ratings.order_by('rating_date_time')
        elif sort_by == 'upvotes_most':
            ratings = ratings.annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
        elif sort_by == 'upvotes_least':
            ratings = ratings.annotate(upvote_count=Count('upvotes')).order_by('upvote_count')
        elif sort_by == 'rating_highest':
            ratings = sorted(ratings.all(), key=lambda t: t.get_average)[::-1]
        elif sort_by == 'rating_lowest':
            ratings = sorted(ratings.all(), key=lambda t: t.get_average)
    
        args = {
            'professor': professor,
            'ratings': ratings
        }

        upvoted_ratings = upvotes_by_professor(student, professor)
        args['upvoted_ratings'] = upvoted_ratings
        print(upvoted_ratings)

        return render(request, 'rate_a_professor/rating_list.html', args)
    
    else:
        return redirect('landing_page:home')
    
def add_rating(request, professor, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)
 
        professor = Professor.objects.get(pk=professor)
        rating = professor.ratings.get(pk=kwarg['pk'])

        upvote = ProfessorUpvoteForm().save(False)
        upvote.student = student
        upvote.rating = rating
        upvote.save()
        
        return redirect('rate_a_professor:rating_list', professor.pk)

    else:
        return redirect('landing_page:home')
    
def remove_rating(request, professor, **kwarg):
    if request.user.is_authenticated and request.user.is_student:
        current_user = request.user
        student = Student.objects.get(pk = current_user.pk)

        professor = Professor.objects.get(pk=professor)
        rating = professor.ratings.get(pk=kwarg['pk'])

        query = Upvotes.objects.get(rating = rating, student = student)
        query.delete()

        return redirect('rate_a_professor:rating_list', professor.pk)
    
    else:
        return redirect('landing_page:home')