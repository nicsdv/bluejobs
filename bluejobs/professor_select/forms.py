from django import forms

class ProfessorForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=255)
    email = forms.CharField(label='Email', max_length=255)

class SectionForm(forms.Form):
    section_code = forms.CharField(label='Section Code', max_length=255)
    days = forms.CharField(label='Day Schedule', max_length=20)
    time = forms.CharField(label='Time Schedule', max_length=20)

class CourseForm(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=20)
    course_title = forms.CharField(label='Course Title', max_length=255)