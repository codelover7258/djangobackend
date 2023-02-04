from django.db import models

# Create your models here.
class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_email = models.CharField(max_length=100)