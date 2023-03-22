from django.shortcuts import render
from .models import *

# Create your views here.
def GradeView(request):
    grades1st = FirstSem_1stQ.objects.all()
    grades2nd = FirstSem_2ndQ.objects.all()
    grades3rd = SecondSem_3rdQ.objects.all()
    grades4th = SecondSem_4thQ.objects.all()

    grades = {
        'grades1st' : grades1st,
        'grades2nd' : grades2nd,
        'grades3rd' : grades3rd,
        'grades4th' : grades4th,
    }

    return render(request, 'portal-grades11.html', grades)