from rest_framework import serializers

from truck.models import Truck
from location.models import Location


class TruckDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        write_only=True,
    )
    registration_plate = serializers.CharField(read_only=True)
    load_capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Truck
        fields = (
            'location',
            'registration_plate',
            'load_capacity',
        )
