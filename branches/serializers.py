from rest_framework import serializers

from branches import models


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        exclude = ["id"]


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ["id", "name"]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = "__all__"


class EmployeeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        exclude = ["id"]


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["id", "first_name", "last_name"]


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"
