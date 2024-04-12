from django.shortcuts import render, redirect
from .forms import ProfessorRatingForm
from professor_select.models import Professor

# Create your views here.

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'rate_a_professor/professor_list.html', {'professors': professors})

def rate_professor(request, **kwarg):
    professor = Professor.objects.get(pk=kwarg['pk'])
    if request.method == 'POST':
        form = ProfessorRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.professor = professor
            rating.save()
            return redirect('professor_list')
    else:
        form = ProfessorRatingForm()
    return render(request, 'rate_a_professor/rating_form.html', {'professor': professor, 'form': form})