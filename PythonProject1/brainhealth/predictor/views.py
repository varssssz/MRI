from django.shortcuts import render

# Create your views here.
# predictor/views.py
import os
import joblib
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

MODEL_PATH = os.path.join(settings.BASE_DIR, "prototype_model.pkl")
if not os.path.exists(MODEL_PATH):
    # Let Django import time show an error if model is missing
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run train_model.py first.")

model = joblib.load(MODEL_PATH)

def index(request):
    # Renders templates/index.html
    return render(request, "index.html")

@api_view(['POST'])
def predict(request):
    try:
        age = int(request.data.get('age', 0))
        memory_score = int(request.data.get('memory_score', 0))
        genetic_marker = int(request.data.get('genetic_marker', 0))
    except Exception:
        return Response({"error": "Please provide numeric age, memory_score, genetic_marker"}, status=400)

    pred = model.predict([[age, memory_score, genetic_marker]])[0]
    label = "Yes" if int(pred) == 1 else "No"
    return Response({"prediction": label})
