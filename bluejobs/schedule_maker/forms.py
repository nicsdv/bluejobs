from django import forms
from .models import RequiredCourse, StudentSchedule

'''
The following code initializes the form to add courses, professors, and creating schedules

Code written by: Nics and Lex
'''

class CourseSelectForm(forms.ModelForm):
    class Meta:
        model = RequiredCourse
        fields = ['course']

class SectionSelectForm(forms.ModelForm):
    class Meta:
        model = StudentSchedule
        fields = ['course_section']