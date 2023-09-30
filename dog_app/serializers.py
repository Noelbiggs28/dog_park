from rest_framework import serializers
from .models import Triggers, Dog
from user_profile.models import UserProfile
class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triggers
        fields = ('trigger_name',)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name',)


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields= ('dog_name',)


class DogSerializer(serializers.ModelSerializer):
    # triggers = TriggerSerializer(many=True)
    owner = UserProfileSerializer()
    # likes = LikesSerializer(many=True)
    class Meta:
        model = Dog
        fields = ('id', 'dog_name', 'age', 'triggers', 'owner', 'description', 'likes')