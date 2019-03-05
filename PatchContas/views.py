from .models import Compras, Vendas
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class JanelaInicial(LoginRequiredMixin, TemplateView):
    template_name = 'tela_inicial.html'


class CreateCompra(LoginRequiredMixin, CreateView):
    template_name = 'compras_add.html'
    model = Compras
    fields = ['nome', 'descricao', 'valor', 'data', 'parcelas', 'usuario']
    success_url = reverse_lazy('compras_lista')


class CreateVenda(LoginRequiredMixin, CreateView):
    template_name = 'vendas_add.html'
    model = Vendas
    fields = ['nome', 'descricao', 'parcela_um_val', 'parcela_um_data', 'parcela_um_paga',
              'parcela_dois_val', 'parcela_dois_data', 'parcela_dois_paga',
              'parcela_tres_val', 'parcela_tres_data', 'parcela_tres_paga',
              'parcela_quatro_val', 'parcela_quatro_data', 'parcela_quatro_paga', 'usuario']
    success_url = reverse_lazy('vendas_lista')


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
    paginate_by = 10

    def get_queryset(self):
        pesquisa = self.request.GET.get('pesquisa', None)
        radio = self.request.GET.get('radio_pgto', None)
        vendas = self.model.objects.filter(usuario=self.request.user.id)
        if radio == 'aberto':
            vendas = vendas.filter(parcela_um_paga=0) | vendas.filter(parcela_dois_paga=0)
            vendas = vendas | vendas.filter(parcela_tres_paga=0) | vendas.filter(parcela_quatro_paga=0)
        elif radio == 'pago':
            #  exclui da query vendas que ja tiveram as parcelas pagas
            vendas = vendas.exclude(parcela_um_paga=0)
            vendas = vendas.exclude(parcela_dois_paga=0)
            vendas = vendas.exclude(parcela_tres_paga=0)
            vendas = vendas.exclude(parcela_quatro_paga=0)
        if pesquisa:
            vendas = vendas.filter(nome__contains=pesquisa) | vendas.filter(descricao__contains=pesquisa)
        return vendas


class ComprasList(LoginRequiredMixin, ListView):
    model = Compras
    paginate_by = 10

    def get_queryset(self):
        pesquisa = self.request.GET.get('pesquisa', None)
        data_min = self.request.GET.get('data_min', None)
        compras = self.model.objects.filter(usuario=self.request.user.id)
        if pesquisa or data_min:
            compras = compras.filter(nome__contains=pesquisa) | compras.filter(
                                     descricao__contains=pesquisa)
            if data_min:
                compras = compras.filter(data__gte=str(data_min)).order_by('data')
        return compras
