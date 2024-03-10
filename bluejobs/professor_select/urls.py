from django.urls import path
from .views import index, professor_form_view, section_form_view, course_form_view

urlpatterns = [
    path('', index, name='index'),
    path('professor_form', professor_form_view, name = 'professor_form'),
    path('section_form', section_form_view, name = 'section_form'),
    path('course_form', course_form_view, name = 'course_form')
]

app_name = "professor_select"