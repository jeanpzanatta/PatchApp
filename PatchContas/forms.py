from django.forms.models import ModelForm
from .models import Compras, Vendas


class ComprasCreateForm(ModelForm):
    class Meta:
        model = Compras
        exclude = ('usuario',)

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(ComprasCreateForm, self).__init__(*args, **kwargs)


class VendasCreateForm(ModelForm):
    class Meta:
        model = Vendas
        exclude = ('usuario',)

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(VendasCreateForm, self).__init__(*args, **kwargs)
