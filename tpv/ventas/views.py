from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm, EditClienteForm, AddProductoForm, EditProductoForm
from django.contrib import messages
import time

# Create your views here.
# templates


def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context)

# visualizacion principal clientes ****************************
def clientes_view(request):
    registros = Cliente.objects.all()
    form_add = AddClienteForm()
    form_editar = EditClienteForm()
    context = {
        'registros': registros,
        'form_add': form_add,
        'form_editar': form_editar,
        'time': time.time(),
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print('Guardar cliente')
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save(commit=True)
                #messages.add_message(request, messages.INFO, 'Formulario guardado correctamente')
                messages.success(request,'Formulario guardado correctamente')
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
    #print('Editar cliente')
    if request.POST:
        # id del registro a editar, en form añadir instance=cliente
        cliente = Cliente.objects.get(pk=request.POST.get('id_edit'))
        form = EditClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            try:
                form.save(commit=True)
                messages.success(request,'Formulario guardado correctamente')
            except:
                messages.warning(request, 'No se guardo el formulario')
                return redirect('Clientes')
        else:
            print(form.errors)
            messages.error(request, 'Formulario no válido')
    return redirect('Clientes')


def delete_cliente_view(request):
    if  request.POST:
        #idCliente = request.POST.get('id_cliente_eliminar')
        #print(f"Delete cliente ID: {idCliente}")
        cliente = Cliente.objects.get(pk=request.POST.get('id_delete'))
        cliente.delete()
        messages.success(request,'Registro eliminado correctamente')
    return redirect('Clientes')


# visualizacion principal productos ***************************************
def productos_view(request):
    registros = Producto.objects.all()
    form_add = AddProductoForm()
    form_editar = EditProductoForm()
    context = {
        'registros': registros,
        'form_add': form_add,
        'form_editar': form_editar,
        'time': time.time(),
    }
    return render(request, 'productos.html', context)


def add_producto_view(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save(commit=True)
                #messages.add_message(request, messages.INFO, 'Formulario guardado correctamente')
                messages.success(request,'Formulario guardado correctamente')
            except:
                messages.warning(request, 'No se guardo el formulario')
                return redirect('Productos')
        else:
            print('form no valido')
            print(form.errors)
            messages.error(request, 'Formulario no válido')
    return redirect('Productos')


def edit_producto_view(request):
    if request.POST:
        # id del registro a editar, en form añadir instance=cliente
        producto = Producto.objects.get(pk=request.POST.get('id_edit'))
        form = EditProductoForm(request.POST, request.FILES, instance=producto)
        form.instance.pk = producto.pk #Agregue esta línea para asegurarme de que la identificación permanezca sin cambios
        img = request.POST.get('id_imagen')

        if form.is_valid():
            #try:
                print(f'pk: {form.instance.pk}')
                if 'imagen' in request.FILES:
                    producto.imagen = request.FILES['imagen']
                    print(producto.imagen)
                else:
                    producto.imagen = img
                    print(producto.imagen)

                #print(f'Formulario: Precio:{request.FILES['precio_edit']} Cantidad:{request.FILES['cantidad_edit']}')
                print('ERRORS: ')
                print(form.errors)
                form.save()
                messages.success(request,'Formulario guardado correctamente')
                """
            except:
                messages.warning(request, 'No se guardo el formulario')
                return redirect('Productos')
                """
        else:
            print("El form no es valido. Error: ", form.errors)
            messages.error(request, 'Formulario no válido', form.errors)
    return redirect('Productos')

def delete_producto_view(request):
    if  request.POST:
        #idCliente = request.POST.get('id_cliente_eliminar')
        #print(f"Delete cliente ID: {idCliente}")
        cliente = Cliente.objects.get(pk=request.POST.get('id_delete'))
        cliente.delete()
        messages.success(request,'Registro eliminado correctamente')
    return redirect('Productos')
