from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.forms import *
from django.db.models import Q
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def upload(request):
    if request.POST:
        
      form = MentorForm(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
          form.save()
      return redirect('main:homepage')
    return render(request, 'main/upload.html', {'form' : MentorForm})
   

def upload2(request):
    if request.POST:
        
      form = KolegijForm(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
          form.save()
      return redirect('main:homepage')
    return render(request, 'main/upload2.html', {'form' : KolegijForm})

def upload3(request):
    if request.POST:
        
      form = StudentForm(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
          form.save()
      return redirect('main:homepage')
    return render(request, 'main/upload3.html', {'form' : StudentForm})


def upload4(request):
    if request.method == 'POST':
        form = ZavrsniRadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:homepage')
    else:
        form = ZavrsniRadForm()
    return render(request, 'main/upload4.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Mentor.objects.filter(mentor_ime__iexact=query) | Mentor.objects.filter(mentor_prezime__iexact=query)
    else:
        results = []
    return render(request, 'main/search.html', {'results': results})

def search2(request):
    query = request.GET.get('q')
    if query:
        results = Kolegij.objects.filter(kolegij_naziv__icontains=query)
    else:
        results = []
    return render(request, 'main/search2.html', {'results': results})

def search3(request):
    query = request.GET.get('q')
    if query:
        results = Student.objects.filter(student_ime__iexact=query) | Student.objects.filter(student_prezime__iexact=query)
    else:
        results = []
    return render(request, 'main/search3.html', {'results': results})

def search4(request):
    query = request.GET.get('q')
    if query:
        results = ZavrsniRad.objects.filter(zavrsni_naslov__icontains=query)
    else:
        results = []
    return render(request, 'main/search4.html', {'results': results})
    
def delete(request, pk):
    obj = Mentor.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('main:homepage')
    context = {'object': obj}
    return render(request, 'main/confirm_delete.html', context)

def delete2(request, pk):
    obj = Kolegij.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('main:homepage')
    context = {'object': obj}
    return render(request, 'main/confirm_delete.html', context)

def delete3(request, pk):
    obj = Student.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('main:homepage')
    context = {'object': obj}
    return render(request, 'main/confirm_delete.html', context)

def delete4(request, pk):
    obj = ZavrsniRad.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('main:homepage')
    context = {'object': obj}
    return render(request, 'main/confirm_delete.html', context)


def updateMentor(request, pk):
    mentor = Mentor.objects.get(pk = pk)
    form = MentorForm(request.POST or None, instance=mentor)
    if form.is_valid():
        form.save()
        return redirect('main:mentori')
    return render(request,'main/update_mentor.html', {'mentor' : mentor, 'form': form})


def updateKolegij(request, pk):
    kolegij = Kolegij.objects.get(pk = pk)
    form = KolegijForm(request.POST or None, instance=kolegij)
    if form.is_valid():
        form.save()
        return redirect('main:kolegiji')
    return render(request,'main/update_mentor.html', {'mentor' : kolegij, 'form': form})

def updateStudent(request, pk):
    student = Student.objects.get(pk = pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('main:studenti')
    return render(request,'main/update_student.html', {'mentor' : student, 'form': form})

def updateZavrsni(request, pk):
    zavrsni = ZavrsniRad.objects.get(pk = pk)
    form = ZavrsniRadForm(request.POST or None, instance=zavrsni)
    if form.is_valid():
        form.save()
        return redirect('main:zavrsniradovi')
    return render(request,'main/update_zavrsni.html', {'mentor' : zavrsni, 'form': form})