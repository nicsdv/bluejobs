from django.urls import path
from . import views
from .views import StudentHomepage, DepartmentHomepage, student_signup, department_signup, user_login

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('help/', views.help, name = 'help'),
    path('developers/', views.developers, name = 'developers'),
    path('student_homepage/', StudentHomepage.as_view(), name = 'homepage-student'),    
    path('department_homepage/', DepartmentHomepage.as_view(), name = 'homepage-department'),    
    path('signup/', views.signup, name = 'signup'),
    path('signup/student/', student_signup, name ='signup-student'),
    path('signup/department/', department_signup, name='signup-department'),
    path('login/', user_login, name='login'),
]

app_name = "landing_page"

