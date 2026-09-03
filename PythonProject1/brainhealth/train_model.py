# train_model.py
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "patients.csv")
MODEL_PATH = os.path.join(BASE_DIR, "prototype_model.pkl")

df = pd.read_csv(DATA_PATH)
print("Dataset preview:")
print(df.head())

df['early_decline'] = df['early_decline'].map({'Yes': 1, 'No': 0})

X = df[['age', 'memory_score', 'genetic_marker']]
y = df['early_decline']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {acc:.3f}")
print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=['No','Yes']))

joblib.dump(model, MODEL_PATH)
print(f"\nModel saved to: {MODEL_PATH}")
