from django.db import models

class Article(models.Model):
    """
    Modèle pour représenter un article.
    """
    title = models.CharField(max_length=255, unique=True)  # Titre limité à 255 caractères
    content = models.TextField()             # Contenu sans limite de taille
    author = models.CharField(max_length=50 , default="melissa")
    created_at = models.DateTimeField(auto_now_add=True)  # Ajout automatique de la date de création

    def __str__(self):
        return self.title  # Représentation en texte


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) # Description optionnelle

    def __str__(self):
        return self.name