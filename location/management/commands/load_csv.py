import csv
import os

from django.core.management.base import BaseCommand


from location.models import Location

class Command(BaseCommand):
    help = 'Загрузка данных из CSV в БД'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Укажите путь к csv файлу')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR('CSV файл не существует'))
            return
        locations = []
        with open(csv_file, 'r') as file:
            raw_locations = csv.DictReader(file)
            for row in raw_locations:
                location = Location(
                    city=row.get('city'),
                    state=row.get('state_name'),
                    zip_code=int(row.get('zip')), # преобразуем в тип int, чтобы избежать добавление нулей в начале строки
                    lat=row.get('lat'),
                    lon=row.get('lng'),
                )
                if not Location.objects.filter(city=location.city, lat=location.lat, lon=location.lon).exists():
                    locations.append(location)
        Location.objects.bulk_create(locations)

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
