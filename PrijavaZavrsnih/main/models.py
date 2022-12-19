from django.db import models
from django.core.validators import *
# Create your models here.


class Mentor(models.Model):
    mentor_ime = models.CharField(max_length=30)
    mentor_prezime = models.CharField(max_length=30)

    def __str__(self):
        return self.mentor_ime

class Kolegij(models.Model):
    kolegij_naziv = models.CharField(max_length=50)
    kolegij_nositelj = models.ForeignKey(Mentor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.kolegij_naziv

class Student(models.Model):
    student_ime = models.CharField(max_length=25)
    student_prezime = models.CharField(max_length=50)
    student_broj_xice = models.CharField(max_length=10)
    student_kolegiji = models.ManyToManyField(Kolegij)

    def __str__(self):
        return self.student_broj_xice
    

class ZavrsniRad(models.Model):
    zavrsni_mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE, default=1)
    zavrsni_student = models.OneToOneField(
        Student, on_delete=models.CASCADE, primary_key=True, default=1)
    zavrsni_naslov = models.CharField(max_length=50)
    zavrsni_broj_prijave = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
    zavrsni_kolegij = models.ForeignKey(
        Kolegij, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.zavrsni_naslov
