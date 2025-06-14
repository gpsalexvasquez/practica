from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def index_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index_productos.html',
                  {'productos':productos})

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

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method =='POST':
        producto.cod = request.POST.get('cod')
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
        return redirect('index_productos')
    return render(request, 'productos/editar_producto.html',{'producto':producto})

def eliminar_producto(request, id):
    if request.method=='POST':
        producto = Producto.objects.get(pk=id)
        producto.delete()
        return JsonResponse({'success':True})
    







