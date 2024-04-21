from django.db import models
from landing_page.models import Student
from professor_select.models import *

'''
The following code initializes the django models for the schedule maker. It declares the entities as 
model classes, which will be accessed and used by all apps across the project. During the course of 
development, libraries may be imported and/or removed as needed.

(Note: django automatically designates primary keys as 'pk' so it need not be explicitly declared)

Code written by: Nics
'''

# REQUIRED_COURSE (Course_Code, Student_ID)
class RequiredCourse (models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, related_name = "required_courses",
                                on_delete = models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['course', 'student'], name = 'required_course')
        ]

    def __str__(self):
        return '{} Selected: {} '.format(self.student, self.course)
    
    @property
    def preferred_classes(self):
        favorites = ProfessorFavorite.objects.filter(student = self.student, course = self.course)
        favorites = [favorite.professor for favorite in favorites]
        return list(self.course.classes.filter(professor__in = favorites))
    
    @property
    def get_selected_class(self):
        query = self.student.classes.all()
        for classes in query:
            if classes.course_section.course == self.course:
                return classes.course_section
        return ""


# STUDENT_SCHEDULE (Course_Section,  Student_ID)
class StudentSchedule (models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "classes")
    course_section = models.ForeignKey(CourseSection, on_delete = models.CASCADE, related_name = "students")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_section', 'student'], name = 'student_schedule')
        ]
    
    def __str__(self):
        return '{} Selected: {} '.format(self.student, self.course_section)
    
    def get_added_courses(self):
        return self.objects.filter(student = self.student)
