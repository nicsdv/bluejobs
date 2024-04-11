from django.contrib import admin
from schedule_maker.models import RequiredCourse, StudentSchedule

'''
The following code initializes the admin panel for the user schedule maker. 
This will help keep track of the existing instances of the entities and 
modify them when necessary.

Code written by: Nics and Eldon
'''

admin.site.register(RequiredCourse)
admin.site.register(StudentSchedule)