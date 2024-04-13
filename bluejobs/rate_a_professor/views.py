from django.shortcuts import render, redirect
from .forms import ProfessorRatingForm, ProfessorUpvoteForm
from professor_select.models import Professor, ProfessorRating
from landing_page.models import Student

# Create your views here.

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
                return redirect('rate_a_professor:professor_list')
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
        rating = professor.ratings.all()
    
        args = {
            'professor': professor,
            'ratings': rating
        }

        upvoted_ratings = [upvote.rating for upvote in student.student_upvotes.filter(professor = professor)] 
        args['upvoted_ratings'] = upvoted_ratings

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

        query = rating.upvotes.get(professor = professor, rating = rating)
        query.delete()

        return redirect('professor_select:rating_list', professor.pk)
    
    else:
        return redirect('landing_page:home')