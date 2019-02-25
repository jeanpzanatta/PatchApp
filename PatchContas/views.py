from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Compras, Vendas
from .forms import FormCompras, FormVendas


@login_required
def tela_inicial(request):
    return render(request, 'tela_inicial.html')


@login_required
def compras_lista(request):
    compras = Compras.objects.all()
    return render(request, 'lista_compras.html', {'compras': compras})


@login_required
def vendas_lista(request):
    vendas = Vendas.objects.all()
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
