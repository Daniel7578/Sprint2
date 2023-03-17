from django.http import HttpResponse
from .logic import historiaClinica_logic as hl
from django.core import serializers
import json


def historiaClinica_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historiaClinica_dto = hl.get_HistoriaClinica(id)
            historiaClinica = serializers.serialize('json', historiaClinica_dto)
            return HttpResponse(historiaClinica, 'application/json')
        else:
            historiaClinica_dto = hl.get_HistoriaClinicas()
            historiaClinica = serializers.serialize('json', historiaClinica_dto)
            return HttpResponse(historiaClinica, 'application/json')







# Create your views here.
