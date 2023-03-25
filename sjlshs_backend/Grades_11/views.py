from django.shortcuts import render
from .models import *

# Create your views here.
def GradeView(request):
    grades1st = FirstSem_1stQ_11.objects.all()
    grades2nd = FirstSem_2ndQ_11.objects.all()
    grades3rd = SecondSem_3rdQ_11.objects.all()
    grades4th = SecondSem_4thQ_11.objects.all()

    grades = {
        'grades1st' : grades1st,
        'grades2nd' : grades2nd,
        'grades3rd' : grades3rd,
        'grades4th' : grades4th,
    }

    return render(request, 'portal-grades11.html', grades)