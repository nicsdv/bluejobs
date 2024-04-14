from django.urls import path
from .views import *

'''
The following code connects the app views to their corresponding url paths. These urls will be accessed
across different templates in the project. 

Code written by: Nics
'''

urlpatterns = [
    path('course_select', course_select_view, name = 'course_select'),    
    path('course/<int:pk>/remove', remove_course, name = 'course_remove'),
    path('schedule/create', create_schedule, name = 'create-schedule'),
    path('schedule/reset', reset_schedule, name = 'reset-schedule'),
    path('schedule/display', display_schedule, name = 'display-schedule'),

]

app_name = "schedule_maker"