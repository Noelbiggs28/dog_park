from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import Triggers



class TriggerView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            trigger = get_object_or_404(Triggers, pk=pk)
            json_trigger = json.loads(serialize('json', [trigger]))[0]
            
        else:
            triggers = Triggers.objects.order_by("pk")
            json_trigger = json.loads(serialize("json",triggers))
        return Response(json_trigger)

    def post(self, request):
        new_trigger = Triggers.objects.create(**request.data)
        new_trigger.save()
        new_trigger.full_clean()
        new_trigger = json.loads(serialize('json', [new_trigger]))
        return Response(new_trigger)

