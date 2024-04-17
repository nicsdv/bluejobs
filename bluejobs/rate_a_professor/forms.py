from django import forms
from professor_select.models import ProfessorRating
from rate_a_professor.models import Upvotes

class ProfessorRatingForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        exclude = ['professor', 'student', 'rating_date_time']

class ProfessorUpvoteForm(forms.ModelForm):
    class Meta:
        model = Upvotes
        fields = ['rating']