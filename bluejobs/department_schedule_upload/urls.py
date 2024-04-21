from django.urls import path
from .views import *
'''
The following code connects the app views to their corresponding url paths. These urls will be accessed
across different templates in the project. 

Code written by: Nics
'''

urlpatterns = [
    path('index', index, name = 'index'),
    path('courses', department_classes, name="classes")
]

app_name = "department_schedule_upload"