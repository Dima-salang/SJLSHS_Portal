from django.db import models

# Create your models here.


class Student(models.Model):
    LRN = models.TextField()
    Name = models.TextField()
    Age = models.TextField()
    Section = models.TextField()
    Sex = models.TextField(default="Undetermined")

sections = (
    ("Microsoft", "Microsoft"),
    ("Python", "Python"),
    ("Java", "Java"),
    ("Oracle", "Oracle")
)

class Post(models.Model):
    Title = models.CharField(max_length=50)
    Body = models.TextField(null=True)
    Section = models.CharField(max_length=50, choices=sections)
    Published = models.DateTimeField()

    def __str__(self):
        return self.Title