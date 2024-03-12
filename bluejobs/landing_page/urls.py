from django.urls import path
from . import views
from .views import StudentHomepage
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student_homepage', StudentHomepage.as_view(), name = 'student_homepage'),    
    path('', views.home, name = 'home'),
    path('student/', views.student, name = "signup-student"),
    path('department/', views.department),
    path('login/', LoginView.as_view(
        template_name='landing_page/login.html'), name='login'),
]

app_name = "landing_page"

