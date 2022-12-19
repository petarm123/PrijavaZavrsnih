from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mentori/', MentorList.as_view()),
    path('kolegiji/', KolegijList.as_view()),
    path('studenti/', StudentList.as_view()),
    path('zavrsniradovi/', ZavrsniRadList.as_view()),
]