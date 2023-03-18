from..models import HistoriaClinica

def get_HistoriaClinicas():
    historiasClinicas = HistoriaClinica.objects.all()
    return historiasClinicas

def get_HistoriaClinica(historia_pk):
    historiasClinicas = HistoriaClinica.objects.get(pk=historia_pk)
    return historiasClinicas