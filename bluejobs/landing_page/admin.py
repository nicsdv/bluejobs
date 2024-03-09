from django.contrib import admin
from landing_page.models import Student, StudentLogin, Department, DepartmentLogin

'''
The following code initializes the admin panel for the user credentials in the system. This will help
keep track of the existing instances of the entities and modify them when necessary.

Code written by: Nics
'''

class StudentAdmin(admin.ModelAdmin):
    model = Student
    search_fields = ('student_ID', 'student_name', 'email', 'degree_program',)
    list_display = ('student_ID', 'student_name', 'email', 'degree_program',)
    list_filter = ('student_ID', 'student_name', 'email', 'degree_program',)

class StudentLoginAdmin(admin.ModelAdmin):
    model = StudentLogin
    search_fields = ('student',)
    list_display = ('student', 'password',)
    list_filter = ('student',)

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    search_fields = ('department_name', 'email',)
    list_display = ('department_name', 'email',)
    list_filter = ('department_name', 'email',)

class DepartmentLoginAdmin(admin.ModelAdmin):
    model = DepartmentLogin
    search_fields = ('department_username', 'department',)
    list_display = ('department_username', 'department', 'password',)
    list_filter = ('department_username', 'department',)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentLogin, StudentLoginAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentLogin, DepartmentLoginAdmin)