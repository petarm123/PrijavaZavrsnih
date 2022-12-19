from django.contrib import admin
from . models import *
# Register your models here.
model_list = [Student, Mentor, ZavrsniRad, Kolegij]
admin.site.register(model_list)