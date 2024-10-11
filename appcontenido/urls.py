from django.urls import path
from . import views

urlpatterns = [
    path("vista1.html/", views.vista_app1, name="app1"),
    path("app2/", views.vista_con_parametros, name="app2"),
]
