from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('items/', views.list_items, name='list_items'),
    path('items/<int:item_id>/', views.get_item, name='get_item'),
    path('users/<str:username>/' , views.get_user, name='get_user'),
    path('articles/', views.article_list_create, name='article_list_create'),
    path('articles/search/', views.search_articles, name='search_articles'),
    path('articles/<int:id>/', views.article_detail_update_delete, name='article_detail_update_delete'),  # Détail, mise à jour, suppression
    path('categories/', views.list_categories, name='list_categories'),
]