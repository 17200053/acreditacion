from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import *
from django.urls import reverse
from .models import *
from .forms import *

def index(request):
    return render(request,template_name='blank.html')

def list_encargados(request):
    encargado = Encargado.objects.all()
    return render(request, template_name='list_encargados.html', context={'encargado': encargado})

class EncargadoCreate(CreateView):
    model = Encargado
    form_class = EncargadoForm
    template_name = 'add_encargado.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class EncargadoEdit(UpdateView):
    model = Encargado
    form_class = EncargadoForm
    template_name = 'edit_encargado.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class EncargadoDelete(DeleteView):
    model = Encargado
    form_class = EncargadoForm
    template_name = 'delete_encargado.html'

    def get_context_data(self, **kwargs):
        context_data = super(EncargadoDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        encargado=Encargado.objects.get(enc_codigo=pk)
        context_data.update({'encargado':encargado})
        return context_data

    def get_success_url(self):
        return reverse('list_laboratorio')


def list_referencias(request):
    referencia = Referencia.objects.all()
    return render(request, template_name='list_referencias.html', context={'referencia': referencia})

class ReferenciaCreate(CreateView):
    model = Referencia
    form_class = ReferenciaForm
    template_name = 'add_referencia.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class ReferenciaEdit(UpdateView):
    model = Referencia
    form_class = ReferenciaForm
    template_name = 'edit_referencia.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class ReferenciaDelete(DeleteView):
    model = Referencia
    form_class = ReferenciaForm
    template_name = 'delete_referencia.html'

    def get_context_data(self, **kwargs):
        context_data = super(ReferenciaDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        referencia=Referencia.objects.get(ref_id=pk)
        context_data.update({'referencia':referencia})
        return context_data

    def get_success_url(self):
        return reverse('list_laboratorio')

def list_categorias(request):
    categoria = Categoria.objects.all()
    return render(request, template_name='list_categorias.html', context={'categoria': categoria})

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'add_categoria.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class CategoriaEdit(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'edit_categoria.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class CategoriaDelete(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'delete_categoria.html'

    def get_context_data(self, **kwargs):
        context_data = super(CategoriaDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        categoria=Categoria.objects.get(cat_id=pk)
        context_data.update({'categoria':categoria})
        return context_data

    def get_success_url(self):
        return reverse('list_laboratorio')


def list_dependencias(request):
    dependencia = Dependencia.objects.all()
    return render(request, template_name='list_dependencias.html', context={'dependencia': dependencia})

class DependenciaCreate(CreateView):
    model = Dependencia
    form_class = DependenciaForm
    template_name = 'add_Dependencia.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class DependenciaEdit(UpdateView):
    model = Dependencia
    form_class = DependenciaForm
    template_name = 'edit_dependencia.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class DependenciaDelete(DeleteView):
    model = Dependencia
    form_class = DependenciaForm
    template_name = 'delete_dependencia.html'

    def get_context_data(self, **kwargs):
        context_data = super(DependenciaDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        dependencia=Dependencia.objects.get(dpn_codigo=pk)
        context_data.update({'dependencia':dependencia})
        return context_data

    def get_success_url(self):
        return reverse('list_laboratorio')

def list_programas(request):
    programa = Programa.objects.all()
    return render(request, template_name='list_programas.html', context={'programa': programa})

class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'add_Programa.html'

    def get_success_url(self):
        return reverse('list_programa')

class ProgramaEdit(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'edit_programa.html'

    def get_success_url(self):
        return reverse('list_programa')

class ProgramaDelete(DeleteView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'delete_programa.html'

    def get_context_data(self, **kwargs):
        context_data = super(ProgramaDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        programa=Programa.objects.get(prg_id=pk)
        context_data.update({'programa':programa})
        return context_data

    def get_success_url(self):
        return reverse('list_programa')

def list_componentes(request):
    componente = Componente.objects.all()
    categoria= Categoria.objects.all()
    return render(request, template_name='list_componentes.html', context={'componente': componente,'categoria':categoria})

class ComponenteCreate(CreateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'add_Componente.html'

    def get_success_url(self):
        return reverse('list_componente')

class ComponenteEdit(UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'edit_componente.html'

    def get_success_url(self):
        return reverse('list_componente')

class ComponenteDelete(DeleteView):
    model = Componente
    form_class =ComponenteForm
    template_name = 'delete_componente.html'

    def get_context_data(self, **kwargs):
        context_data = super(ComponenteDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        componente=Componente.objects.get(comp_id=pk)
        context_data.update({'componente':componente})
        return context_data

    def get_success_url(self):
        return reverse('list_componente')

def list_laboratorios(request):
    laboprg = LaboratorioProgramas.objects.all()
    labocomp = LaboratorioComponente.objects.all()
    encargado = Encargado.objects.all()
    referencia = Referencia.objects.all()
    laboratorio = Laboratorio.objects.all()
    componente= Componente.objects.all()
    programa=Programa.objects.all()
    return render(request, template_name='list_laboratorios.html', context={'laboratorio': laboratorio,'encargado': encargado,'referencia': referencia ,'labocomp': labocomp, 'componente':componente, 'programa':programa, 'laboprg':laboprg})

def detalle_Laboratorio(request):
    labo = request.POST.get('laboId',False)
    laboprg = LaboratorioProgramas.objects.all()
    labocomp = LaboratorioComponente.objects.all()
    encargado = Encargado.objects.all()
    referencia = Referencia.objects.all()
    laboratorio = Laboratorio.objects.get(labo_id=labo)
    componente = Componente.objects.all()
    programa = Programa.objects.all()
    return render(request, template_name='detalle_laboratorio.html',
                                  context={'laboratorio': laboratorio, 'encargado': encargado, 'referencia': referencia,
                                           'labocomp': labocomp, 'componente': componente, 'programa': programa, 'laboprg': laboprg})

class LaboratorioCreate(CreateView):
    model = Laboratorio
    form_class =LaboratorioForm
    template_name = 'add_Laboratorio.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioEdit(UpdateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'edit_laboratorio.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioDelete(DeleteView):
    model = Laboratorio
    form_class =LaboratorioForm
    template_name = 'delete_laboratorio.html'

    def get_context_data(self, **kwargs):
        context_data = super(LaboratorioDelete, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        laboratorio=Laboratorio.objects.get(labo_id=pk)
        context_data.update({'laboratorio':laboratorio})
        return context_data

    def get_success_url(self):
        return reverse('list_laboratorio')

def list_componentesLaboratorio(request):
    compLabo = LaboratorioComponente.objects.all()
    return render(request, template_name='list_labocomponente.html', context={'compLabo': compLabo})

class LaboratorioComponenteCreate(CreateView):
    model = LaboratorioComponente
    form_class =LaboratorioComponenteForm
    template_name = 'add_componenteLabo.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioComponenteEdit(UpdateView):
    model = LaboratorioComponente
    form_class = LaboratorioComponenteForm
    template_name = 'edit_componenteLabo.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioComponenteDelete(DeleteView):
    model = LaboratorioComponente
    form_class = LaboratorioComponenteForm
    template_name = 'delete_componenteLabo.html'

    def get_context_data(self, **kwargs):
            context_data = super(LaboratorioComponenteDelete, self).get_context_data(**kwargs)
            pk = self.kwargs.get('pk')
            cmplabo = LaboratorioComponente.objects.get(id=int(pk))
            context_data.update({'cmplabo': cmplabo})
            return context_data

    def get_success_url(self):
            return reverse('list_laboratorio')


class LaboratorioProgramaCreate(CreateView):
    model = LaboratorioProgramas
    form_class =LaboratorioProgramaForm
    template_name = 'add_programaLabo.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioProgramaEdit(UpdateView):
    model = LaboratorioProgramas
    form_class = LaboratorioProgramaForm
    template_name = 'edit_programaLabo.html'

    def get_success_url(self):
        return reverse('list_laboratorio')

class LaboratorioProgramaDelete(DeleteView):
    model = LaboratorioProgramas
    form_class = LaboratorioProgramaForm
    template_name = 'delete_programaLabo.html'

    def get_context_data(self, **kwargs):
            context_data = super(LaboratorioProgramaDelete, self).get_context_data(**kwargs)
            pk = self.kwargs.get('pk')
            prglabo = LaboratorioProgramas.objects.get(id=int(pk))
            context_data.update({'prglabo': prglabo})
            return context_data

    def get_success_url(self):
            return reverse('list_laboratorio')