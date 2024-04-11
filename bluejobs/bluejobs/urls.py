"""
URL configuration for bluejobs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bluejobs/', include('landing_page.urls', namespace="landing_page")),
    path('professor_select/', include('professor_select.urls', namespace="professor_select")),
    path('schedule_maker/', include('schedule_maker.urls', namespace="schedule_maker")),
    path('rate_professor/', include('rate_a_professor.urls', namespace="rate_a_professor")),
]
