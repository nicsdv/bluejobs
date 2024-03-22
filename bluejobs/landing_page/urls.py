from django.urls import path
from .views import (StudentHomepage, DepartmentHomepage, student_signup, department_signup, user_login,
home, about, help, developers, signup)

urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name = 'about'),
    path('help/', help, name = 'help'),
    path('developers/', developers, name = 'developers'),
    path('student_homepage/', StudentHomepage.as_view(), name = 'homepage-student'),    
    path('department_homepage/', DepartmentHomepage.as_view(), name = 'homepage-department'),    
    path('signup/', signup, name = 'signup'),
    path('signup/student/', student_signup, name ='signup-student'),
    path('signup/department/', department_signup, name='signup-department'),
    path('login/', user_login, name='login'),
]

app_name = "landing_page"

