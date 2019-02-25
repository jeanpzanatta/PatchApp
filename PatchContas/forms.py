from django.forms import ModelForm
from .models import Compras, Vendas


class FormVendas(ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome', 'descricao', 'parcela_um_val', 'parcela_um_data', 'parcela_um_paga',
                  'parcela_dois_val', 'parcela_dois_data', 'parcela_dois_paga',
                  'parcela_tres_val', 'parcela_tres_data', 'parcela_tres_paga',
                  'parcela_quatro_val', 'parcela_quatro_data', 'parcela_quatro_paga']


class FormCompras(ModelForm):
    class Meta:
        model = Compras
        fields = ['nome', 'descricao', 'valor', 'data', 'parcelas']
