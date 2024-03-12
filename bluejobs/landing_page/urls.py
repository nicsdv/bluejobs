from django.urls import path
from . import views
from .views import StudentHomepage
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('help/', views.help, name = 'help'),
    path('developers/', views.developers, name = 'developers'),
    path('student_homepage/', StudentHomepage.as_view(), name = 'student_homepage'),    
    path('student/', views.student, name = "signup-student"),
    path('department/', views.department, name ="signup-department"),
    path('login/', LoginView.as_view(
        template_name='landing_page/login.html'), name='login'),
    path('signup/', views.signup, name = 'signup'),
]

app_name = "landing_page"

