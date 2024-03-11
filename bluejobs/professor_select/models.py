from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from landing_page.models import Student, Department

'''
The following code initializes the django models for the professor select. It declares the entities as 
model classes, which will be accessed and used by all apps across the project. During the course of 
development, libraries may be imported and/or removed as needed.

(Note: django automatically designates primary keys as 'pk' so it need not be explicitly declared)

Code written by: Nics
'''

# PROFESSOR (Professor_ID, Name, Email)
class Professor (models.Model):
    professor_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique = True)

    def __str__(self):
        return '{}'.format(self.professor_name)

# SECTION_SCHEDULE (Section, Day_Schedule, Time_Schedule)
class SectionSchedule (models.Model):
    section_code = models.CharField(max_length = 10)
    day_schedule = models.CharField(max_length = 20)
    time_schedule = models.CharField(max_length = 20)
    
    def __str__(self):
        return '{}: {} at {}'.format(self.section_code, self.day_schedule, self.time_schedule)

# COURSE (Course_Code, Course_Title)
class Course (models.Model):
    course_code = models.CharField(max_length = 20, unique = True)
    course_title = models.CharField(max_length = 255)

    def __str__(self):
        return '{}: {}'.format(self.course_code, self.course_title)

# COURSE_SECTION (Course_Code, Section, Professor_ID, Department_ID, Slots, Venue)
class CourseSection (models.Model):
    course = models.ForeignKey(Course, related_name = "course_sections",
                                on_delete = models.CASCADE)
    section = models.ForeignKey(SectionSchedule, related_name = "course_schedule",
                                on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, related_name = "professor_classes",
                                on_delete = models.CASCADE)
    department = models.ForeignKey(Department, related_name = "department_classes",
                                on_delete = models.CASCADE)
    slots = models.PositiveIntegerField()
    venue = models.CharField(max_length = 255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'section'], name='course_section')
        ]

    def __str__(self):
        return '{} {}: {} '.format(self.course, self.section.section_code, self.professor)
    
    def get_professor(self):
        return self.professor

# COURSE_SECTION_STUDENT (Course_Code,Section, Student_ID)
class CourseSectionStudent (models.Model):
    course_section = models.ForeignKey(CourseSection, related_name = "class_students",
                                on_delete = models.CASCADE)
    student = models.ForeignKey(Student, related_name = "student_courses",
                                on_delete = models.CASCADE)
    
    def __str__(self):
        return '{} Available Slots: {} '.format(self.course_section, self.course_section.slots)

'''
PROFESSOR_RATING(Student_ID, Professor_ID, Course_Code, Subject_Matter_Expertise, 
    Workload_Management, Grading_Leniency, Approachability, Friendliness, Comment)

    Note: the integer fields will have a corresponding dropdown for scoring 1-10
    for their input fields
'''
class ProfessorRating (models.Model):
    student = models.ForeignKey (Student, related_name = "student_reviews",
                                 on_delete = models.CASCADE)
    professor = models.ForeignKey (Professor, related_name = "professor_ratings",
                                 on_delete = models.CASCADE)
    course = models.ForeignKey (Course, related_name = "student_reviews",
                                 on_delete = models.CASCADE)
    subject_matter_expertise = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    workload_management = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    grading_leniency = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    approachability = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    friendliness = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)])
    comment = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'professor', 'course'], name='student_rating')
        ]

    def __str__(self):
        return 'Rating for {} in {} '.format(self.professor, self.course)
    
    def get_average(self):
        average = (self.subject_matter_expertise + self.workload_management + self.grading_leniency + self.approachability + self.friendliness)/4
        return average

class ProfessorFavorite(models.Model):
    professor = models.ForeignKey (Professor, on_delete = models.CASCADE)
    course = models.ForeignKey (Course, on_delete = models.CASCADE)
    student = models.ForeignKey (Student, related_name = "favorites",
                                 on_delete = models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'professor', 'course'], name='student_favorite')
        ]

    def __str__(self):
        return '{} for {} marked Favorite by {} '.format(self.professor, self.course, self.student)
