from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto
from django.contrib.admin.views.decorators import staff_member_required


def inicio(request):
    productos = Producto.objects.all()
    categorias = Producto.objects.values_list("categoria", flat=True).distinct().order_by("categoria")

    categoria = request.GET.get("categoria", "")
    busqueda = request.GET.get("q", "").strip()

    if categoria:
        productos = productos.filter(categoria=categoria)
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    contexto = {
        "productos": productos,
        "categorias": categorias,
        "categoria_actual": categoria,
        "busqueda": busqueda,
    }
    return render(request, "catalogo/index.html", contexto)

@staff_member_required
def crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ProductoForm()
    return render(request, "catalogo/form.html", {"form": form, "titulo": "Nuevo producto"})

@staff_member_required
def editar(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "catalogo/form.html", {"form": form, "titulo": "Editar producto"})

@staff_member_required
def eliminar(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("inicio")
    return render(request, "catalogo/confirmar_eliminar.html", {"producto": producto})