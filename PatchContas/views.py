from .models import Compras, Vendas
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class JanelaInicial(LoginRequiredMixin, TemplateView):
    template_name = 'tela_inicial.html'


class CreateCompra(LoginRequiredMixin, CreateView):
    model = Compras
    fields = ['nome', 'descricao', 'valor', 'data', 'parcelas', 'ususario']
    success_url = reverse_lazy('tela_inicial')


class CreateVenda(LoginRequiredMixin, CreateView):
    model = Vendas
    fields = ['nome', 'descricao', 'parcela_um_val', 'parcela_um_data', 'parcela_um_paga',
              'parcela_dois_val', 'parcela_dois_data', 'parcela_dois_paga',
              'parcela_tres_val', 'parcela_tres_data', 'parcela_tres_paga',
              'parcela_quatro_val', 'parcela_quatro_data', 'parcela_quatro_paga']
    success_url = reverse_lazy('tela_inicial')


class UpdateCompra(LoginRequiredMixin, UpdateView):
    model = Compras
    fields = ['nome', 'descricao', 'valor', 'data', 'parcelas']
    success_url = reverse_lazy('tela_inicial')


class UpdateVenda(LoginRequiredMixin, UpdateView):
    model = Vendas
    fields = ['nome', 'descricao', 'parcela_um_val', 'parcela_um_data', 'parcela_um_paga',
              'parcela_dois_val', 'parcela_dois_data', 'parcela_dois_paga',
              'parcela_tres_val', 'parcela_tres_data', 'parcela_tres_paga',
              'parcela_quatro_val', 'parcela_quatro_data', 'parcela_quatro_paga']
    success_url = reverse_lazy('tela_inicial')


class DeleteCompra(LoginRequiredMixin, DeleteView):
    model = Compras
    success_url = reverse_lazy('tela_inicial')


class DeleteVenda(LoginRequiredMixin, DeleteView):
    model = Vendas
    success_url = reverse_lazy('tela_inicial')


class VendasList(LoginRequiredMixin, ListView):
    model = Vendas


class ComprasList(LoginRequiredMixin, ListView):
    model = Compras


"""
@login_required
def compras_lista(request):
    pesquisa = request.GET.get('pesquisa', None)
    data_min = request.GET.get('data_min', None)
    if pesquisa or data_min:
        compras = Compras.objects.filter(nome__contains=pesquisa) | Compras.objects.filter(descricao__contains=pesquisa)
        if data_min:
            compras = compras.filter(data__lte=str(data_min)).order_by('data')
    else:
        compras = Compras.objects.all()
    return render(request, 'compras_list.html', {'compras': compras})


@login_required
def vendas_lista(request):
    pesquisa = request.GET.get('pesquisa', None)
    radio = request.GET.get('radio_pgto', None)
    if radio == 'aberto':
        vendas = Vendas.objects.filter(parcela_um_paga=0) | Vendas.objects.filter(parcela_dois_paga=0)
        vendas = vendas | Vendas.objects.filter(parcela_tres_paga=0) | Vendas.objects.filter(parcela_quatro_paga=0)
    elif radio == 'pago':  # TEM QUE OTIMIZAR ESSA BUSCA
        vendas = Vendas.objects.filter(parcela_um_paga=1,
                                       parcela_dois_paga=1,
                                       parcela_tres_paga=1,
                                       parcela_quatro_paga=1)
        vendas = vendas | Vendas.objects.filter(parcela_um_paga=1,
                                                parcela_dois_paga=1,
                                                parcela_tres_paga=1,
                                                parcela_quatro_paga=None)
        vendas = vendas | Vendas.objects.filter(parcela_um_paga=1,
                                                parcela_dois_paga=1,
                                                parcela_tres_paga=None,
                                                parcela_quatro_paga=None)
        vendas = vendas | Vendas.objects.filter(parcela_um_paga=1,
                                                parcela_dois_paga=None,
                                                parcela_tres_paga=None,
                                                parcela_quatro_paga=None)
    else:
        vendas = Vendas.objects.all()
    if pesquisa:
        vendas = vendas.filter(nome__contains=pesquisa) | vendas.filter(descricao__contains=pesquisa)
    return render(request, 'vendas_list.html', {'vendas': vendas})
"""
