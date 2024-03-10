from django.db import models
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
    course = models.ForeignKey(SectionSchedule, related_name = "course_sections",
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

# COURSE_SECTION_STUDENT (Course_Code,Section, Student_ID)
class CourseSectionStudent (models.Model):
    course_section = models.ForeignKey(CourseSection, related_name = "class_students",
                                on_delete = models.CASCADE)
    student = models.ForeignKey(Student, related_name = "student_courses",
                                on_delete = models.CASCADE)
    
    def __str__(self):
        return '{} Available Slots: {} '.format(self.course_section, self.section.section_code, self.professor)

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
    subject_matter_expertise = models.PositiveIntegerField()
    workload_management = models.PositiveIntegerField()
    grading_leniency = models.PositiveIntegerField()
    approachability = models.PositiveIntegerField()
    friendliness = models.PositiveIntegerField()
    comment = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'professor', 'course'], name='student_rating')
        ]

    def __str__(self):
        return 'Rating for {} in {} '.format(self.professor, self.course)