from django.http import HttpResponse

from django.shortcuts import render

def my_view(request):
    return HttpResponse("Uma teste String de resposta")

def user_view(request, username):
    return HttpResponse(f"Perfil do Usuário:{username}")

def root_view(request):
    return HttpResponse("Estamos na raiz: Porta 8000")
