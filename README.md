# Travel Partner Chatbot

**Travel Partner Chatbot** est un assistant de voyage intelligent basé sur l'intelligence artificielle, conçu pour simplifier et personnaliser la planification de voyages. Ce projet combine des techniques avancées de traitement du langage naturel (NLP), des API externes, et une interface utilisateur intuitive pour offrir une expérience de planification de voyage fluide et personnalisée.

---

## Fonctionnalités Principales

- **Génération de Plans de Voyage** : Crée des itinéraires personnalisés en fonction des préférences de l'utilisateur (destination, budget, centres d'intérêt).
- **Analyse de Sentiment** : Analyse les sentiments des messages de l'utilisateur en temps réel pour adapter les réponses.
- **Extraction d'Entités** : Identifie et catégorise les entités clés (lieux, dates, etc.) dans les conversations.
- **Mémoire Conversationnelle** : Utilise une base de données vectorielle (ChromaDB) pour stocker et rechercher des conversations passées.
- **Intégration d'APIs Externes** : 
  - **OpenWeatherMap** : Fournit des prévisions météorologiques.
  - **FourSquare** : Recommande des attractions locales.
  - **Serper** : Recherche des informations pertinentes sur le web.
- **Interface Utilisateur Interactive** : Développée avec **Streamlit**, elle permet une interaction fluide et intuitive.
- **Export de Plans** : Génère et exporte des plans de voyage au format PDF.

---

## Architecture du Projet

Le projet est structuré en plusieurs modules pour une meilleure modularité et maintenabilité :

- **`main_app.py`** : Point d'entrée de l'application, gère l'interface utilisateur principale.
- **`chatbot_page.py`** : Gère les interactions conversationnelles avec le chatbot.
- **`nlp_services.py`** : Contient les services de traitement du langage naturel (analyse de sentiment, extraction d'entités, etc.).
- **`api_services.py`** : Gère les communications avec les APIs externes (météo, attractions, etc.).
- **Gestion des Données** : Utilise **ChromaDB** pour le stockage vectoriel des conversations et des embeddings.

---

## Technologies Utilisées

- **Frameworks et Interfaces** :
  - **Streamlit** : Pour l'interface utilisateur web.
  - **Python** : Langage principal du projet.
  
- **Traitement du Langage Naturel (NLP)** :
  - **TextBlob** : Pour l'analyse de sentiment.
  - **SentenceTransformer** : Pour la génération d'embeddings.
  
- **Base de Données** :
  - **ChromaDB** : Base de données vectorielle pour le stockage des conversations.
  
- **APIs Externes** :
  - **OpenWeatherMap** : Pour les prévisions météorologiques.
  - **FourSquare** : Pour les recommandations d'attractions locales.
  - **Serper** : Pour la recherche d'informations sur le web.
  - **Groq API** : Pour la génération de plans de voyage personnalisés.

---

## Comment Utiliser ce Projet

1. **Cloner le Repository** :
   ```bash
   git clone https://github.com/votre-username/Travel-Partner-Chatbot.git
   cd Travel-Partner-Chatbot
