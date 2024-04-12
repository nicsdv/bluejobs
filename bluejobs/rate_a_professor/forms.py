from django import forms
from professor_select.models import ProfessorRating

class ProfessorRatingForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        exclude = ['professor', 'student', 'course']