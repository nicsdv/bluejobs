from django.forms import ModelForm
from .models import Student, StudentLogin, Department, DepartmentLogin

class StudentForm(ModelForm):
    class Meta:
        model = Student, StudentLogin
        fields = ['student_ID', 'student_name', 'email', 'degree_program',s]
    
class StudentSignupForm(ModelForm):
    class Meta:
        model = StudentLogin
        fields = ['password1','password2',]

class StudentLoginForm(ModelForm):
    class Meta:
        model = StudentLogin
        fields = ['student_ID','password',]

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'email', 'degree_program',]
    
class DepartmentSignupForm(ModelForm):
    class Meta:
        model = DepartmentLogin
        fields = ['password1','password2',]

class DepartmentLoginForm(ModelForm):
    class Meta:
        model = DepartmentLogin
        fields = ['department_username','password',]