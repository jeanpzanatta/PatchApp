from django.urls import path
from .views import tela_inicial, compras_lista, vendas_lista, nova_compra, nova_venda
from .views import deletar_compra, deletar_venda, atualizar_compra, atualizar_venda


urlpatterns = [
    path('', tela_inicial, name='tela_inicial'),
    path('compras/', compras_lista, name='compras_lista'),
    path('vendas/', vendas_lista, name='vendas_lista'),
    path('nova_compra/', nova_compra, name='nova_compra'),
    path('nova_venda/', nova_venda, name='nova_venda'),
    path('deletar_venda/<int:id>/', deletar_venda, name='deletar_venda'),
    path('deletar_compra/<int:id>/', deletar_compra, name='deletar_compra'),
    path('atualizar_compra/<int:id>/', atualizar_compra, name='atualizar_compra'),
    path('atualizar_venda/<int:id>/', atualizar_venda, name='atualizar_venda'),
]
