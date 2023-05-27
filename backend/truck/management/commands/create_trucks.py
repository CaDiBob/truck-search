import random
import string

from django.core.management.base import BaseCommand

from truck.models import Truck
from location.models import Location


class Command(BaseCommand):
    help = 'Добавление машин в БД'

    def add_arguments(self, parser):
        parser.add_argument(
                'num_trucks',
                nargs='?',
                type=int,
                default=20,
                help='Укажите количество машин, по умолчанию 20'
            )

    def handle(self, *args, **options):
        num_trucks = options['num_trucks']
        locations = Location.objects.all()

        trucks = []
        for _ in range(num_trucks):
            number = random.randint(1000, 9999+1)
            letter = random.choice(string.ascii_uppercase)

            truck = Truck(
                registration_plate=f'{number}{letter}',
                load_capacity=random.randint(1, 1000+1),
                location=random.choice(locations)
            )
            trucks.append(truck)
        Truck.objects.bulk_create(trucks)

        self.stdout.write(self.style.SUCCESS('Машины успешно созданы'))
