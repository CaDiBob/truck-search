from rest_framework import viewsets
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from cargo import filters
from cargo.models import Cargo
from cargo.serializers import (
    CargoCreateSerializer,
    CargoSerializer,
    CargoDetailSerializer,
    CargoUpdateSerializer
)


class CargoViewSet(viewsets.ViewSet, GenericAPIView):
    serializer_class = CargoCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = CargoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CargoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, requst, pk=None):
        queryset = self.get_queryset()
        cargo = get_object_or_404(queryset, pk=pk)
        serializer = CargoDetailSerializer(cargo)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Cargo.objects.select_related(
            'delivery_location',
            'pickup_location'
        ).get_trucks_with_distance().get_nearest_trucks()

        if distance := self.request.query_params.get('distance'):
            return filters.filter_by_distance(queryset, distance)

        if weight := self.request.query_params.get('weight'):
            return queryset.filter(weight=weight)

        return queryset


class DestroyUpdateCargoView(RetrieveUpdateDestroyAPIView):
    serializer_class = CargoUpdateSerializer
    queryset = Cargo.objects.select_related(
            'delivery_location',
            'pickup_location'
        )
