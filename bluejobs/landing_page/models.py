from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.utils import timezone


'''
The following code initializes the django models for the user credentials. It declares the entities as 
model classes, which will be accessed and used by all apps across the project. During the course of 
development, libraries may be imported and/or removed as needed.

(Note: django automatically designates primary keys as 'pk' so it need not be explicitly declared)

Code written by: Nics and Eldon
'''

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Creates and saves a User with the given email and password.
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Creates and saves a Superuser with the given email and password.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_department = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# STUDENT (Student_ID, Name, Email, degree_program)
class Student(User):
    student_ID = models.IntegerField(default=200000, null=False)
    student_name = models.CharField(max_length=255, null=False)
    degree_program = models.CharField(max_length=255, null=False)

    def save(self, *args, **kwargs):
        self.is_student = True
        self.student_ID = self.student_ID
        return super().save(*args, **kwargs)

# DEPARTMENT (Department_ID, Department_Name, Email)
class Department(User):
    department_name = models.CharField(max_length=255, null=False)

    def save(self, *args, **kwargs):
        self.is_department = True
        return super().save(*args, **kwargs)