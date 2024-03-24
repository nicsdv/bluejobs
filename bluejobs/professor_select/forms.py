from django import forms

from .models import CourseStudent, ProfessorFavorite

class CourseSelectForm(forms.ModelForm):
    class Meta:
        model = CourseStudent
        fields = ['course']

class ProfessorFavoriteForm(forms.ModelForm):
    class Meta:
        model = ProfessorFavorite
        fields = ['professor', 'course']