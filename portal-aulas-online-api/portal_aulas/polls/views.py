from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

def sobreNos(request):
    return HttpResponse("Sobre o projeto")

def perfil(request):
    return HttpResponse("Meus dados")
