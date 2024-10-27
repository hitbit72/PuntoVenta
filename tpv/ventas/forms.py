# formularios basados en nuestros modelos
from django import forms
from ventas.models import Cliente, Producto
from django.forms.widgets import FileInput

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
            'codigo': 'Código TPV',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
            'precio': 'Precio venta',
            'cantidad': 'Existencias',
            'taxes': 'Impuestos',
        }
        error_messages = {
            'codigo': {'required': 'El campo Código es obligatorio'},
            'descripcion': {'required': 'El campo Descripcion es obligatorio'},
            'precio': {'required': 'El campo Precio es obligatorio'},
        }

class EditProductFrom(forms.ModelForm):
    """
        clase que contiene los campos del formulario
        @autor Jorge Tejada
    """

    # codigo
    codigo = forms.CharField(
        label ='Codigo',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'id': 'codigo_edit',
                'title': 'Codigo del producto',
                'data-toggle': 'tooltip',
                'type': 'text',
            }
        )
    )

    # Descripcion
    descripcion = forms.CharField(
        label ='Descripcion',
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'id': 'descripcion_edit',
                'title': 'Descripcion del producto',
                'data-toggle': 'tooltip',
                'type': 'text',
            }
        )
    )


class EditProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields = '__all__'
        fields = ['codigo','descripcion', 'imagen', 'precio','cantidad','taxes']
        labels = {
            'codigo': 'Código TPV',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
            'precio': 'Precio venta',
            'cantidad': 'Existencias',
            'taxes': 'Impuestos',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'id': 'codigo_edit', 'type': 'text', 'autofocus': True}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_edit', 'type': 'text'}),
            'imagen': FileInput(),
            'precio': forms.TextInput(attrs={'id': 'precio_edit', 'placeholder': '000.00'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_edit', 'placeholder': '000.00' }),
            'taxes': forms.TextInput(attrs={'id': 'taxes_edit', 'placeholder': '000.00'}),
        }
        error_messages = {
            'codigo': {'required': 'El campo Código es obligatorio'},
            'descripcion': {'required': 'El campo Descripcion es obligatorio'},
            'precio': {'required': 'El campo Precio es obligatorio'},
        }
