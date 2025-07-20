from rest_framework import serializers
from .models import Article
from .models import Category

class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Article incluant des validations simples.
    """
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']

    def validate_title(self, value):
        """
        Vérifie que le titre comporte au moins 5 caractères.
        """
        if len(value) < 5:
            raise serializers.ValidationError("Le titre doit contenir au moins 5 caractères.")
        return value

    def validate_content(self, value):
        """
        Vérifie plusieurs règles pour le champ content :
        1. Ne doit pas être vide.
        2. Ne doit pas contenir de mots interdits.
        """
        # Vérifier que le contenu n'est pas vide
        if not value.strip():
            raise serializers.ValidationError("Le contenu ne peut pas être vide.")

        # Vérifier les mots interdits
        forbidden_words = ["spam", "fake"]
        for word in forbidden_words:
            if word in value.lower(): # .lower() pour une recherche insensible à la casse
                raise serializers.ValidationError(
                    f"Le mot '{word}' est interdit dans le contenu."
                )
        return value

    def validate(self, data):
        """
        Vérifie que le titre commence par '[Urgent]' si le contenu mentionne 'urgent'.
        """
        content_lower = data['content'].lower()
        title = data['title']
        if "urgent" in content_lower and not title.startswith("[Urgent]"):
            raise serializers.ValidationError(
                "Si le contenu contient 'urgent', le titre doit commencer par '[Urgent]'."
            )
        return data

class CategorySerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour convertir les objets Category en JSON.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  # Champs à inclure dans le JSON
