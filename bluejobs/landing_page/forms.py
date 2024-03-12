from django.forms import ModelForm
from django import forms
from .models import Student, Department
from django.contrib.auth.forms import UserCreationForm
from landing_page.models import User, StudentUser, Department

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_ID', 'student_name', 'email', 'degree_program']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'email']


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = StudentUser
        fields = ('email', 'username',)
        #fields = ('student_ID', 'student_name', 'email', 'degree_program')


    # class Meta(UserCreationForm.Meta):
    #     model = User

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     student.interests.add(*self.cleaned_data.get('interests'))
    #     return user
