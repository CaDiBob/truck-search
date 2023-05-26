from rest_framework import serializers

from truck.models import Truck

class TruckDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = [
            'registration_plate',
            'load_capacity',
            'location'
        ]
