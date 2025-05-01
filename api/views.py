

import joblib
import json
import pandas as pd
import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Chargement du modèle et du scaler
MODELE_PATH = os.path.join(settings.BASE_DIR, 'modele_logistique.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'scaler.pkl')
COLONNES_PATH = os.path.join(settings.BASE_DIR, 'colonnes_modele.json')

model = joblib.load(MODELE_PATH)
scaler = joblib.load(SCALER_PATH)
with open(COLONNES_PATH, 'r') as f:
    colonnes_attendues = json.load(f)

class PredictionAdmission(APIView):
    def post(self, request):
        try:
            df = pd.DataFrame([request.data])
            df = pd.get_dummies(df)

            for col in colonnes_attendues:
                if col not in df.columns:
                    df[col] = 0

            df = df[colonnes_attendues]  # ordre identique

            X_scaled = scaler.transform(df)
            prediction = int(model.predict(X_scaled)[0])
            proba_round = round(float(model.predict_proba(X_scaled)[0][1]), 4) * 100
            proba = round(proba_round, 0)
            return Response({
                'prediction': prediction,
                'probabilite_admission': proba
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'predict.html')