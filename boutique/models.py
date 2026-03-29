from django.db import models

class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

    class Meta:
        ordering = ['-date_envoi']
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Commande(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    produit = models.CharField(max_length=200)
    prix = models.IntegerField()
    paiement = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='en_attente', choices=[
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ])

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.produit}"

    class Meta:
        ordering = ['-date_commande']
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"