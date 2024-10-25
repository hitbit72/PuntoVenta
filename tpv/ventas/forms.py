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

class EditClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','telefono')
        labels = {
            'codigo': 'Referencia o mote',
            'nombre': 'Nombre cliente',
            'telefono': 'Teleéfono',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_edit'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_edit'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_edit'}),
        }
