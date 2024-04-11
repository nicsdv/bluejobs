from django.urls import path
from .views import (course_select_view, remove_course)

'''
The following code connects the app views to their corresponding url paths. These urls will be accessed
across different templates in the project. 

Code written by: Nics
'''

urlpatterns = [
    path('course_select', course_select_view, name = 'course_select'),    
    path('course/<int:pk>/remove', remove_course, name = 'course_remove'),
]

app_name = "schedule_maker"