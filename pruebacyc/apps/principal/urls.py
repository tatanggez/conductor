from django.conf.urls import url,include
from .views import menu,mapa,editarPerfil,coords_save,coords_obtener,coords_eliminar,index,index2,coords_save2

urlpatterns = [
    url(r'^$', menu, name='menu'),
    url(r'^mapeo$', mapa, name='mapeo'),
    url(r'^mapa/$', index, name='index'),
    url(r'^editarPerfil(?P<user_id>\d+)/$', editarPerfil, name='editar'),
    url(r'^coords/save$', coords_save, name='coords_save'),
    url(r'^coords/save2$', coords_save2, name='coords_save2'),
    url(r'^coords/obtener$', coords_obtener, name='coords_obtener'),
    url(r'^coords/eliminar$', coords_eliminar, name='coords_eliminar'),
	url(r'^viaje$', index2, name='index2'),
    
]