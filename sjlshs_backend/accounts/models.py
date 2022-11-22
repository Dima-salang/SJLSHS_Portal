from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class StudentUser(AbstractUser):
    lrn = models.PositiveBigIntegerField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    birthday = models.DateField()

    REQUIRED_FIELDS = ['lrn', 'birthday', 'age', 'email']

