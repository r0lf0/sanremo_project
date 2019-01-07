from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_cantanti/', views.lista_cantanti, name="lista_cantanti"),
    path('vota/<int:concorrente_id>/', views.vota, name="vota")
]
