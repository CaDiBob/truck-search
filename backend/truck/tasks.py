import random

from celery import shared_task

from truck.models import Truck
from location.models import Location


@shared_task
def relocate_trucks():
    locations = Location.objects.all()

    trucks = []
    for truck in Truck.objects.select_related('location'):
        truck.location = random.choice(locations)
        trucks.append(truck)
    Truck.objects.bulk_update(trucks, ['location'])
