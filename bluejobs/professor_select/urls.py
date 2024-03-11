from django.urls import path
from .views import (
    index, 
    professor_form_view, 
    section_form_view, 
    course_form_view,
    course_select_view,
    professor_list_view,
    professor_detail_view
)

urlpatterns = [
    path('', index, name='index'),
    path('professor_form', professor_form_view, name = 'professor_form'),
    path('section_form', section_form_view, name = 'section_form'),
    path('course_form', course_form_view, name = 'course_form'),
    path('course_select', course_select_view, name = 'course_select'),
    path('professor_list', professor_list_view, name = 'professor_list'),
    path('professor_detail', professor_detail_view, name = 'professor_detail')
]

app_name = "professor_select"