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
    path('courses/<int:pk>/professors', professor_list_view, name = 'professor_list'),
    path('courses/<int:course>/professor/<int:pk>/details', professor_detail_view, name = 'professor_details'),
    path('courses/<int:course>/professor/<int:pk>/add', add_professor, name = 'add_professor'),
    path('courses/<int:course>/professor/<int:pk>/remove', remove_professor, name = 'remove_professor'),
]

app_name = "professor_select"