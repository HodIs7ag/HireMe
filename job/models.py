from django.db import models

'''
django model fileds:
    - html widget
    - validation
    - db size
'''

# Create your models here.
class Job(models.Model): #table
    title = models.CharField(max_length=100)    #column