## factories.py
import factory
from factory.django import DjangoModelFactory
from main.models import *
import factory.fuzzy


## Defining a factory
class MentorFactory(DjangoModelFactory):
    class Meta:
        model = Mentor

    mentor_ime = factory.Faker("first_name")
    mentor_prezime = factory.Faker("last_name")

class KolegijFactory(DjangoModelFactory):
    class Meta:
        model = Kolegij

    kolegij_naziv = factory.Faker("sentence", nb_words=4)
    kolegij_nositelj = factory.Iterator(Mentor.objects.all())

class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    student_ime = factory.Faker("first_name")
    student_prezime = factory.Faker("last_name")
    student_broj_xice = factory.fuzzy.FuzzyInteger(1000000000, 9999999999)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.groups.add(*extracted)

class ZavrsniRadFactory(DjangoModelFactory):
    class Meta:
        model = ZavrsniRad

    zavrsni_mentor = factory.Iterator(Mentor.objects.all())
    zavrsni_student = factory.Iterator(Student.objects.all())
    zavrsni_naslov = factory.Faker("sentence", nb_words=10)
    zavrsni_broj_prijave = factory.fuzzy.FuzzyInteger(0, 10)
    zavrsni_kolegij = factory.Iterator(Kolegij.objects.all())


