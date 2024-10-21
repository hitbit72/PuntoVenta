# formularios basados en nuestros modelos
from django import forms
from ventas.models import Cliente


class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','telefono')
        labels = {
            'codigo': 'Referencia o mote',
            'nombre': 'Nombre cliente',
            'telefono': 'Teléfono'
        }
