from django.shortcuts import render, redirect
from .models import Producto

def index_productos(request):
    return render(request, 'productos/index_productos.html')

def registrar_producto(request):
    
    if request.method=='POST':
        cod = request.POST.get('cod')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        Producto.objects.create(
            cod=cod,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )

        return redirect('index_productos')
    return render(request,'productos/registrar_producto.html')
