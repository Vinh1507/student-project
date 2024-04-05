from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, null=True)
    username = models.CharField(default='hello', max_length=200)
    password = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name
    
class Lecturer(models.Model):
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, null=True)
    username = models.CharField(default='hello', max_length=200)
    password = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name

