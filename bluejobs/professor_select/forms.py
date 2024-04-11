from django import forms

from .models import CourseStudent, ProfessorFavorite

'''
The following code initializes the forms for selecting a course and setting a professor
as favorite.

Code written by: Nics and Lex
'''

class CourseSelectForm(forms.ModelForm):
    class Meta:
        model = CourseStudent
        fields = ['course']

class ProfessorFavoriteForm(forms.ModelForm):
    class Meta:
        model = ProfessorFavorite
        fields = ['professor', 'course']