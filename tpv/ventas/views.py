from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm
from django.contrib import messages
#from pyexpat.errors import messages
import time

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
        'time': time.time(),
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print('Guardar cliente')
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save(commit=True)
                #messages.add_message(request, messages.INFO, 'Formulario guardado correctamente')
                #messages.success(request,'Formulario guardado correctamente')
                #messages.success(request,'Formulario guardado correctamente')
                messages.add_message(request,messages.SUCCESS,'Formulario guardado correctamente')
            except:
                messages.warning(request, 'No se guardo el formulario')
                print(form.errors)
                #return redirect('Clientes')
        else:
            print('form no valido')
            print(form.errors)
            messages.error(request, 'Formulario no válido')
    return redirect('Clientes')

def edit_cliente_view(request):
    return redirect('Clientes')

def delete_cliente_view(request):
    if  request.POST:
        #idCliente = request.POST.get('id_cliente_eliminar')
        #print(f"Delete cliente ID: {idCliente}")
        cliente = Cliente.objects.get(pk=request.POST.get('id_cliente_eliminar'))
        cliente.delete()
        messages.success(request,'Cliente eliminado correctamente')
    return redirect('Clientes')