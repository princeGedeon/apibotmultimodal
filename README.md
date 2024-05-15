# Api botmultimodal

Ce projet permet de créer un bot multimodal pour diverses applications interactives.

## Installation

### Pré-requis

- Installer un environnement virtuel Python :

```bash
python -m venv env
source env/bin/activate  # Pour Linux/MacOS
env\Scripts\activate  # Pour Windows
```

- Créer un fichier `.env` à la racine du projet et renseigner les API keys nécessaires :

```
GPLACES_API_KEY=...
SERPAPI_API_KEY=...
TAVILY_API_KEY=...
GOOGLE_MAPS_API_KEY=...
GOOGLE_API_KEY=...
OPENAI_API_KEY=...
```

### Dépendances

- Installer les dépendances du projet avec la commande suivante :

```bash
pip install -r requirements.txt
```

### Lancer le serveur

- Pour lancer le serveur, utilisez la commande suivante :

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Vous pouvez ensuite accéder à l'application en utilisant votre navigateur web à l'adresse suivante : `http://0.0.0.0:8000`.

## Utilisation

Après avoir dégmarré le serveur, vous pouvez interagir avec le bot multimodal selon les instructions spécifiques de votre application. N'hésitez pas à consulter la documentation supplémentaire ou les fichiers de configuration pour des détails sur les fonctionnalités disponibles.
Accéder à la page de notre documentation `http://127.0.0.1:8000/docs`