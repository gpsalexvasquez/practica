from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')  # más ligero

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
    

def obtener_respuesta(pregunta):
    productos = list(Producto.objects.all())
    corpus = [f"{p.nombre} {p.descripcion}" for p in productos]
    pregunta_embedding=model.encode(pregunta, convert_to_tensor=True)    
    corpus_embeddings=model.encode(corpus, convert_to_tensor=True)

    similitudes = util.cos_sim(pregunta_embedding, corpus_embeddings)[0]
    idx = similitudes.argmax().item()

    producto_mas_relevante = productos[idx]
    if "precio" in pregunta.lower():
        return f"El precio de {producto_mas_relevante.nombre} \
            es S/ {producto_mas_relevante.precio}"
    elif "stock" in pregunta.lower() or "hay" in pregunta.lower():
        return f"Hay {producto_mas_relevante.stock} \
            unidades de {producto_mas_relevante.nombre}"
    else:
        return f"{producto_mas_relevante.nombre}: \
            S/{producto_mas_relevante.precio}, \
                {producto_mas_relevante.stock} unidades disponibles"


