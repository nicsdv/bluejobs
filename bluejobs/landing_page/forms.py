from django.forms import ModelForm
from .models import Student, Department

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_ID', 'student_name', 'email', 'degree_program']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'email']