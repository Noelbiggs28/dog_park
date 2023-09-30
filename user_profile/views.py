from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .serializers import UserProfileSerializer, DogSerializer

class UserProfileView(APIView):
    def get(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        dogs = user_profile.dog_set.all()
        serializer = UserProfileSerializer(user_profile)
        data = serializer.data
        data['dogs'] = DogSerializer(dogs, many=True).data
        return Response(data)

    def put(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


