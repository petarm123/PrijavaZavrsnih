from django.shortcuts import render
from django.views.generic import ListView
from main.models import *
# Create your views here.
def homepage(request):
    return render(request, 'base_generic.html')

class MentorList(ListView):
    model = Mentor

class KolegijList(ListView):
    model = Kolegij

class StudentList(ListView):
    model = Student

class ZavrsniRadList(ListView):
    model = ZavrsniRad