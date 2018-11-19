from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import GradoForm
from registro.models import Grado, Materia, Seccion

def grado_nuevo(request):
    if request.method == 'POST':
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Grado Guardado Exitosamente')
            return redirect('/grado/nuevo')
    else:
        formulario = GradoForm()
    return render(request, 'registro/grado_nuevo.html', {'formulario': formulario})
