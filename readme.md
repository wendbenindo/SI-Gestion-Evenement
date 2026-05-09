# Systeme de Gestion d'Événements

Application web permettant de publier des événements et de gérer les inscriptions des participants.

## Stack Technique

### Backend
- **FastAPI** - Framework Python moderne pour API REST
- **SQLAlchemy** - ORM pour la gestion de la base de données
- **SQLite** - Base de données légère et portable
- **Pydantic** - Validation des données

### Frontend
- **React** - Bibliothèque JavaScript pour l'interface utilisateur
- **Vite** - Build tool moderne et rapide

## Prérequis

- Python 3.8+
- Node.js 16+
- npm ou yarn

## Installation et Lancement

### Backend

1. Créer et activer un environnement virtuel :

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

3. Lancer le serveur :

```bash
uvicorn app.main:app --reload

```
L'API sera accessible sur : http://localhost:8000
Documentation interactive : http://localhost:8000/docs

### Frontend
1. Installer les dépendances :
```bash
cd frontend
npm install
```

2. Lancer le serveur de développement :

```bash
npm run dev
```
L'application sera accessible sur : http://localhost:5173