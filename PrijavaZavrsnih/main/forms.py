from django.forms import ModelForm
from django import forms
from main.models import *


class MentorForm(ModelForm):
    mentor_ime = forms.TextInput()
    mentor_prezime = forms.TextInput()
    class Meta:
        model = Mentor
        fields = ['mentor_ime', 'mentor_prezime']
        

class KolegijForm(forms.ModelForm):
    kolegij_naziv = forms.TextInput()
    kolegij_nositelj = forms.ModelChoiceField(queryset=Mentor.objects.all())
    class Meta:
        model = Kolegij
        fields = ['kolegij_naziv', 'kolegij_nositelj']
        

class StudentForm(forms.ModelForm):
    student_ime = forms.TextInput()
    student_prezime = forms.TextInput()
    student_broj_xice = forms.TextInput()
    student_kolegiji = forms.ModelMultipleChoiceField(queryset=Kolegij.objects.all())
    class Meta:
        model = Student
        fields = ['student_ime', 'student_prezime', 'student_broj_xice', 'student_kolegiji']



class ZavrsniRadForm(forms.ModelForm):
     zavrsni_mentor = forms.ModelChoiceField(queryset=Mentor.objects.all())
     zavrsni_student = forms.ModelChoiceField(queryset=Student.objects.all())
     zavrsni_kolegij = forms.ModelChoiceField(queryset=Kolegij.objects.all())
     zavrsni_naslov = forms.CharField(max_length=50)
     zavrsni_broj_prijave = forms.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

     class Meta:
        model = ZavrsniRad
        fields = ['zavrsni_mentor', 'zavrsni_student', 'zavrsni_naslov', 'zavrsni_broj_prijave', 'zavrsni_kolegij']

