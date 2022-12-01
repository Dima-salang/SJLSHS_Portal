from django.db import models
from accounts.models import StudentUser, StudentSection, TeacherUser, StudentYear, Subject
from django.conf import settings



# Create your models here.

class Post(models.Model):
    Author = models.CharField(max_length=50, null=True)
    Title = models.CharField(max_length=50)
    Body = models.TextField(null=True)
    Section = models.ForeignKey(StudentSection, null=False, on_delete=models.CASCADE)
    Published = models.DateTimeField()

    def __str__(self):
        return f"{self.Author} {self.Title}"

class GradePost(models.Model):
    pr2 = models.SmallIntegerField(default=0)
    cpar = models.SmallIntegerField(default=0)
    pe = models.SmallIntegerField(default=0)
    spec = models.SmallIntegerField(default=0)
    ucsp = models.SmallIntegerField(default=0)
    philo = models.SmallIntegerField(default=0)
    eapp = models.SmallIntegerField(default=0)
    lrn = models.OneToOneField(StudentUser, null=False, on_delete=models.CASCADE, related_name='GradePost')

    def __str__(self):
        return str(self.lrn)

class Modules(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    grade = models.ForeignKey(StudentYear, null=True, blank=True, on_delete=models.SET_NULL, related_name='grade')
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL, related_name='subject')
    file = models.FileField(upload_to=f"media/modules/", max_length=100)

    def __str__(self):
        return f"{self.title} - {self.grade}"

class Schedule(models.Model):
    section = models.OneToOneField(StudentSection, on_delete=models.CASCADE, related_name='sched_section')
    schedule_file = models.FileField(upload_to=f'media/schedules/', max_length=255)

    def __str__(self):
        return f"{self.section} Schedule"

