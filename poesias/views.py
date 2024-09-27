from django.http import HttpResponse

from django.shortcuts import render

def my_view(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Pagina</title>
</head>
<body>
    <h1>Bem-vindo a minha página Django</h1>
    <p>Esta é minha página Servida através do Django</p>
    
</body>
</html>''')

def user_view(request, username):
    return HttpResponse(f"Perfil do Usuário:{username}")

def root_view(request):
    return HttpResponse("Estamos na raiz: Porta 8000")

def home(request):
    return render(request,'home.html')