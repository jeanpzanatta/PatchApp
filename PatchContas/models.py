from django.db import models


class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateField()
    parcelas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.data)


class Vendas(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateField()
    parcelas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.data)
