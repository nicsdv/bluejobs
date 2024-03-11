from django.urls import path
from .views import index, StudentHomepage

urlpatterns = [
    path('', index, name='index'),
    path('student_homepage', StudentHomepage.as_view(), name = 'student_homepage')
]

app_name = "landing_page"