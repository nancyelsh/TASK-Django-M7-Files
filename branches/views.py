from django.http import HttpRequest
from rest_framework import generics

from branches import models, serializers


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = models.Restaurant.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.RestaurantListSerializer
        return serializers.RestaurantCreateUpdateSerializer


class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Restaurant.objects.all()
    lookup_url_kwarg = "restaurant_id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.RestaurantDetailSerializer
        return serializers.RestaurantCreateUpdateSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.EmployeeListSerializer
        return serializers.EmployeeCreateUpdateSerializer


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    lookup_url_kwarg = "employee_id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.EmployeeDetailSerializer
        return serializers.EmployeeCreateUpdateSerializer
