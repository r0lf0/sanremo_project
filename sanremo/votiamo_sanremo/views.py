from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import VotaForm
from .models import Categoria, Concorrente, Voto
from django.contrib.auth import get_user_model

def index(request):
    return HttpResponse('Hello, World!')

def lista_cantanti(request):
    cantanti = Concorrente.objects.all()
    context = {'cantanti':cantanti}
    return render(request, "votiamo_sanremo/lista_cantanti.html", context)

def home(request):
    concorrenti = Concorrente.objects.all().order_by("nome")
    voti = Voto.objects.all().filter(utente_id=request.user.id)
    context = {
        'concorrenti':concorrenti,
        'voti':voti
    }
    return render(request, "home.html", context)

def vota(request, concorrente_id):
    concorrente = Concorrente.objects.get(id=concorrente_id)
    try:
        voto = Voto.objects.filter(utente_id=request.user.id).get(concorrente=concorrente_id)
    except:
        voto = Voto()

    if request.method == 'POST':
        form = VotaForm(request.POST)
        if form.is_valid():
            voto.voto_canzone = form.cleaned_data['voto_canzone']
            voto.voto_interpretazione = form.cleaned_data['voto_interpretazione']
            voto.voto_outfit = form.cleaned_data['voto_outfit']
            voto.concorrente = concorrente
            voto.utente = request.user
            voto.save()
            return HttpResponseRedirect('/')

    else:
        form = VotaForm(instance=voto)


    context = {
        'concorrente':concorrente,
        'form':form
    }
    return render(request, "vota.html", context)
