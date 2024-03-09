from django.db import models


'''
The following code initializes the django models for the user credentials. It declares the entities as 
model classes, which will be accessed and used by all apps across the project. During the course of 
development, libraries may be imported and/or removed as needed.

(Note: django automatically designates primary keys as 'pk' so it need not be explicitly declared)

Code written by: Nics
'''

# STUDENT (Student_ID, Name, Email, degree_program)
class Student (models.Model):
    student_ID = models.IntegerField(unique = True)
    student_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    degree_program = models.CharField(max_length = 255)

    def __str__(self):
        return '{}: {}'.format(self.student_ID, self.student_name)

# STUDENT_LOGIN (Student_ID, password)
class StudentLogin (models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, primary_key = True)
    password = models.CharField(max_length = 255) 
    # stored password will be hashed for encryption

    def __str__(self):
        return '{}'.format(self.student.student_ID)

# DEPARTMENT (Department_ID, Department_Name, Email)
class Department(models.Model):
    department_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

    def __str__(self):
        return '{} Department'.format(self.department_name)

# DEPARTMENT_LOGIN (Department_Username, Department_ID, password)
class DepartmentLogin (models.Model):
    department_username = models.CharField(max_length = 15)
    department = models.OneToOneField(Department, on_delete = models.CASCADE, primary_key = True)
    password = models.CharField(max_length = 255) 
    # stored password will be hashed for encryption

    def __str__(self):
        return '{}'.format(self.department.username)
