from rest_framework import serializers
from .models import Article
from .models import Category

class ArticleSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour convertir les objets Article en JSON.
    """
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'content', 'created_at']  # Champs à inclure dans le JSON

class CategorySerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour convertir les objets Category en JSON.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  # Champs à inclure dans le JSON
