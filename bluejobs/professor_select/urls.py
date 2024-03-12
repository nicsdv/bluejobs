from django.urls import path
from .views import (
    course_select_view,
    professor_list_view,
    professor_detail_view
)

urlpatterns = [
    path('course_select', course_select_view, name = 'course_select'),
    path('professor_list', professor_list_view, name = 'professor_list'),
    path('professor_detail', professor_detail_view, name = 'professor_detail')
]

app_name = "professor_select"