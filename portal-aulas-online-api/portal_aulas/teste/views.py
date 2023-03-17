from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Teste</h1>\n<label>Click me <input type='text' id='User' name='Name' /></label>")

def sobreNos(request):
    return HttpResponse("Sobre o projeto")

def perfil(request):
    return HttpResponse("Meus dados")
