from django.shortcuts import render

def index_productos(request):
    return render(request, 'productos/index_productos.html')

