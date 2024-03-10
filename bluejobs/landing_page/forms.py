from django.forms import ModelForm
from .models import Student, StudentLogin, Department, DepartmentLogin

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_ID', 'student_name', 'email', 'degree_program']
    
class StudentSignupForm(ModelForm):
    class Meta:
        model = StudentLogin
        fields = ['password']

class StudentLoginForm(ModelForm):
    class Meta:
        model = StudentLogin
        fields = ['password']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'email']
    
class DepartmentSignupForm(ModelForm):
    class Meta:
        model = DepartmentLogin
        fields = ['department_username','password']

class DepartmentLoginForm(ModelForm):
    class Meta:
        model = DepartmentLogin
        fields = ['department_username','password']