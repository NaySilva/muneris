from django.conf.urls import url

from agenda import views
from agenda.views import RemarcarCompromissoView, MarcarCompromissoView, EditarPerfilView, RegistrarEscritorioView, \
    AdicionarProfissionalView, AdicionarSalaView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^compromisso/(?P<compromisso_id>\d+)$', views.detalhesDoCompromisso, name='compromisso'),
    url(r'^compromisso/(?P<compromisso_id>\d+)/cancelar$', views.cancelarCompromisso, name='cancelarCompromisso'),
    url(r'^compromisso/(?P<compromisso_id>\d+)/concluir$', views.concluirCompromisso, name='concluirCompromisso'),
    url(r'^compromisso/(?P<compromisso_id>\d+)/iniciar$', views.iniciarCompromisso, name='iniciarCompromisso'),
    url(r'^compromisso/(?P<compromisso_id>\d+)/remarcar$', RemarcarCompromissoView.as_view(), name='remarcarCompromisso'),
    url(r'^escritorio/(?P<escritorio_id>\d+)/marcar$', MarcarCompromissoView.as_view(), name='marcarCompromisso'),
    url(r'^escritorio/registrar$', RegistrarEscritorioView.as_view(), name='registrarEscritorio'),
    url(r'^escritorio/gerenciar$', views.gerenciarEscritorio, name='gerenciar'),
    url(r'^escritorio/removerProfissional/(?P<profissional_id>\d+)$', views.removerProfissional, name='removerProfissional'),
    url(r'^escritorio/removerSala/(?P<sala_id>\d+)$', views.removerSala, name='removerSala'),
    url(r'^escritorio/adicionarProfissional$', AdicionarProfissionalView.as_view(), name='adicionarProfissional'),
    url(r'^escritorio/adicionarSala$', AdicionarSalaView.as_view(), name='adicionarSala'),
    url(r'^perfil/(?P<perfil_id>\d+)/editar$', EditarPerfilView.as_view(), name='editarPerfil'),
    url(r'^perfil/(?P<perfil_id>\d+)$', views.detalhesPerfil, name='perfil'),
    url(r'^perfil/(?P<perfil_id>\d+)/ficarAusente$', views.ficarAusente, name='ficarAusente'),
    url(r'^perfil/(?P<perfil_id>\d+)/ficarPresente$', views.ficarPresente, name='ficarPresente'),
    url(r'^perfil/excluir$', views.excluirPerfil, name='excluirPerfil'),
    url(r'^agenda$', views.detalhesAgenda, name='agenda'),
    url(r'^agenda/filter=(?P<filter>\w+)$', views.detalhesAgenda, name='filtroAgenda'),
]