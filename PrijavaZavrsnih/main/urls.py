from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mentori/', MentorList.as_view(), name='mentori'),
    path('kolegiji/', KolegijList.as_view(), name='kolegiji'),
    path('studenti/', StudentList.as_view(), name='studenti'),
    path('zavrsniradovi/', ZavrsniRadList.as_view(), name = 'zavrsniradovi'),
    path('mentori/upload', views.upload, name='upload'),
    path('kolegiji/upload', views.upload2, name='upload2'),
    path('studenti/upload', views.upload3, name='upload3'),
    path('zavrsnirad/upload', views.upload4, name='upload4'),
    path('mentori/search/', views.search, name='search'),
    path('kolegiji/search/', views.search2, name='search2'),
    path('studenti/search/', views.search3, name='search3'),
    path('zavrsnirad/search/', views.search4, name='search4'),
    path('mentor/delete/<int:pk>/', views.delete, name='delete'),
    path('kolegij/delete/<int:pk>/', views.delete2, name='delete2'),
    path('student/delete/<int:pk>/', views.delete3, name='delete3'),
    path('zavrsnirad/delete/<int:pk>/', views.delete4, name='delete4'),
    path('mentori/update/<int:pk>/', views.updateMentor, name='update-mentor'),
    path('kolegiji/update/<int:pk>/', views.updateKolegij, name='update-kolegij'),
    path('studenti/update/<int:pk>/', views.updateStudent, name='update-student'),
     path('zavrsnirad/update/<int:pk>/', views.updateZavrsni, name='update-zavrsni'),
    
]