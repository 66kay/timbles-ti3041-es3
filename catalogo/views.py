from django.shortcuts import render, redirect
from .forms import ProductoForm,ConsultaForm 
from .models import Producto
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Avg, Sum

def inicio(request):
    productos = Producto.objects.all()
    categorias = Producto.objects.values_list("categoria", flat=True).distinct().order_by("categoria")

    categoria = request.GET.get("categoria", "")
    busqueda = request.GET.get("q", "").strip()

    if categoria:
        productos = productos.filter(categoria=categoria)
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    visitas = request.session.get("visitas", 0) + 1
    request.session["visitas"] = visitas

    contexto = {
        "productos": productos,
        "categorias": categorias,
        "categoria_actual": categoria,
        "busqueda": busqueda,
        "visitas": visitas,
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

def reporte_categorias(request):
    resumen = Producto.objects.values("categoria").annotate(
        cantidad=Count("id"),
        precio_promedio=Avg("precio"),
        stock_total=Sum("stock"),
    ).order_by("categoria")
    return render(request, "catalogo/reporte_categorias.html", {"resumen": resumen})

def reporte_stock_critico(request):
    productos = Producto.objects.filter(stock__lte=5).order_by("stock", "nombre")
    return render(request, "catalogo/reporte_stock.html", {"productos": productos})

def contacto(request):
    enviado = False
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            enviado = True
            form = ConsultaForm()
    else:
        form = ConsultaForm()
    return render(request, "catalogo/contacto.html", {"form": form, "enviado": enviado})