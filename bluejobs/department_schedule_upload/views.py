from django.shortcuts import render
from django.http import HttpResponse

'''
The following code declares the different Department Schedule Upload views. Views are subject to change 
throughout the course of the implementation.

Code written by: Nics, Lex, and Eldon
'''

def index(request):
    return HttpResponse('Hello World! This came from the Department Schedule Upload.')