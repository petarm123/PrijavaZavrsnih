from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from main.views import *
from main.models import *


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')
        self.assertEquals(resolve(url).func, homepage)

    def test_mentori_url_is_resolved(self):
        url = reverse('main:mentori')
        self.assertEquals(resolve(url).func.view_class, MentorList)

    def test_kolegiji_url_is_resolved(self):
        url = reverse('main:kolegiji')
        self.assertEquals(resolve(url).func.view_class, KolegijList)

    def test_studenti_url_is_resolved(self):
        url = reverse('main:studenti')
        self.assertEquals(resolve(url).func.view_class, StudentList)

    def test_zavrsniradovi_url_is_resolved(self):
        url = reverse('main:zavrsniradovi')
        self.assertEquals(resolve(url).func.view_class, ZavrsniRadList)




class ModelsTestCase(TestCase):
    def setUp(self):
        self.mentor1 = Mentor.objects.create(mentor_ime="ime-1", mentor_prezime="prezime-1")
        self.kolegij1 = Kolegij.objects.create(kolegij_naziv="Programiranje za Web", kolegij_nositelj=self.mentor1)
        self.student1 = Student.objects.create(student_ime="student-ime-1", student_prezime="student-prezime-1", student_broj_xice="1234578")
        self.student1.student_kolegiji.add(self.kolegij1)
        self.zavrsni_rad1 = ZavrsniRad.objects.create(zavrsni_mentor=self.mentor1, zavrsni_student=self.student1, zavrsni_naslov="zavrsni-naslov-1", zavrsni_broj_prijave=1, zavrsni_kolegij=self.kolegij1)

    def test_mentor(self):
        self.assertEqual(self.mentor1.mentor_ime, "ime-1")

    def test_kolegij(self):
        self.assertEqual(self.kolegij1.kolegij_naziv, "Programiranje za Web")

    def test_student(self):
        self.assertEqual(self.student1.student_broj_xice, "1234578")
    
    def test_zavrsni_rad(self):
        self.assertEqual(self.zavrsni_rad1.zavrsni_naslov, "zavrsni-naslov-1")



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:homepage')
        self.mentor_list_url = reverse('main:mentori')
        self.kolegij_list_url = reverse('main:kolegiji')
        self.student_list_url = reverse('main:studenti')
        self.zavrsni_list_url = reverse('main:zavrsniradovi')
        self.register_url = reverse('register')
        
        self.mentor1 = Mentor.objects.create(mentor_ime='Mentor1', mentor_prezime='Mentor1')
        self.kolegij1 = Kolegij.objects.create(kolegij_naziv='Kolegij1', kolegij_nositelj=self.mentor1)
        self.student1 = Student.objects.create(student_ime='Student1', student_prezime='Student1', student_broj_xice='1234')
        self.student1.student_kolegiji.set([self.kolegij1])
        self.zavrsni1 = ZavrsniRad.objects.create(zavrsni_mentor=self.mentor1, zavrsni_student=self.student1, zavrsni_naslov='Zavrsni1', zavrsni_broj_prijave=1, zavrsni_kolegij=self.kolegij1)
        #self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_homepage_GET(self):
        client = Client()
        response = client.get(self.homepage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')
	

    def test_mentor_list_GET(self):
        client = Client()
        response = client.get(self.mentor_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/mentor_list.html')

    def test_kolegij_list_GET(self):
        client = Client()
        response = client.get(self.kolegij_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kolegij_list.html')

    def test_student_list_GET(self):
        client = Client()
        response = client.get(self.student_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/student_list.html')
	
    def test_zavrsni_list_GET(self):
        client = Client()
        response = client.get(self.zavrsni_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/zavrsnirad_list.html')
	
    def test_register_view_GET(self):
      client = Client()
      response = client.get(self.register_url)
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response, 'registration/register.html')

	
	
	
	
	
	
	
	
"""
	def test_register_view_GET(self):
		client = Client()
        response = client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
	"""





"""
nmp el ovo triba dodat u register testiranje
 def test_register_view_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='testuser').exists())
"""

"""
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.mentor_list_url = reverse('mentor_list')
        self.kolegij_list_url = reverse('kolegij_list')
        self.student_list_url = reverse('student_list')
        self.zavrsni_list_url = reverse('zavrsni_list')
        self.register_url = reverse('register')
        
        self.mentor1 = Mentor.objects.create(mentor_ime='Mentor1', mentor_prezime='Mentor1')
        self.kolegij1 = Kolegij.objects.create(kolegij_naziv='Kolegij1', kolegij_nositelj=self.mentor1)
        self.student1 = Student.objects.create(student_ime='Student1', student_prezime='Student1', student_broj_xice='1234', student_kolegiji=self.kolegij1)
        self.zavrsni1 = ZavrsniRad.objects.create(zavrsni_mentor=self.mentor1, zavrsni_student=self.student1, zavrsni_naslov='Zavrsni1', zavrsni_broj_prijave=1, zavrsni_kolegij=self.kolegij1)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_homepage_GET(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_mentor_list_GET(self):
        response = self.client.get(self.mentor_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/mentor_list.html')

    def test_kolegij_list_GET(self):
        response = self.client.get(self.kolegij_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kolegij_list.html')

    def test_student_list_GET(self):
        response = self.client.get(self.student_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/student_list.html')

	"""
        
   