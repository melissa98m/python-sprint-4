# 🐍 Projet Django (v3.9) — Docker Ready

Ce dépôt contient un projet Django configuré pour tourner dans un environnement Docker. Il inclut un service web exposé sur le port 8000, avec persistance des données via un volume Docker.

---

## 🧱 Prérequis

- Docker
- Docker Compose

---

## 🚀 Démarrage rapide

1. Clone le dépôt :

   ```bash
   git clone <url-du-repo>
   cd <nom-du-repo>

Lance les services Docker :

  ```bash
    docker compose up --build

Accède à l'application :
👉 http://0.0.0.0:8000

⚙️ Configuration de la base de données
Ce projet utilise SQLite avec le fichier de base de données stocké dans un volume Docker (db-data), ce qui garantit la persistance même après l'arrêt du conteneur.

📂 Chemin du fichier SQLite
python
Copier
Modifier
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3'
    }
}
Le dossier db/ est monté dans un volume Docker via cette ligne dans docker-compose.yml :

yaml
Copier
Modifier
- db-data:/app/db
Ce volume persiste la base de données en dehors du conteneur, dans un volume nommé db-data.


⚙️ Commandes utiles
Toutes les commandes suivantes s'exécutent dans le conteneur web.

🔁 Appliquer les migrations
bash

docker compose exec web python manage.py migrate
🏗️ Créer les fichiers de migration
bash
docker compose exec web python manage.py makemigrations
👤 Créer un superutilisateur
bash

docker compose exec web python manage.py createsuperuser
🐚 Accéder au shell Django
bash

docker compose exec web python manage.py shell
🧪 Lancer les tests (si définis)
bash

docker compose exec web python manage.py test
🔄 Rebuilder le conteneur
bash

docker compose up --build

🛠️ Développement
Les fichiers de l’application sont montés directement dans le conteneur (.:/app). Toute modification de code est donc prise en compte instantanément, sans besoin de reconstruire l’image.

Le fichier de base de données SQLite est stocké dans le volume db-data, ce qui permet de conserver les données même si le conteneur est supprimé ou reconstruit.


📚 Documentation Django
Django Project

Django Docs

