from django.forms import ModelForm
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Student
        fields = ('email', 'username', 'student_ID')



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
