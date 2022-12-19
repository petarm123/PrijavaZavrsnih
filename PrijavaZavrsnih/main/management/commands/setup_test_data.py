import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Mentor, Kolegij, Student, ZavrsniRad
from main.factory import (
    MentorFactory,
    KolegijFactory,
    StudentFactory,
    ZavrsniRadFactory
)

NUM_MENTOR = 10
NUM_KOLEGIJ = 10
NUM_STUDENT = 10
NUM_ZAVRSNI_RAD = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Mentor, Kolegij, Student, ZavrsniRad]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_MENTOR):
            mentor = MentorFactory()

        for _ in range(NUM_KOLEGIJ):
            kolegij = KolegijFactory()

        for _ in range(NUM_STUDENT):
            student = StudentFactory()

        for _ in range(NUM_ZAVRSNI_RAD):
            zavrsni_rad = ZavrsniRadFactory()

