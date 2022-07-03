import email
from django.db import models

# Create your models here.
class Student(models.Model):
    level = (("one", "Year 1" ),
             ("two", "Year 2"),
             ("three", "Year 3"),
             ("four", 'Year 4'),)

    name = models.CharField(max_length=150)
    email = models.EmailField()
    level = models.CharField(max_length=50,choices=level, default='one')
    age = models.IntegerField()
    created = models.DateTimeField(auto_now=True)