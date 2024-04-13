from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor_list, name='professor_list'),
    path('rate/<int:pk>/', views.rate_professor, name='rate_professor'),
    path('ratings/<int:pk>/', views.rating_list, name='rating_list'),
    path('rate/<int:professor>/<int:pk>/add', views.add_rating, name = 'add_rating'),
    path('rate/<int:professor>/<int:pk>/remove', views.remove_rating, name = 'remove_rating'),
]

app_name = 'rate_a_professor'