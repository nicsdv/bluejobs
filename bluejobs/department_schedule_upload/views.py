from django.shortcuts import render, redirect
from django.http import HttpResponse
from landing_page.models import *
from professor_select.models import *

'''
The following code declares the different Department Schedule Upload views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics, Lex, and Eldon
'''

def index(request):
    return HttpResponse('Hello World! This came from the Department Schedule Upload.')

def department_classes(request):
    if request.user.is_authenticated and request.user.is_department:
        current_user = request.user
        department = Department.objects.get(pk = current_user.pk)
        args = {
            'user': department,
            'courses': department.department_classes.all()
        }

        return render(request, 'department_schedule_upload/department-classes.html', args)
    

    else:
        return redirect('landing_page:home')