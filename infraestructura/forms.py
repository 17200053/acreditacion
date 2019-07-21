from django import forms
from infraestructura.models import *


class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'Ap_Paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'Ap_Materno': forms.TextInput(attrs={'class': 'form-control'}),
            'Dependencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'Numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReferenciaForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = '__all__'
        widgets = {
            'Numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'Ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'Piso': forms.NumberInput(attrs={'class': 'form-control'}),
            'Pabellon': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DependenciaForm(forms.ModelForm):
    class Meta:
        model = Dependencia
        fields = '__all__'
        widgets = {
            'Codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
        widgets = {
            'Numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Version': forms.TextInput(attrs={'class': 'form-control'}),
            'Fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
        widgets = {
            'Numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'Categoria': forms.NumberInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'Componente': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        widgets = {
            'Numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'Referencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'Codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'Capacidad Maquinas': forms.NumberInput(attrs={'class': 'form-control'}),
            'Programa': forms.NumberInput(attrs={'class': 'form-control'}),
            'Componente': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LaboratorioComponenteForm(forms.ModelForm):
    class Meta:
        model = LaboratorioComponente
        fields = '__all__'
        widgets = {
            'NumeroLabo': forms.NumberInput(attrs={'class': 'form-control'}),
            'NumComponente': forms.NumberInput(attrs={'class': 'form-control'}),
            'Serie': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LaboratorioProgramaForm(forms.ModelForm):
    class Meta:
        model = LaboratorioProgramas
        fields = '__all__'
        widgets = {
            'NumeroLabo': forms.NumberInput(attrs={'class': 'form-control'}),
            'NumPrograma': forms.NumberInput(attrs={'class': 'form-control'}),
            'NumPC': forms.NumberInput(attrs={'class': 'form-control'}),
        }
