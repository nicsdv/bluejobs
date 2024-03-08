from django.db import models


'''
The following code initializes the django models for the database. It declares all entities as 
model classes, which will be accessed and used by all apps across the project. During the course of 
development, libraries may be imported and/or removed as needed.

(Note: django automatically designates primary keys as 'pk' so it need not be explicitly declared)

Code written by: Nics
'''

# STUDENT (Student_ID, Name, Email, degree_program)
class Student (models.Model):
    student_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    degree_program = models.CharField(max_length = 255)

# STUDENT_LOGIN (Student_ID, password)
class StudentLogin (models.Model):
    student = models.ForeignKey(Student, related_name = "student_login", 
                                on_delete = models.CASCADE)
    password = models.CharField(max_length = 255) 
    # stored password will be hashed for encryption

# DEPARTMENT (Department_ID, Department_Name, Email)
class Department(models.Model):
    department_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

# DEPARTMENT_LOGIN (Department_ID, password)
class DepartmentLogin (models.Model):
    department = models.ForeignKey(Student, related_name = "department_login", 
                                on_delete = models.CASCADE)
    password = models.CharField(max_length = 255) 
    # stored password will be hashed for encryption

# PROFESSOR (Professor_ID, Name, Email)
class Professor (models.Model):
    professor_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

# SECTION_SCHEDULE (Section, Day_Schedule, Time_Schedule)
class SectionSchedule (models.Model):
    section_code = models.CharField(max_length = 5)
    day_schedule = models.CharField(max_length = 5)
    time_schedule = models.CharField(max_length = 10)
    
# Course (Course_Code, Section, Professor_ID, Department_ID, Slots, Venue)
class Course (models.Model):
    course_code = models.CharField(max_length = 255)
    section = models.ForeignKey(SectionSchedule, related_name = "class_sections",
                                on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, related_name = "professor_classes",
                                on_delete = models.CASCADE)
    department = models.ForeignKey(Department, related_name = "department_classes",
                                on_delete = models.CASCADE)
    slots = models.PositiveBigIntegerField()
    venue = models.CharField(max_length = 255)

# CLASS_SECTION_STUDENT(Course_Code,Section, Student_ID)
class ClassStudent (models.Model):
    course = models.ForeignKey(Course, related_name = "class_students",
                                on_delete = models.CASCADE)
    student = models.ForeignKey(Student, related_name = "student_courses",
                                on_delete = models.CASCADE)

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