from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm
from django.contrib import messages
from pyexpat.errors import messages

# Create your views here.
# templates

def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context)


def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print('Guardar cliente')
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save
            except:
                messages(request, 'Error al cargar el cliente')
                return redirect('Clientes')
        else:
            messages(request,'Error, formulario no valido')
    return redirect('Clientes')

def edit_cliente_view(request):
    return redirect('Clientes')

def delete_cliente_view(request):
    return redirect('Clientes')