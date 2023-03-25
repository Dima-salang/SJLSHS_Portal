from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings




# Create your models here.

class TrackAndStrand(models.Model):
    strand = models.CharField(max_length=100)

    def __str__(self):
        return self.strand

class StudentYear(models.Model):
    Grade_Year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Grade_Year)


class StudentSection(models.Model):
    section_id = models.IntegerField()
    section = models.CharField(max_length=20)
    section_adviser = models.ForeignKey('TeacherUser', null=True,
    on_delete=models.SET_NULL, blank=True)
    room_num = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.section

class Subject(models.Model):
    subject_matter = models.CharField(max_length=50)
    grade_year = models.ForeignKey(StudentYear, null=True,
    on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.subject_matter} - {self.grade_year}"



class Db_Students(models.Model):

    lrn = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    strand = models.ForeignKey(TrackAndStrand, null=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    birthday = models.DateField()
    grade_year = models.ForeignKey(StudentYear, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(StudentSection, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.lrn} - {self.last_name}, {self.first_name} ({self.section})"

class StudentUser(AbstractUser):

    queryset = Db_Students.objects.all()

    lrn = models.CharField(max_length=15)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    birthday = models.DateField()
    image_id = models.ImageField(upload_to='media/image_id', null=True, blank=True)
    grade_year = models.ForeignKey(StudentYear, null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(StudentSection, null=True, on_delete=models.SET_NULL, blank=True)
    strand =models.ForeignKey(TrackAndStrand, null=True, on_delete=models.SET_NULL, blank=True)
    is_email_verified = models.BooleanField(null=True, blank=True)

    REQUIRED_FIELDS = ['lrn', 'age', 'email', 'birthday']
                
    def __str__(self):
        return f"{self.lrn} - {self.last_name}, {self.first_name} ({self.section})"

class TeacherUser(models.Model):
    user_field = models.OneToOneField(StudentUser, on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.PositiveSmallIntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_num = models.PositiveBigIntegerField()
    section_handle = models.ManyToManyField(StudentSection, blank=True)
    subject_handle = models.ManyToManyField(Subject, blank=True )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    

    def get_students(self):
        sections = self.section_handle.all()
        if sections:
            return StudentUser.objects.filter(section__in=sections)
        else:
            return StudentUser.objects.none()








