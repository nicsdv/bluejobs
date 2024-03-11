from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email or len(email) <= 0:
            raise ValueError("Email is required!")
        if not password:
            raise ValueError("Password is required!")
        
        user = self.model(
            email = self.normalize_email(email),
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
    
class Student(User):
    base_role = User.Role.STUDENT
    objects = StudentManager()
    class Meta:
        proxy = True

class DepartmentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.DEPARTMENT)
        
class Department(User):
    base_role = User.Role.DEPARTMENT
    objects = DepartmentManager()
    class Meta:
        proxy = True