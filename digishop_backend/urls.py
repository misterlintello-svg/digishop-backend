from django.contrib import admin
from django.urls import path
from boutique import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/message/', views.envoyer_message),
    path('api/commande/', views.envoyer_commande),
]