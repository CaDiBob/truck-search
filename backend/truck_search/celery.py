import os

from django.conf import settings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'truck_search.settings')

app = Celery('truck_search')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "truck_search": {
        "task": "truck.tasks.relocate_trucks",
        "schedule": 180, # Запускает задачу каждые 180 секунд
    },
}
