from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-nos', views.sobreNos, name='sobreNos'),
    path('perfil', views.perfil, name='perfil'),
]