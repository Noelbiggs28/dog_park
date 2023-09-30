from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404

from .models import Dog
from user_profile.models import UserProfile
from .serializers import DogSerializer
class DogView(APIView): 

    def get(self, request, pk=None):
        if pk is not None:
            dog = get_object_or_404(Dog, pk=pk)
            serializer = DogSerializer(dog)
        else:
            dogs = Dog.objects.order_by("pk")
            serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        owner=get_object_or_404(UserProfile, pk=request.data['owner'])
        request.data['owner'] = owner
        dog = Dog.objects.create(**request.data)
        dog.save()
        dog.full_clean()
        dog = json.loads(serialize('json', [dog]))
        return Response(f"{dog} created")

    
    def patch(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk) 
        if 'age' in request.data:
            dog.age =request.data.get('age',dog.age)
        if 'dog_name' in request.data:
            dog.dog_name = request.data.get('dog_name',dog.dog_name)
        if 'description' in request.data:
            dog.description= request.data.get('description',dog.description)
        # elif 'triggers' in request.data:
        #     dog.add_trigger(request.data.get('triggers'))
        #     result_msg = "added trigger"
        # elif 'untriggers' in request.data:
        #     dog.remove_trigger(request.data.get('untriggers'))
        #     result_msg = "removed trigger"
        # elif 'likes' in request.data:
        #     dog.add_like(request.data.get('likes'))
        #     result_msg = "updated likes"
        # elif "unlikes" in request.data:
        #     dog.remove_like(request.data.get('unlikes'))
        #     result_msg = "updated likes"
        dog.full_clean()
        dog.save()
        dog = json.loads(serialize('json',[dog]))

        return Response(dog)

    def delete(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response('dog was deleted')