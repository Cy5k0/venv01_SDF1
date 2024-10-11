from django.shortcuts import render


def vista_app1(request):
    return render(request, "appcontenido/app1.html")


def vista_con_parametros(request, nombre):
    contexto = {"nombre": nombre}
    return render(request, "appcontenido/app_parametros.html", contexto)


# Create your views here.
