from django.urls import path

from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('index',views.index, name='index'),

    path('list_encargado', views.list_encargados, name='list_encargado'),
    path('create_encargado', views.EncargadoCreate.as_view(), name='create_encargado'),
    path(r'edit_encargado/(?P<pk>\d+)/$', views.EncargadoEdit.as_view(), name='edit_encargado'),
    path(r'delete_encargado/(?P<pk>\d+)/$', views.EncargadoDelete.as_view(), name='delete_encargado'),

    path('list_referencia', views.list_referencias, name='list_referencia'),
    path('create_referencia', views.ReferenciaCreate.as_view(), name='create_referencia'),
    path(r'edit_referencia/(?P<pk>\d+)/$', views.ReferenciaEdit.as_view(), name='edit_referencia'),
    path(r'delete_referencia/(?P<pk>\d+)/$', views.ReferenciaDelete.as_view(), name='delete_referencia'),

    path('list_categoria', views.list_categorias, name='list_categoria'),
    path('create_categoria', views.CategoriaCreate.as_view(), name='create_categoria'),
    path(r'edit_categoria/(?P<pk>\d+)/$', views.CategoriaEdit.as_view(), name='edit_categoria'),
    path(r'delete_categoria/(?P<pk>\d+)/$', views.CategoriaDelete.as_view(), name='delete_categoria'),

    path('list_programa', views.list_programas, name='list_programa'),
    path('create_programa', views.ProgramaCreate.as_view(), name='create_programa'),
    path(r'edit_programa/(?P<pk>\d+)/$', views.ProgramaEdit.as_view(), name='edit_programa'),
    path(r'delete_programa/(?P<pk>\d+)/$', views.ProgramaDelete.as_view(), name='delete_programa'),

    path('list_dependencia', views.list_dependencias, name='list_dependencia'),
    path('create_dependencia', views.DependenciaCreate.as_view(), name='create_dependencia'),
    path(r'edit_dependencia/(?P<pk>\d+)/$', views.DependenciaEdit.as_view(), name='edit_dependencia'),
    path(r'delete_dependencia/(?P<pk>\d+)/$', views.DependenciaDelete.as_view(), name='delete_dependencia'),

    path('list_laboratorio', views.list_laboratorios, name='list_laboratorio'),
    path('create_laboratorio', views.LaboratorioCreate.as_view(), name='create_laboratorio'),
    path(r'edit_laboratorio/(?P<pk>\d+)/$', views.LaboratorioEdit.as_view(), name='edit_laboratorio'),
    path(r'delete_laboratorio/(?P<pk>\d+)/$', views.LaboratorioDelete.as_view(), name='delete_laboratorio'),
    path('detalle_laboratorio', views.detalle_Laboratorio, name='detalle_laboratorio'),


    path('list_componente', views.list_componentes, name='list_componente'),
    path('create_componente', views.ComponenteCreate.as_view(), name='create_componente'),
    path(r'edit_componente/(?P<pk>\d+)/$', views.ComponenteEdit.as_view(), name='edit_componente'),
    path(r'delete_componente/(?P<pk>\d+)/$', views.ComponenteDelete.as_view(), name='delete_componente'),

    path('list_componenteLaboratorio', views.list_componentesLaboratorio, name='list_componenteLaboratorio'),
    path('create_componenteLaboratorio', views.LaboratorioComponenteCreate.as_view(), name='create_componenteLaboratorio'),
    path(r'edit_componenteLaboratorio/(?P<pk>\d+)/$', views.LaboratorioComponenteEdit.as_view(), name='edit_componenteLaboratorio'),
    path(r'delete_componenteLaboratorio/(?P<pk>\d+)/$', views.LaboratorioComponenteDelete.as_view(), name='delete_componenteLaboratorio'),

    path('create_programaLaboratorio', views.LaboratorioProgramaCreate.as_view(), name='create_programaLaboratorio'),
    path(r'edit_programaLaboratorio/(?P<pk>\d+)/$', views.LaboratorioProgramaEdit.as_view(), name='edit_programaLaboratorio'),
    path(r'delete_programaLaboratorio/(?P<pk>\d+)/$', views.LaboratorioProgramaDelete.as_view(), name='delete_programaLaboratorio'),
]