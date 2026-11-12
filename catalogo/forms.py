from django import forms
from .models import Producto, ConsultaCliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "precio", "stock", "imagen"]


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = ConsultaCliente
        fields = ["nombre", "correo", "producto", "mensaje"]

    def clean_mensaje(self):
        mensaje = self.cleaned_data["mensaje"]
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return mensaje