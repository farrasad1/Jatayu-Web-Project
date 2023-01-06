from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map),
    path('tentang/', views.tentang),
    path('kontak/', views.kontak),
    path('unduh/', views.unduh)
]