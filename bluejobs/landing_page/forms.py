from django import forms
from .models import Student, Department
from django.contrib.auth.forms import UserCreationForm

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ('email','student_ID', 'student_name', 'degree_program')

class DepartmentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Department
        fields = ('email','department_ID', 'department_name')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)