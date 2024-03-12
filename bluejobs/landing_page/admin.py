from django.contrib import admin
from landing_page.models import Student, Department, User, StudentUser, DepartmentUser
'''
The following code initializes the admin panel for the user credentials in the system. This will help
keep track of the existing instances of the entities and modify them when necessary.

Code written by: Nics and Eldon
'''
''
class StudentAdmin(admin.ModelAdmin):
    model = Student
    search_fields = ('student_ID', 'student_name', 'email', 'degree_program',)
    list_display = ('student_ID', 'student_name', 'email', 'degree_program',)
    list_filter = ('student_ID', 'student_name', 'email', 'degree_program',)

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    search_fields = ('department_name', 'email',)
    list_display = ('department_name', 'email',)
    list_filter = ('department_name', 'email',)


admin.site.register(User)
admin.site.register(StudentUser)
admin.site.register(DepartmentUser)
admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)