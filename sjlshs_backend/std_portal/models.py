from django.db import models
from accounts.models import StudentUser


# Create your models here.


class Student(models.Model):
    LRN = models.TextField()
    Name = models.TextField()
    Age = models.TextField()
    Section = models.TextField()
    Sex = models.TextField(default="Undetermined")

sections = (
    (1, "Microsoft"),
    (2, "Python"),
    (3, "Java"),
    (4, "Oracle")
)

class Post(models.Model):
    Title = models.CharField(max_length=50)
    Body = models.TextField(null=True)
    Section = models.CharField(max_length=50, choices=sections)
    Published = models.DateTimeField()

    def __str__(self):
        return self.Title

class Grades1stSem(models.Model):
    pr2 = models.SmallIntegerField(default=0)
    cpar = models.SmallIntegerField(default=0)
    pe = models.SmallIntegerField(default=0)
    spec = models.SmallIntegerField(default=0)
    ucsp = models.SmallIntegerField(default=0)
    philo = models.SmallIntegerField(default=0)
    eapp = models.SmallIntegerField(default=0)
    lrn = models.ForeignKey(StudentUser, null=False, on_delete=models.CASCADE)

