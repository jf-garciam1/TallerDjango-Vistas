from django.shortcuts import render
from .logic import measurments_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurments_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurment_dto = ml.get_measurment(id)
            measurment = serializers.serialize('json', [measurment_dto,])
            return HttpResponse(measurment, 'application/json')
        else:
            measurment_dto = ml.get_measurments()
            measurment = serializers.serialize('json', [measurment_dto,])
            return HttpResponse(measurment, 'application/json')
    if request.method == 'POST':
        measurment_dto = ml.create_measurment(json.loads(request.body))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

@csrf_exempt
def measurment_view(request, pk):
    if request.method == 'GET':
        measurment_dto = ml.get_measurment(pk)
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

    if request.method == 'PUT':
        variable_dto = ml.update_measurment(pk, json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')