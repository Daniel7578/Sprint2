from..models import HistoriaClinica

def get_HistoriaClinicas():
    historiasClinicas = HistoriaClinica.objects.all()
    return historiasClinicas
def get_HistoriaClinica(var_pk):
    historiasClinicas = HistoriaClinica.objects.get(paciente_id=var_pk)
    return historiasClinicas