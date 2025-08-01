# Utiliser une image de base Python
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires dans l'image
COPY app/requirements.txt requirements.txt
COPY app/main.py main.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application Flask va tourner
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "main.py"]