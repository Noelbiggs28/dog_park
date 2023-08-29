from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import Owner

class OwnerView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            owner = get_object_or_404(Owner, pk=pk)
            json_owner = json.loads(serialize('json', [owner]))[0]
            
        else:
            owners = Owner.objects.order_by("pk")
            json_owner = json.loads(serialize("json",owners))
        return Response(json_owner)
    
    def post(self, request):
        newOwner = Owner.objects.create(**request.data)
        newOwner.save()
        newOwner.full_clean()
        newOwner = json.loads(serialize('json', [newOwner]))
        return Response(newOwner)
