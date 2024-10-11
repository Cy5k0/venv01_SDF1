from django.shortcuts import render


def vista_app1(request):
    return render(request, "vista1.html")


def vista_con_parametros(request, nombre):
    contexto = {"nombre": nombre}
    return render(request, "vista2.html", contexto)


# Create your views here.
