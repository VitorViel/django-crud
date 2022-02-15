from django.shortcuts import render, redirect
from .models import Transacao
from django.http import HttpResponse
from .form import TransacaoForm
import datetime

# Create your views here.


def home(request):
    info = {}

    # info['transacoes'] = ['transacao1', 'transacao2', 'transacao3']
    # info['now'] = datetime.datetime.now()
    # html = "<html><body> It is now %s. </body></html>" % now
    return render(request, 'contas/home.html', info)

def mostraConteudo(request):
    conteudo = 'Olá, seja bem vindo(a) ao meu site!'
    return HttpResponse(conteudo)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)