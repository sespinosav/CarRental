from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    _id = serializers.IntegerField()
    brand = serializers.CharField()
    model = serializers.CharField()
    comercial_value = serializers.FloatField()
    dialy_alquiler_value = serializers.FloatField()
    allow = serializers.BooleanField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance._id = validated_data.get('_id', instance._id)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.comercial_value = validated_data.get('comercial_value', instance.comercial_value)
        instance.dialy_alquiler_value = validated_data.get('dialy_alquiler_value', instance.dialy_alquiler_value)
        instance.allow = validated_data.get('allow', instance.allow)

        instance.save()
        return instance
