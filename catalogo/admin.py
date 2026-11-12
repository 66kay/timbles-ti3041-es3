from django.contrib import admin
from .models import Producto, ConsultaCliente

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "stock")
    search_fields = ("nombre",)
    list_filter = ("categoria",)

@admin.register(ConsultaCliente)
class ConsultaClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "producto", "fecha")
    search_fields = ("nombre", "correo")
