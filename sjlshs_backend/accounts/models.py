from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class StudentSection(models.Model):
    section_id = models.IntegerField()
    section = models.CharField(max_length=20)

    def __str__(self):
        return self.section

class StudentUser(AbstractUser):
    lrn = models.IntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    birthday = models.DateField()
    section = models.ForeignKey(StudentSection, null=True, on_delete=models.SET_NULL)

    REQUIRED_FIELDS = ['lrn', 'birthday', 'age', 'email']

    def __str__(self):
        return str(self.lrn)


class TeacherUser(models.Model):
    teacher_id = models.IntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    section_handle = models.ManyToManyField(StudentSection)

    def __str__(self):
        return self.last_name

