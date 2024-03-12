from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse


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
    email = models.EmailField(max_length = 255, unique = True)
    degree_program = models.CharField(max_length = 255)

    def __str__(self):
        return '{}: {}'.format(self.student_ID, self.student_name)

# DEPARTMENT (Department_ID, Department_Name, Email)
class Department(models.Model):
    department_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique = True)

    def __str__(self):
        return '{} Department'.format(self.department_name)
    

# The following models are created for the user accounts of the departments and students

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("Email is required!")
        if not password:
            raise ValueError("Password is required!")
        
        user = self.model(
            email = self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
    
class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        DEPARTMENT = 'DEPARTMENT', 'Department'

    base_role = Role.STUDENT
    role = models.CharField(
        ('Role'), max_length=50, choices=Role.choices, default=base_role
    )

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username':self.username})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        return super().save(*args, **kwargs)

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.STUDENT)
    
class StudentUser(User):
    base_role = User.Role.STUDENT
    class Meta:
        proxy = True

class DepartmentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.DEPARTMENT)
        
class DepartmentUser(User):
    base_role = User.Role.DEPARTMENT
    objects = DepartmentManager()
    class Meta:
        proxy = True