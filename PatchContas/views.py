from .models import Compras, Vendas
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .forms import ComprasCreateForm, VendasCreateForm
from django.shortcuts import HttpResponseRedirect


class JanelaInicial(LoginRequiredMixin, TemplateView):
    template_name = 'tela_inicial.html'


class CreateCompra(LoginRequiredMixin, CreateView):
    model = Compras
    form_class = ComprasCreateForm
    success_url = reverse_lazy('compras_lista')
    template_name = 'compras_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreateCompra, self).get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


class CreateVenda(LoginRequiredMixin, CreateView):
    model = Vendas
    form_class = VendasCreateForm
    success_url = reverse_lazy('vendas_lista')
    template_name = 'vendas_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreateVenda, self).get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


class UpdateCompra(LoginRequiredMixin, UpdateView):
    model = Compras
    fields = ['nome', 'descricao', 'valor', 'data', 'parcelas']
    success_url = reverse_lazy('compras_lista')


class UpdateVenda(LoginRequiredMixin, UpdateView):
    model = Vendas
    fields = ['nome', 'descricao', 'parcela_um_val', 'parcela_um_data', 'parcela_um_paga',
              'parcela_dois_val', 'parcela_dois_data', 'parcela_dois_paga',
              'parcela_tres_val', 'parcela_tres_data', 'parcela_tres_paga',
              'parcela_quatro_val', 'parcela_quatro_data', 'parcela_quatro_paga']
    success_url = reverse_lazy('vendas_lista')


class DeleteCompra(LoginRequiredMixin, DeleteView):
    model = Compras
    success_url = reverse_lazy('compras_lista')


class DeleteVenda(LoginRequiredMixin, DeleteView):
    model = Vendas
    success_url = reverse_lazy('vendas_lista')


class VendasList(LoginRequiredMixin, ListView):
    model = Vendas
    paginate_by = 10

    def get_queryset(self):
        pesquisa = self.request.GET.get('pesquisa', None)
        radio = self.request.GET.get('radio_pgto', None)
        vendas_tot = self.model.objects.filter(usuario=self.request.user.id)
        data_min = self.request.GET.get('data_min', None)
        data_max = self.request.GET.get('data_max', None)
        #  As datas NÃO podem receber valores nulos, para evitar isso, é verificado cada uma das quatro
        #  possibulidades de ter ou não uma ou as duas datas no filtro.
        if data_min and data_max:
            vendas = vendas_tot.filter(parcela_um_data__lte=data_max, parcela_um_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_dois_data__lte=data_max, parcela_dois_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_tres_data__lte=data_max, parcela_tres_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_quatro_data__lte=data_max, parcela_quatro_data__gte=data_min)
        elif data_min and not data_max:
            vendas = vendas_tot.filter(parcela_um_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_dois_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_tres_data__gte=data_min)
            vendas = vendas | vendas_tot.filter(parcela_quatro_data__gte=data_min)
        elif not data_min and data_max:
            vendas = vendas_tot.filter(parcela_um_data__lte=data_max)
            vendas = vendas | vendas_tot.filter(parcela_dois_data__lte=data_max)
            vendas = vendas | vendas_tot.filter(parcela_tres_data__lte=data_max)
            vendas = vendas | vendas_tot.filter(parcela_quatro_data__lte=data_max)
        else:
            vendas = vendas_tot
        if radio == 'aberto':
            vendas = vendas.filter(parcela_um_paga=0)
            vendas = vendas | vendas_tot.filter(parcela_dois_paga=0)
            vendas = vendas | vendas_tot.filter(parcela_tres_paga=0)
            vendas = vendas | vendas_tot.filter(parcela_quatro_paga=0)
        elif radio == 'pago':
            #  exclui da query vendas que não tiveram as parcelas pagas
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
        data_max = self.request.GET.get('data_max', None)
        compras = self.model.objects.filter(usuario=self.request.user.id)
        if pesquisa or data_min or data_max:
            compras = compras.filter(nome__contains=pesquisa) | compras.filter(descricao__contains=pesquisa)
            if data_min:
                compras = compras.filter(data__gte=str(data_min)).order_by('data')
            if data_max:
                compras = compras.filter(data__lte=str(data_max)).order_by('data')
        return compras
