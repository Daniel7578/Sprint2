from django.http import HttpResponse
from django.shortcuts import render
from .logic import historiaClinica_logic as hl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def historias_list(request):
    historias = hl.get_HistoriaClinicas()
    context = {
        'historias_list': historias
        }
    return render(request, 'HistoriaClinica/historiasclinicas.html', context)

def historia_detail(request, pk):
    historia_dto = hl.get_HistoriaClinica(pk)
    historia_json = serializers.serialize('json', [historia_dto,])
    historia = json.loads(historia_json)[0]  # extract the first object from the list
    pk_value = historia['pk']
    
    return render(request, 'HistoriaClinica/historia_detail.html', {'historia': historia, 'pk_value': pk_value})

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

