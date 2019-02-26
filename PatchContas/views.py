from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Compras, Vendas
from .forms import FormCompras, FormVendas


@login_required
def tela_inicial(request):
    return render(request, 'tela_inicial.html')


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
    return render(request, 'lista_compras.html', {'compras': compras})


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
    return render(request, 'lista_vendas.html', {'vendas': vendas})


@login_required
def nova_compra(request):
    form = FormCompras(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tela_inicial')
    return render(request, 'nova_compra.html', {'form': form})


@login_required
def nova_venda(request):
    form = FormVendas(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tela_inicial')
    return render(request, 'nova_venda.html', {'form': form})


@login_required
def deletar_compra(request, id):
    compra = get_object_or_404(Compras, pk=id)
    if request.method == 'POST':
        compra.delete()
        return redirect('tela_inicial')
    return render(request, 'deletar_compra.html', {'form': compra})


@login_required
def deletar_venda(request, id):
    venda = get_object_or_404(Vendas, pk=id)
    if request.method == 'POST':
        venda.delete()
        return redirect('tela_inicial')
    return render(request, 'deletar_venda.html', {'form': venda})


@login_required
def atualizar_compra(request, id):
    compra = get_object_or_404(Compras, pk=id)
    form = FormCompras(request.POST or None, instance=compra)
    if form.is_valid():
        form.save()
        return redirect('tela_inicial')
    return render(request, 'nova_compra.html', {'form': form})


@login_required
def atualizar_venda(request, id):
    venda = get_object_or_404(Vendas, pk=id)
    form = FormVendas(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('tela_inicial')
    return render(request, 'nova_venda.html', {'form': form})
