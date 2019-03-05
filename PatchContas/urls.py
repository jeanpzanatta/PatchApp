from django.urls import path
from .views import ComprasList, VendasList, CreateCompra, CreateVenda, JanelaInicial
from .views import DeleteCompra, DeleteVenda, UpdateCompra, UpdateVenda


urlpatterns = [
    path('', JanelaInicial.as_view(), name='tela_inicial'),
    path('compras/', ComprasList.as_view(), name='compras_lista'),
    path('vendas/', VendasList.as_view(), name='vendas_lista'),
    path('compras/nova/', CreateCompra.as_view(), name='nova_compra'),
    path('vendas/nova/', CreateVenda.as_view(), name='nova_venda'),
    path('vendas/deletar/<int:pk>/', DeleteVenda.as_view(), name='deletar_venda'),
    path('compras/deletar/<int:pk>/', DeleteCompra.as_view(), name='deletar_compra'),
    path('compras/atualizar/<int:pk>/', UpdateCompra.as_view(), name='atualizar_compra'),
    path('vendas/atualizar/<int:pk>/', UpdateVenda.as_view(), name='atualizar_venda'),
]
