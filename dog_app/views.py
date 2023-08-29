from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404

from .models import Dog
from owner_app.models import Owner

# Create your views here.
class DogView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            dog = get_object_or_404(Dog, pk=pk)
            json_dog = json.loads(serialize('json', [dog]))[0]
            
        else:
            dog = Dog.objects.order_by("pk")
            json_dog = json.loads(serialize("json",dog))
        return Response(json_dog)

# need to fix direct assignment of many to many for triggers
    def post(self, request):
        owner = Owner.objects.get(pk=request.data['owner'])
        request.data['owner']=owner
        dog = Dog.objects.create(**request.data)
        dog.save()
        dog.full_clean()
        dog = json.loads(serialize('json', [dog]))
        return Response(dog)

    
    def patch(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        owner_id = request.data.get('owner', [])
        owner = Owner.objects.get(pk=owner_id)
        if 'owner' in request.data:
            dog.change_owner(owner)
        dog.full_clean()
        dog.save()
        result_msg = f"Dog {dog.dog_name} assigned to owner {owner.owners_name}"
        dog = json.loads(serialize('json',[dog]))

        return Response(result_msg)
