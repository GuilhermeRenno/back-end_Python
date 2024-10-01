from django.urls import path
from poesias.views import contatos,root_view,user_view,home,contexto,sobre,produtos

urlpatterns = [
    path('home/', home),
    path('sobre/', sobre),
    path('contatos/', contatos),
    path('produtos/', produtos),
    path('user/<str:username>/',user_view),
    path('',root_view),
    path('contexto',contexto)
    
]