from django import forms

from .models import CourseStudent

class CourseSelectForm(forms.ModelForm):
    class Meta:
        model = CourseStudent
        fields = ['course']