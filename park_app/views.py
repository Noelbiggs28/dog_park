from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import DogPark
from dog_app.models import Dog

class DogParkView(APIView):
    def numbers_to_dog_names(self, dog_park):
        dogs = dog_park.dogs.all()
        dog_names = []
        for dog in dogs:
            dog_names.append(dog.dog_name)
        return dog_names



    def get(self, request, pk=None):
        if pk is not None:
            # get dog park
            dog_park = get_object_or_404(DogPark, pk=pk)
            # get names in dog park
            dogs = self.numbers_to_dog_names(dog_park)
            # turn it into json
            json_dog_park = json.loads(serialize('json', [dog_park]))[0]
            #change the numbers to names
            json_dog_park["fields"]['dogs']=dogs
        else:
            dog_parks = DogPark.objects.order_by("pk")
            dog_park_list = []
            for park in dog_parks:
                dogs = self.numbers_to_dog_names(park)
                json_park = json.loads(serialize('json', [park]))[0]
                json_park["fields"]["dogs"] = dogs
                dog_park_list.append(json_park)
            json_dog_park = dog_park_list

        return Response(json_dog_park)
    
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