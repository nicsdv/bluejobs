from django.shortcuts import render, redirect
from django.http import HttpResponse
from landing_page.models import *
from professor_select.models import *
from .forms import *
import pandas as pd

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
    

'''
source: 
https://stackoverflow.com/questions/55895975/reading-uploaded-csv-file-into-pandas-dataframe 
'''    
def upload_classes(request):
    if request.user.is_authenticated and request.user.is_department:
        current_user = request.user
        department = Department.objects.get(pk = current_user.pk)
        args = {
            'user': department,
        }
        
        # checks if a course add form was submitted
        if request.method  == "POST":

            # loading uploaded csv file as pandas dataframe to extract classes 
            file = request.FILES['file']
            classes = pd.read_csv(file)

            # saving every instance of course and section ['Course', 'Section', 'Professor', 'Slots', 'Venue']
            for index, row in classes.iterrows():

                # try-except block in case an entry does not exist 
                try:
                    course = Course.objects.get(course_code = row['Course'])
                    section = SectionSchedule.objects.get(section_code = row['Section'])
                    professor = Professor.objects.get(professor_name = row['Professor'])
                    slots = row['Slots']
                    venue = row['Venue']

                    # check if the course section already exists. if yes, update details instead
                    if CourseSection.objects.get(course = course, section = section):
                        schedule = CourseSection.objects.get(course = course, section = section)
                        schedule.professor = professor
                        schedule.slots = slots
                        schedule.venue = venue
                        schedule.save()
                    
                    else:
                        # saving instance given that all needed objects in foreign keys exist
                        schedule = CourseSection(course = course, section = section, professor = professor,
                                    slots = slots, venue = venue)
                        schedule.save()

                except Exception as x:
                    print("Instance does not exist.\n",x)
  
            return (redirect ('department:class-list'))
        
        return render(request, 'department_schedule_upload/schedule-upload.html', args)
    
    else:
        return redirect('landing_page:home')
