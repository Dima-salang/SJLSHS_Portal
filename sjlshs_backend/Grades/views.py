from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.

def GradeView(request):
    grades1st = GradePost.objects.all()
    grades2nd = GradePost2nd.objects.all()
    grades3rd = GradePost3rd.objects.all()
    grades4th = GradePost4th.objects.all()

    grades = {
        'grades1st' : grades1st,
        'grades2nd' : grades2nd,
        'grades3rd' : grades3rd,
        'grades4th' : grades4th
    }

    return render(request, 'portal-grades.html', grades)