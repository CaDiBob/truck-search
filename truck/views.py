from rest_framework.generics import UpdateAPIView

from truck.models import Truck
from truck.serializers import TruckDetailSerializer


class TruckUpdateView(UpdateAPIView):
    serializer_class = TruckDetailSerializer
    queryset = Truck.objects.all()
