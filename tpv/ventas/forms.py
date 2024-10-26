# formularios basados en nuestros modelos
from django import forms
from ventas.models import Cliente, Producto


# Formularios clientes **********************************************
class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','dni','telefono')
        labels = {
            'codigo': 'Referencia o mote',
            'nombre': 'Nombre cliente',
            'dni': 'DNI',
            'telefono': 'Teléfono'
        }

class EditClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','dni','telefono')
        labels = {
            'codigo': 'Referencia o mote',
            'nombre': 'Nombre cliente',
            'dni': 'DNI',
            'telefono': 'Teléfono',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_edit'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_edit'}),
            'dni': forms.TextInput(attrs={'id': 'dni_edit'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_edit'}),
        }


# Formularios Productos **********************************************
class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion','imagen','precio','cantidad','taxes')
        labels = {
            'codigo': 'Código:',
            'descripcion': 'Descripcion:',
            'imagen': 'Imagen:',
            'precio': 'Precio venta:',
            'cantidad': 'Existencias:',
            'taxes': 'Impuestos:',
        }