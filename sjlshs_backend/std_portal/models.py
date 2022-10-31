from django.db import models

# Create your models here.


class Student(models.Model):
    LRN = models.TextField()
    Name = models.TextField()
    Age = models.TextField()
    Section = models.TextField()
    Sex = models.TextField(default="Undetermined")

