from django.db import models
from accounts.models import StudentUser, Db_Students
from subjects.models import CoreSubjects, SpecializedSubjects

# Create your models here.



class GradeTest(models.Model):
    PR2 = models.SmallIntegerField(default=0)
    CPAR = models.SmallIntegerField(default=0)
    PHILOSOPHY = models.SmallIntegerField(default=0)
    UCSP = models.SmallIntegerField(default=0)
    EAPP = models.SmallIntegerField(default=0)
    SPECC = models.SmallIntegerField(default=0)
    SPECC2 = models.SmallIntegerField(default=0)
    PE = models.SmallIntegerField(default=0)

    lrn = models.CharField(max_length=15)

class GradePost(models.Model):
    sub1 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub1')
    sub2 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub2')
    sub3 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub3')
    sub4 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub4')
    sub5 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub5')
    sub6 = models.ForeignKey(CoreSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub6')
    sub7 = models.ForeignKey(SpecializedSubjects, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub7')
    sub8 = models.ForeignKey(SpecializedSubjects, null=True, blank=True,  on_delete=models.SET_NULL, related_name='sub8')

    grade_sub1 = models.SmallIntegerField(default=0)
    grade_sub2 = models.SmallIntegerField(default=0)
    grade_sub3 = models.SmallIntegerField(default=0)
    grade_sub4 = models.SmallIntegerField(default=0)
    grade_sub5 = models.SmallIntegerField(default=0)
    grade_sub6 = models.SmallIntegerField(default=0)
    grade_sub7 = models.SmallIntegerField(default=0)
    grade_sub8 = models.SmallIntegerField(default=0)

    lrn = models.OneToOneField(StudentUser, null=False, on_delete=models.CASCADE, related_name='GradePost')

    @property
    def grade_avg(self):
        average = (self.pr2 + self.cpar + self.pe + self.spec + self.ucsp + self.philo + self.eapp) / 7.0
        return average
    
    def __str__(self):
        return str(self.lrn)

class GradePost2nd(models.Model):
    pr2_2nd = models.SmallIntegerField(default=0)
    cpar_2nd = models.SmallIntegerField(default=0)
    pe_2nd = models.SmallIntegerField(default=0)
    spec_2nd = models.SmallIntegerField(default=0)
    ucsp_2nd = models.SmallIntegerField(default=0)
    philo_2nd = models.SmallIntegerField(default=0)
    eapp_2nd = models.SmallIntegerField(default=0)
    lrn = models.OneToOneField(StudentUser, null=False, on_delete=models.CASCADE, related_name='GradePost2nd')

    @property
    def grade_avg_2ndq(self):
        average = (self.pr2_2nd + self.cpar_2nd + self.pe_2nd + self.spec_2nd + self.ucsp_2nd + self.philo_2nd + self.eapp_2nd) / 7.0
        return average

    def __str__(self):
        return str(self.lrn)

class GradePost3rd(models.Model):
    pr2_3rd = models.SmallIntegerField(default=0)
    cpar_3rd = models.SmallIntegerField(default=0)
    pe_3rd = models.SmallIntegerField(default=0)
    spec_3rd = models.SmallIntegerField(default=0)
    ucsp_3rd = models.SmallIntegerField(default=0)
    philo_3rd = models.SmallIntegerField(default=0)
    eapp_3rd = models.SmallIntegerField(default=0)
    lrn = models.OneToOneField(StudentUser, null=False, on_delete=models.CASCADE, related_name='GradePost3rd')
    
    @property
    def grade_avg_3rdq(self):
        average = (self.pr2_3rd + self.cpar_3rd + self.pe_3rd + self.spec_3rd + self.ucsp_3rd + self.philo_3rd + self.eapp_3rd) / 7.0
        return average

    def __str__(self):
        return str(self.lrn)    

class GradePost4th(models.Model):
    pr2_4th = models.SmallIntegerField(default=0)
    cpar_4th = models.SmallIntegerField(default=0)
    pe_4th = models.SmallIntegerField(default=0)
    spec_4th = models.SmallIntegerField(default=0)
    ucsp_4th = models.SmallIntegerField(default=0)
    philo_4th = models.SmallIntegerField(default=0)
    eapp_4th = models.SmallIntegerField(default=0)
    lrn = models.OneToOneField(StudentUser, null=False, on_delete=models.CASCADE, related_name='GradePost4th')

    @property
    def grade_avg_4thq(self):
        average = (self.pr2_4th + self.cpar_4th + self.pe_4th + self.spec_4th + self.ucsp_4th + self.philo_4th + self.eapp_4th) / 7.0
        return average

    def __str__(self):
        return str(self.lrn)