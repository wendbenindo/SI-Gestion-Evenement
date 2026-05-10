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
py -m venv venv
# OU
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


##  Base de Données
### Création automatique

La base de données SQLite est **créée automatiquement** au premier lancement du backend.

**Emplacement :** `backend/database/events.db`

Les tables `events` et `registrations` sont générées automatiquement par SQLAlchemy à partir des modèles définis dans `backend/app/models.py`.

**Aucune action manuelle n'est requise !** 

### Structure des tables

**Table `events` :**
- `id` : Identifiant unique (auto-généré)
- `title` : Titre de l'événement (max 100 caractères)
- `description` : Description optionnelle
- `date` : Date et heure de l'événement
- `location` : Lieu de l'événement
- `capacity` : Capacité maximale (> 0)
- `created_at` : Date de création (auto-généré)

**Table `registrations` :**
- `id` : Identifiant unique (auto-généré)
- `event_id` : Référence vers l'événement
- `first_name` : Prénom du participant
- `last_name` : Nom du participant
- `email` : Email du participant (unique par événement)
- `registered_at` : Date d'inscription (auto-généré)


##  API Endpoints

### Documentation interactive

Accédez à `http://localhost:8000/docs` pour tester tous les endpoints via l'interface Swagger.

### Endpoints disponibles

**Événements :**
- `GET /api/events` - Liste des événements (avec filtres ?search= et ?date=)
- `POST /api/events` - Créer un événement
- `GET /api/events/{id}` - Détail d'un événement
- `PUT /api/events/{id}` - Modifier un événement
- `DELETE /api/events/{id}` - Supprimer un événement

**Inscriptions :**
- `POST /api/events/{id}/register` - S'inscrire à un événement
- `GET /api/events/{id}/registrations` - Liste des participants
- `DELETE /api/registrations/{id}` - Annuler une inscription


##  Fonctionnalités Principales

### Côté utilisateur
1. **Consulter les événements** avec recherche par titre
2. **Voir le détail** d'un événement avec compteur de places
3. **S'inscrire** à un événement (si places disponibles)
4. **Créer un événement** (optionnel mais implémenté)

### Côté technique
1. **Validation automatique** des données (Pydantic)
2. **Gestion des erreurs** avec messages clairs
3. **Mise à jour en temps réel** du compteur de places



##  Auteur

Test technique - Poste Développeur Full Stack  
Durée : 24 heures  
Date : 10 Mai 2026

