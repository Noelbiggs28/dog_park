from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import DogPark
from dog_app.models import Dog
from .serializers import DogParkSerializer

class DogParkView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            # get dog park
            dog_park = get_object_or_404(DogPark, pk=pk)
            serializer = DogParkSerializer(dog_park)
        else:
            dog_park = DogPark.objects.order_by("pk")
            serializer = DogParkSerializer(dog_park, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        dog_park = DogPark.objects.create(**request.data)
        dog_park.save()
        dog_park.full_clean()
        dog_park = json.loads(serialize('json', [dog_park]))
        return Response(dog_park)
    
    def patch(self, request, pk):
        dog_park = get_object_or_404(DogPark, pk=pk)
        dog_ids = [request.data.get('dogs', [])]
        action = request.data.get('action')
        dogs = Dog.objects.filter(pk__in=dog_ids)
        if action == 'add':
            dog_park.dogs.add(*dogs)
            result_msg = f"Dogs added to {dog_park.dog_park_name}"
        elif action == 'remove':
            dog_park.dogs.remove(*dogs)
            result_msg = f"Dogs removed to the {dog_park.dog_park_name}"
        return Response(result_msg)
    
    def delete(self, request, pk):
        park = get_object_or_404(DogPark, pk=pk)
        park.delete()
        return Response('park was deleted')