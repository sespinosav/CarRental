from .models import Car
from rest_framework import serializers
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'comercialValue', 'dialyValue', 'allow')
