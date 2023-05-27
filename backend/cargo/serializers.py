from rest_framework import serializers

from truck.models import Truck
from cargo.models import Cargo
from location.models import Location
from location.serializers import LocationDetailSerializer
from cargo.sevices import get_distance_from_truck_to_load


class CargoUpdateSerializer(serializers.ModelSerializer):
    pickup_location = LocationDetailSerializer(read_only=True)
    delivery_location = LocationDetailSerializer(read_only=True)

    class Meta:
        model = Cargo
        fields = (
            'pickup_location',
            'delivery_location',
            'weight',
            'description'
        )


class CargoCreateSerializer(serializers.ModelSerializer):
    pickup_zip = serializers.SlugRelatedField(
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
        fields = (
            'pickup_zip',
            'delivery_zip',
            'weight',
            'description',
        )


class CargoSerializer(serializers.ModelSerializer):
    pickup_location = LocationDetailSerializer(read_only=True)
    delivery_location = LocationDetailSerializer(read_only=True)
    nearest_trucks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cargo
        fields = (
            'pickup_location',
            'delivery_location',
            'nearest_trucks',
        )

    def get_nearest_trucks(self, obj):
        return obj.nearest_trucks


class CargoDetailSerializer(serializers.ModelSerializer):
    pickup_location = LocationDetailSerializer(read_only=True)
    delivery_location = LocationDetailSerializer(read_only=True)
    trucks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cargo
        fields = (
            'pickup_location',
            'delivery_location',
            'weight',
            'description',
            'trucks',
        )

    def get_trucks(self, obj):
        trucks = Truck.objects.select_related('location')
        trucks_with_distance = [
            {
                'registation_plate': truck.registration_plate,
                'distance': get_distance_from_truck_to_load(truck, obj)
            }
            for truck in trucks
        ]
        return trucks_with_distance
