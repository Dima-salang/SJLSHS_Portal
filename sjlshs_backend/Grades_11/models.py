from django.db import models
from accounts.models import StudentUser

# Create your models here.

class FirstSem_1stQ_11(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    ORALCOMM = models.SmallIntegerField(default=0, null=True, blank=True)
    KOMUNIKASYON = models.SmallIntegerField(default=0, null=True, blank=True)
    GENMATH = models.SmallIntegerField(default=0, null=True, blank=True)
    ELS = models.SmallIntegerField(default=0, null=True, blank=True)
    PERDEV = models.SmallIntegerField(default=0, null=True, blank=True)
    LITERATURE = models.SmallIntegerField(default=0, null=True, blank=True)
    PR1 = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.SET_NULL, null=True, related_name="firstsem1stq11")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class FirstSem_2ndQ_11(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    ORALCOMM = models.SmallIntegerField(default=0, null=True, blank=True)
    KOMUNIKASYON = models.SmallIntegerField(default=0, null=True, blank=True)
    GENMATH = models.SmallIntegerField(default=0, null=True, blank=True)
    ELS = models.SmallIntegerField(default=0, null=True, blank=True)
    PERDEV = models.SmallIntegerField(default=0, null=True, blank=True)
    LITERATURE = models.SmallIntegerField(default=0, null=True, blank=True)
    PR1 = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.SET_NULL, null=True, related_name="firstsem2ndq11")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class SecondSem_3rdQ_11(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    READING_WRITING = models.SmallIntegerField(default=0, null=True, blank=True)
    PAGBASA = models.SmallIntegerField(default=0, null=True, blank=True)
    STATS_PROB = models.SmallIntegerField(default=0, null=True, blank=True)
    PHYSCI = models.SmallIntegerField(default=0, null=True, blank=True)
    EMPOWERMENT = models.SmallIntegerField(default=0, null=True, blank=True)
    ENTREP = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE2 = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.SET_NULL, null=True, related_name="secondsem3rdq11")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"

class SecondSem_4thQ_11(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    READING_WRITING = models.SmallIntegerField(default=0, null=True, blank=True)
    PAGBASA = models.SmallIntegerField(default=0, null=True, blank=True)
    STATS_PROB = models.SmallIntegerField(default=0, null=True, blank=True)
    PHYSCI = models.SmallIntegerField(default=0, null=True, blank=True)
    EMPOWERMENT = models.SmallIntegerField(default=0, null=True, blank=True)
    ENTREP = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED = models.SmallIntegerField(default=0, null=True, blank=True)
    SPECIALIZED_2 = models.SmallIntegerField(default=0, null=True, blank=True)
    PE2 = models.SmallIntegerField(default=0, null=True, blank=True)
    Average = models.IntegerField(default=0, null=True, blank=True)
    lrn = models.CharField(max_length=15)
    student = models.OneToOneField(StudentUser, on_delete=models.SET_NULL, null=True, related_name="secondsem4thq11")

    def __str__(self):
        return f"{self.last_name} - {self.lrn}"   