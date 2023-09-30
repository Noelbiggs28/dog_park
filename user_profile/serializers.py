from rest_framework import serializers
from .models import UserProfile
from dog_app.models import Dog  # Import the Dog model

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('pk','dog_name','age','description')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('pk','name')