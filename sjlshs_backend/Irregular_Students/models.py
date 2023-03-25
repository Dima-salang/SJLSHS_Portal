from django.db import models
from accounts.models import Subject

# Create your models here.

class IrregularStudent(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, through='SubjectGrade')

class SubjectGrade(models.Model):
    student = models.ForeignKey(IrregularStudent, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)