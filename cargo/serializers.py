from rest_framework import serializers
from geopy import distance

from truck.models import Truck
from cargo.models import Cargo
from location.models import Location
from location.serializers import LocationDetailSerializer
from cargo.sevices import get_distance_from_truck_to_load
from truck.serializers import TruckDetailSerializer


class CargoCreateSerializer(serializers.ModelSerializer):
    pick_up_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        write_only=True,
        source='pickup_location'
    )
    delivery_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        write_only=True,
        source='delivery_location'
    )
    class Meta:
        model = Cargo
        fields = [
            'pick_up_zip',
            'delivery_zip',
            'weight',
            'description',
        ]


class CargoSerializer(serializers.ModelSerializer):
    pickup_location = LocationDetailSerializer()
    delivery_location = LocationDetailSerializer()
    trucks = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = [
            'pickup_location',
            'delivery_location',
            'trucks'
        ]

    def get_trucks(self, obj):
        trucks = [
            {
                'registration_plate': truck.registration_plate,
                'load_capacity': truck.load_capacity,
                'distance':get_distance_from_truck_to_load(truck, obj)
            }
            for truck in Truck.objects.select_related('location') \
                if get_distance_from_truck_to_load(truck, obj) <= 450
        ]
        return trucks
