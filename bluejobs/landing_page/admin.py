from django.contrib import admin
from landing_page.models import User, Student, Department

'''
The following code initializes the admin panel for the user credentials in the system. 
This will help keep track of the existing instances of the entities and 
modify them when necessary.

Code written by: Nics and Eldon
'''

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Department)