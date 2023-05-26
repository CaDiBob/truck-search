from rest_framework import serializers

from location.models import Location


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'city',
            'state',
            'zip_code',
            'lat',
            'lon'
        ]
