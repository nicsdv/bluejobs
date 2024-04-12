from django import forms
from professor_select.models import ProfessorRating
from rate_a_professor.models import Upvotes

class ProfessorRatingForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        rating_choices = [(x, x) for x in range (0, 11)]
        widgets = {
            'subject_matter_expertise': forms.Select(choices = rating_choices),
            'workload_management': forms.Select(choices = rating_choices),
            'grading_leniency': forms.Select(choices = rating_choices),
            'approachability': forms.Select(choices = rating_choices),
            'friendliness': forms.Select(choices = rating_choices)
        }
        exclude = ['professor', 'student']

class ProfessorUpvoteForm(forms.ModelForm):
    class Meta:
        model = Upvotes
        fields = ['rating']