from django.urls import path
from poesias.views import my_view,root_view,user_view,home,contexto

urlpatterns = [
    path('home/', home),
    path('sobre/', my_view),
    path('user/<str:username>/',user_view),
    path('',root_view),
    path('contexto',contexto)
    
]