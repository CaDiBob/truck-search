from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from django.db import transaction

from cargo.models import Cargo
from truck.models import Truck
from location.models import Location
from cargo.serializers import CargoCreateSerializer, CargoSerializer


class CargoInfo(ListAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.select_related('pickup_location', 'delivery_location')


class CreateCargoView(CreateAPIView):
    serializer_class = CargoCreateSerializer
