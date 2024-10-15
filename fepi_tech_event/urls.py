from django.urls import path
from fepi_tech_event.views import homeevento

urlpatterns = [
    path('homeevento/',homeevento ),
]