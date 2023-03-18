from django.http import HttpResponse
from .logic import historiaClinica_logic as hl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def historiaClinicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historia_dto = hl.get_HistoriaClinica(id)
            historia = serializers.serialize('json', [historia_dto,])
            return HttpResponse(historia, 'application/json')
        else:
            historia_dto = hl.get_HistoriaClinicas()
            historia = serializers.serialize('json', historia_dto)
            return HttpResponse(historia, 'application/json')

@csrf_exempt
def historiaClinica_view(request, pk):
    if request.method == 'GET':
        historia_dto = hl.get_HistoriaClinica(pk)
        historia = serializers.serialize('json', [historia_dto,])
        return HttpResponse(historia, 'application/json')

