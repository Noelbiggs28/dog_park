from rest_framework import serializers
from .models import DogPark, Dog
from owner_app.models import Owner
from triggers_app.models import Triggers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('owners_name',)
    def to_representation(self, instance):
        return instance.owners_name

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triggers
        fields = ('trigger_name',)
    def to_representation(self, instance):
        return instance.trigger_name

class DogSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    triggers = TriggerSerializer(many=True)
    class Meta:
        model = Dog
        fields = ('pk','dog_name','triggers', 'owner', 'description')

class DogParkSerializer(serializers.ModelSerializer):
    dogs = DogSerializer(many=True)

    class Meta:
        model = DogPark
        fields = ('id', 'dog_park_name', 'dogs')