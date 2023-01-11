from django.db import models
from accounts.models import StudentUser, StudentSection, TeacherUser, StudentYear, Subject, Db_Students
from django.conf import settings
import math



# Create your models here.

class Post(models.Model):
    Author = models.CharField(max_length=50, null=True)
    Title = models.CharField(max_length=50)
    Body = models.TextField(null=True)
    Section = models.ForeignKey(StudentSection, null=True, on_delete=models.CASCADE)
    Published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Author} {self.Title}"


class Modules(models.Model):
    title = models.CharField(max_length=255)
    grade = models.ForeignKey(StudentYear, null=True, blank=True, on_delete=models.SET_NULL, related_name='grade')
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL, related_name='subject')
    thumbnail = models.ImageField(upload_to='media/modules/module_thumbnails', blank=True, null=True)
    file = models.FileField(upload_to=f"media/modules/")

    def __str__(self):
        return f"{self.title} - {self.grade}"

class Schedule(models.Model):
    section = models.OneToOneField(StudentSection, on_delete=models.CASCADE, related_name='sched_section')
    schedule_file = models.FileField(upload_to=f'media/schedules/', max_length=255)

    def __str__(self):
        return f"{self.section} Schedule"

