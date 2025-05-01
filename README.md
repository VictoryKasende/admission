# 🎓 Prédiction d'Admission Étudiante

Ce projet est une application web qui permet de prédire la **probabilité d'admission d'un étudiant** en se basant sur ses données académiques. Il utilise un **modèle de machine learning** déployé via une API pour fournir des prédictions précises en temps réel.

## 🚀 Fonctionnalités

- Formulaire interactif pour saisir les données de l'étudiant (notes, tests, etc.)
- Affichage de la **probabilité d'admission** en pourcentage
- Interface utilisateur responsive et épurée
- Intégration d’un modèle de machine learning entraîné
- API RESTful sécurisée avec CSRF token

## 🧠 Modèle de Machine Learning

Le modèle a été entraîné à l'aide de **Scikit-learn** sur un dataset académique comprenant des variables telles que :
- Résultat au test GRE
- Résultat au TOEFL
- Note moyenne
- Expérience en recherche
- Note de recommandation

## ⚙️ Technologies utilisées

- **Frontend** : HTML, TailwindCSS, JavaScript (vanilla)
- **Backend** : Django, Django REST Framework
- **Machine Learning** : Scikit-learn, joblib
- **API** : Endpoint POST `/api/predict/`

## 📦 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/votre-utilisateur/admission-predictor.git
cd admission
