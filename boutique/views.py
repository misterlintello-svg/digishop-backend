from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Message, Commande
import json

@csrf_exempt
@require_http_methods(["POST"])
def envoyer_message(request):
    try:
        data = json.loads(request.body)
        nom = data.get('nom', '').strip()
        email = data.get('email', '').strip()
        sujet = data.get('sujet', '').strip()
        message = data.get('message', '').strip()

        if not all([nom, email, sujet, message]):
            return JsonResponse({
                'status': 'error',
                'message': 'Veuillez remplir tous les champs.'
            })

        Message.objects.create(
            nom=nom,
            email=email,
            sujet=sujet,
            message=message
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Message enregistré avec succès !'
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })


@csrf_exempt
@require_http_methods(["POST"])
def envoyer_commande(request):
    try:
        data = json.loads(request.body)
        nom = data.get('nom', '').strip()
        prenom = data.get('prenom', '').strip()
        email = data.get('email', '').strip()
        whatsapp = data.get('whatsapp', '').strip()
        produit = data.get('produit', '').strip()
        prix = data.get('prix', 0)
        paiement = data.get('paiement', '').strip()
        message = data.get('message', '').strip()

        if not all([nom, prenom, email, whatsapp, produit, paiement]):
            return JsonResponse({
                'status': 'error',
                'message': 'Veuillez remplir tous les champs obligatoires.'
            })

        Commande.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            whatsapp=whatsapp,
            produit=produit,
            prix=int(prix),
            paiement=paiement,
            message=message
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Commande enregistrée avec succès !'
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })