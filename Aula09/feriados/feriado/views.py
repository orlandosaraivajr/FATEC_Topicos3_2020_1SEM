from django.shortcuts import render
from .models import FeriadoModel
from datetime import date


def feriado_index(request):
    hoje = date.today()
    feriado_ou_nao = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(feriado_ou_nao) == 0:
        contexto = {'feriado': False}
    else:
        nome = feriado_ou_nao[0].nome
        contexto = {'feriado': True, 'nome': nome}
    return render(request, 'feriados.html', contexto)
