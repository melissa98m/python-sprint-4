from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer
from .models import Category 
from .serializers import CategorySerializer 



def hello_world(request):
    return JsonResponse({"message": "Bienvenue dans votre API Django REST"})

def list_items(request):
    items = [
        {"id": 1, "name": "Article A"},
        {"id": 2, "name": "Article B"},
        {"id": 3, "name": "Article C"},
    ]
    return JsonResponse(items, safe=False)

def get_item(request, item_id):
    """
    Vue qui récupère un élément précis selon son ID passé dans l'URL.
    """
    items = [
        {"id": 1, "name": "Clé USB"},
        {"id": 2, "name": "Souris"},
        {"id": 3, "name": "Clavier"},
    ]

    # Recherche dans la liste statique
    item = next((i for i in items if i["id"] == item_id), None)

    if item:
        return JsonResponse(item)
    return JsonResponse({"error": "Élément non trouvé"}, status=404)


def get_user(request, username):
    """
    Vue qui récupère un élément précis selon son ID passé dans l'URL.
    """
    users = [
    {"username": "alice", "email": "alice@example.com"},
    {"username": "bob", "email": "bob@example.com"},
    {"username": "carol", "email": "carol@example.com"},
    ]

    # Recherche dans la liste statique
    user = next((i for i in users if i["username"] == username), None)

    if user:
        return JsonResponse(user)
    return JsonResponse({"error": "Élément non trouvé"}, status=404)


@api_view(['GET'])
def list_articles(request):
    """
    Vue pour retourner tous les articles en JSON.
    """
    articles = Article.objects.all()  # Récupère tous les articles
    serializer = ArticleSerializer(articles, many=True)  # Sérialise la liste
    return Response(serializer.data)  # Retourne les données JSON

@api_view(['GET'])
def search_articles(request):
    """
    Vue pour rechercher des articles par titre.
    Attend un paramètre d'URL `q`, ex: /api/articles/search/?q=Django
    """
    query = request.query_params.get('q', None) # Récupère le mot-clé 'q'

    if query is not None:
        # Filtre les articles dont le titre contient le mot-clé (insensible à la casse)
        articles = Article.objects.filter(title__icontains=query)
    else:
        # Si aucun mot-clé n'est fourni, retourne une liste vide ou tous les articles
        articles = Article.objects.all() # Ou Article.objects.none() pour une liste vide

    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_categories(request):
    """
    Vue pour retourner toutes les catégories en JSON.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
