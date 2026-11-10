from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear/", views.crear, name="crear"),
    path("editar/<int:pk>/", views.editar, name="editar"),
    path("eliminar/<int:pk>/", views.eliminar, name="eliminar"),
]