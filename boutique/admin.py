from django.contrib import admin
from .models import Message, Commande

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'sujet', 'date_envoi', 'lu']
    list_filter = ['lu', 'date_envoi']
    search_fields = ['nom', 'email', 'sujet']
    readonly_fields = ['nom', 'email', 'sujet', 'message', 'date_envoi']
    ordering = ['-date_envoi']

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'produit', 'prix', 'statut', 'date_commande']
    list_filter = ['statut', 'date_commande', 'paiement']
    search_fields = ['nom', 'prenom', 'email', 'produit']
    ordering = ['-date_commande']