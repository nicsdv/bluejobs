from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

'''
The following code initializes the admin panel for the rate a professor. 
This will help keep track of the existing instances of the entities and 
modify them when necessary.

Code written by: Nics, Lex and Eldon
'''

admin.site.register(Upvotes)