from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleSerializer
from .models import Category 
from .serializers import CategorySerializer 
from .pagination import CustomPagination


class ArticleListView(ListAPIView):
    """
    Vue pour lister les articles avec une pagination personnalisée.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination

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

@api_view(['GET', 'POST'])
def article_list_create(request):
    """
    Gérer la liste des articles (GET) et la création d'un article (POST).
    Le GET permet de filtrer les articles par titre.
    """
    if request.method == 'GET':
        # Récupère tous les articles par défaut
        articles = Article.objects.all()

        # Récupérer le paramètre 'title' de l'URL (ex: /api/articles/?title=Django)
        title_query = request.query_params.get('title', None)
        if title_query is not None:
            # Filtrer le queryset si le paramètre 'title' est fourni
            # '__icontains' permet une recherche insensible à la casse et partielle
            articles = articles.filter(title__icontains=title_query)

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # (Aucun changement dans la partie POST)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, id):
    """
    Gérer un article spécifique (GET, PUT, DELETE).
    """
    try:
        article = Article.objects.get(pk=id)  # Récupérer l'article avec l'ID donné
    except Article.DoesNotExist:
        return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Lire un article spécifique
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Mettre à jour un article
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Supprimer un article
        article.delete()
        return Response({'message': 'Article deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def list_categories(request):
    """
    Vue pour retourner toutes les catégories en JSON.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


