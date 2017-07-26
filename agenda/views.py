from datetime import date

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from agenda.forms import RemarcarForm, MarcarForm
from agenda.models import Escritorio, Profissional, Sala, ItemAgenda, Cliente


def index(request):
    perfil = perfilLogado()
    escritorio = perfil.escritorio
    profissionais = Profissional.objects.filter(escritorio=escritorio)
    salas = Sala.objects.filter(escritorio=escritorio)
    compromissos = ItemAgenda.objects.filter(escritorio=escritorio, data=date.today())
    return render(request,'index.html', {'escritorio':escritorio, 'profissionais':profissionais, 'salas':salas,
                                         'compromissos':compromissos, 'perfilLogado':perfil})

def perfilLogado():
    return Profissional.objects.get(id=1)

def detalhesDoCompromisso(request, compromisso_id):
    compromisso = ItemAgenda.objects.get(id=compromisso_id)
    return render(request, 'compromisso.html', {'compromisso':compromisso, 'perfilLogado':perfilLogado()})

def cancelarCompromisso(request, compromisso_id):
    compromisso = ItemAgenda.objects.get(id=compromisso_id)
    compromisso.mudar_situacao('C')
    return redirect('compromisso', compromisso_id=compromisso_id)

def concluirCompromisso(request, compromisso_id):
    compromisso = ItemAgenda.objects.get(id=compromisso_id)
    compromisso.mudar_situacao('R')
    return redirect('compromisso', compromisso_id=compromisso_id)


class RemarcarCompromissoView(View):
    template_name = 'compromisso.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, compromisso_id):
        print(compromisso_id)
        form = RemarcarForm(request.POST)
        compromisso = ItemAgenda.objects.get(id=compromisso_id)
        if form.is_valid():
            dados = form.cleaned_data
            print(dados)
            compromisso.remarcar(data=dados['data'],hora=dados['horario'])
            return redirect('index')
        return render(request, self.template_name, {'form': form, 'compromisso':compromisso, 'perfilLogado':perfilLogado()})

class MarcarCompromissoView(View):

    template_name = 'compromisso.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'perfil.html', {'perfilLogado': perfilLogado()})

    def post(self, request, *args, **kwargs):
        form = MarcarForm(request.POST)
        escritorio_id = kwargs['escritorio_id']
        escritorio = Escritorio.objects.get(id=escritorio_id)
        if form.is_valid():
            dados = form.cleaned_data
            print(dados)
            cliente = Cliente.objects.filter(cpf=dados['cpf']).first()
            if not cliente:
                cliente = Cliente.objects.create(cpf=dados['cpf'],nome=dados['nome'],telefone=dados['telefone'])
            profissional = Profissional.objects.get(nome=dados['profissional'],escritorio=escritorio)
            compromisso = ItemAgenda.objects.create(cliente=cliente,
                                      escritorio=escritorio,
                                      profissional=profissional,
                                      data=dados['data'],
                                      horario=dados['horario'])
            return redirect('compromisso', compromisso_id=compromisso.id)
        return redirect('index')


def detalhesPerfil(request, perfil_id):
    perfil = Profissional.objects.get(id=perfil_id)
    escritorio = perfil.escritorio
    profissionais = Profissional.objects.filter(escritorio=escritorio)
    clientes = Cliente.objects.all()
    return render(request, 'perfil.html', {'perfil':perfil, 'perfilLogado':perfilLogado(),
                                           'escritorio':escritorio, 'profissionais':profissionais,
                                           'clientes':clientes})