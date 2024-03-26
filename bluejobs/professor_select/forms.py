from django import forms

from .models import CourseStudent, ProfessorFavorite

'''
The following code initializes the admin panel for the user credentials in the system. 
This will help keep track of the existing instances of the entities and 
modify them when necessary.

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