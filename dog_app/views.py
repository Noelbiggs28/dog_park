from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404

from .models import Dog
from owner_app.models import Owner



class DogView(APIView):
    def number_to_trigger_names(self, dog):
        triggers = dog.triggers.all()
        trigger_names = [trigger.trigger_name for trigger in triggers]
        return trigger_names



    def number_to_owner_name(self, dog):
        owner = dog.owner
        owner_name = owner.owners_name
        return owner_name
    
    def get(self, request, pk=None):
        if pk is not None:
            # get dog
            dog = get_object_or_404(Dog, pk=pk)
            # get owner name
            owner_name = self.number_to_owner_name(dog)
            trigger_names = self.number_to_trigger_names(dog)
            # make dog jason
            json_dog = json.loads(serialize('json', [dog]))[0]
            # make dog owner a name
            json_dog['fields']['owner'] = owner_name
            json_dog['fields']['triggers'] = trigger_names

        else:
            dogs = Dog.objects.order_by("pk")
            dog_list = []
            for dog in dogs:
                owner_name=self.number_to_owner_name(dog)
                trigger_names = self.number_to_trigger_names(dog)
                json_dog = json.loads(serialize("json",[dog]))[0]
                json_dog['fields']['owner']=owner_name
                json_dog['fields']['triggers'] = trigger_names
                dog_list.append(json_dog)
            json_dog = dog_list
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
