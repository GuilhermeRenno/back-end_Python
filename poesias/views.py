from django.http import HttpResponse

from django.shortcuts import render

def contatos(request):
    return render(request,'contatos.html')

def sobre(request):
    return render(request,'sobre.html')

def produtos(request):
    return render(request,'produtos.html')

def user_view(request, username):
    return HttpResponse(f"Perfil do Usuário:{username}")

def root_view(request):
    return HttpResponse("Estamos na raiz: Porta 8000")

def home(request):
    return render(request,'home.html')

def contexto(request):
    context={
        'nome':'joão',
        'idade':30,
        'hobbies':['Leitura','Ciclismo','Cozinhar']
    }
    return render(request, 'contexto.html', context)