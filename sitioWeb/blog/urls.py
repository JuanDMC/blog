from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_post, name='detalle_post'),
    url(r'^post/new/$', views.nuevo_post, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_post, name='editar_post'),
    url(r'^borradores/$', views.lista_borradores, name='lista_borradores'),
]