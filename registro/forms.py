from django import forms
from .models import Grado, Materia, Seccion

class GradoForm(forms.ModelForm):

    class Meta:
        model = Grado
        fields = [
            'nombre',
            'seccion',
            'materia',

        ]
        labels = {
            'nombre': 'Nombre',
            'seccion': 'Seccion',
            
            'materia': 'Cursos',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'seccion': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.CheckboxSelectMultiple(),
        }
