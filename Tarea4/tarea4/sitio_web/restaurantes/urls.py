from django.conf.urls import url

from restaurantes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^restaurante/(?P<id>[0-9]+)$', views.restaurante, name='restaurante'),
]
