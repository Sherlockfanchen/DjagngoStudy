from django.db import models

# Create your models here.

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    class Meta:
        db_table = "person"

class Student(models.Model):
    student_name = models.CharField(max_length=10)
    student_age = models.IntegerField()
    class Meta:
        db_table = "student"


