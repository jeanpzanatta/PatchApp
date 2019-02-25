from django.db import models
from django.core.validators import MinValueValidator


class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.0)])
    data = models.DateField()
    parcelas = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.data)


class Vendas(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    parcela_um_val = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.0)])
    parcela_um_data = models.DateField()
    parcela_um_paga = models.BooleanField(default=False)
    parcela_dois_val = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                           validators=[MinValueValidator(0.0)])
    parcela_dois_data = models.DateField(blank=True, null=True)
    parcela_dois_paga = models.NullBooleanField()
    parcela_tres_val = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                           validators=[MinValueValidator(0.0)])
    parcela_tres_data = models.DateField(blank=True, null=True)
    parcela_tres_paga = models.NullBooleanField()
    parcela_quatro_val = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True,
                                             validators=[MinValueValidator(0.0)])
    parcela_quatro_data = models.DateField(blank=True, null=True)
    parcela_quatro_paga = models.NullBooleanField()

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.parcela_um_data)
