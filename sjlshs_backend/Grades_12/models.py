from django.db import models
from accounts.models import StudentUser

# Create your models here.

class FirstSem_1stQ(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    PR2 = models.SmallIntegerField(default=0, null=True, blank=True)
    CPAR = models.SmallIntegerField(default=0, null=True, blank=True)
    PHILOSOPHY = models.SmallIntegerField(default=0, null=True, blank=True)
    UCSP = models.SmallIntegerField(default=0, null=True, blank=True)
    EAPP = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, related_name="firstsem1stq")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class FirstSem_2ndQ(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    PR2 = models.SmallIntegerField(default=0, null=True, blank=True)
    CPAR = models.SmallIntegerField(default=0, null=True, blank=True)
    PHILOSOPHY = models.SmallIntegerField(default=0, null=True, blank=True)
    UCSP = models.SmallIntegerField(default=0, null=True, blank=True)
    EAPP = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, related_name="firstsem2ndq")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class SecondSem_3rdQ(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    III = models.SmallIntegerField(default=0, null=True, blank=True)
    MIL = models.SmallIntegerField(default=0, null=True, blank=True)
    PE4 = models.SmallIntegerField(default=0, null=True, blank=True)
    IMMERSION = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, related_name="secondsem3rdq")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class SecondSem_4thQ(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    III = models.SmallIntegerField(default=0, null=True, blank=True)
    MIL = models.SmallIntegerField(default=0, null=True, blank=True)
    PE4 = models.SmallIntegerField(default=0, null=True, blank=True)
    IMMERSION = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, related_name="secondsem4thq")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"   