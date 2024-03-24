from django.urls import path
from .views import (
    course_select_view,
    professor_list_view,
    professor_detail_view,
    add_professor
)

urlpatterns = [
    path('course_select', course_select_view, name = 'course_select'),
    path('courses/<int:pk>/professors', professor_list_view, name = 'professor_list'),
    path('courses/<int:course>/professor/<int:pk>/details', professor_detail_view, name = 'professor_details'),
    path('courses/<int:course>/professor/<int:pk>/add', add_professor, name = 'add_professor')
]

app_name = "professor_select"