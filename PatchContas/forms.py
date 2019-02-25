from django.forms import ModelForm
from .models import Compras, Vendas


class FormVendas(ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome', 'descricao', 'valor', 'data', 'parcelas']


class FormCompras(ModelForm):
    class Meta:
        model = Compras
        fields = ['nome', 'descricao', 'valor', 'data', 'parcelas']
