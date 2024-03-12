from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student/', views.student),
    path('department/', views.department),
    path('login/', LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
]