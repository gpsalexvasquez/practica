from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm

def lista_perfiles(request):
    perfiles = Perfil.objects.all().order_by('-fecha_publicacion')
    return render(request, 'perfil/perfil_index.html', {'perfiles': perfiles})

def crear_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perfiles')
    else:
        form = PerfilForm()
    return render(request, 'perfil/formulario.html', {'form': form})

def editar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('lista_perfiles')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil/formulario.html', {'form': form})

def eliminar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        perfil.delete()
        return redirect('lista_perfiles')
    return render(request, 'perfil/confirmar_eliminar.html', {'perfil': perfil})
