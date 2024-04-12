from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor_list, name='professor_list'),
    path('rate/<int:pk>/', views.rate_professor, name='rate_professor'),
]

app_name = 'rate_a_professor'