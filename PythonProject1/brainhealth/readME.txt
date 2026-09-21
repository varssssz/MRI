# MRI — Internal Team Development Documentation

> **⚠️ This README is for the development team.**
>
> This document explains the current state of the project, how the code works, how to run it, where everything is located, and how we should develop it going forward.
>
> **Read the "CURRENT STATE" section before modifying anything.**

---

# 1. Project Overview

## What are we building?

This project is intended to become an **AI-assisted brain/MRI analysis platform**.

The current codebase is the **initial prototype**.

Right now, the project does **not process MRI images yet**.

The current implementation is a small machine-learning system that takes structured patient information:

```text
Age
Memory Score
Genetic Marker
```

and uses a trained machine-learning model to predict:

```text
Early Cognitive Decline
    ↓
Yes / No
```

The current web application is built with:

```text
Frontend
    ↓
HTML + JavaScript

Backend
    ↓
Django + Django REST Framework

Machine Learning
    ↓
scikit-learn Decision Tree

Data
    ↓
CSV

Model Storage
    ↓
Joblib (.pkl)

Database
    ↓
SQLite
```

---

# 2. 🚨 CURRENT STATE — READ THIS FIRST

## What currently works

The current project contains:

* Django project
* Django `predictor` application
* HTML frontend
* JavaScript frontend logic
* Patient CSV dataset
* Machine-learning training script
* Decision Tree model
* Model evaluation
* Serialized `.pkl` model
* Prediction API
* SQLite database
* Django development server

---

## What does NOT exist yet

The current project does **not** have:

* MRI image upload
* MRI image preprocessing
* DICOM processing
* NIfTI processing
* MRI segmentation
* MRI classification
* CNN
* 3D CNN
* Vision Transformer
* MRI visualization
* Grad-CAM
* Explainable AI
* Patient authentication
* User accounts
* Patient history
* Production deployment
* Production database
* Proper ML experiment tracking

### Do not document these as implemented features until we actually implement them.

The project name is `MRI`, but the current implementation is a **structured-data cognitive-decline prototype**.

---

# 3. Current Architecture

The current system is:

```text
                         USER
                          │
                          ▼
                 ┌─────────────────┐
                 │  HTML Frontend  │
                 └────────┬────────┘
                          │
                          │ JSON
                          ▼
                 ┌─────────────────┐
                 │   Django API    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Input Validation│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Decision Tree   │
                 │      Model      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Prediction   │
                 │     Yes / No    │
                 └────────┬────────┘
                          │
                          ▼
                    JSON Response
                          │
                          ▼
                 ┌─────────────────┐
                 │  HTML Frontend  │
                 └─────────────────┘
```

---

# 4. Repository Structure

Current repository:

```text
MRI/
│
└── PythonProject1/
    │
    └── brainhealth/
        │
        ├── brainhealth/
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── asgi.py
        │   └── wsgi.py
        │
        ├── predictor/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   └── migrations/
        │
        ├── templates/
        │   └── index.html
        │
        ├── patients.csv
        ├── prototype_model.pkl
        ├── train_model.py
        ├── manage.py
        └── db.sqlite3
```

---

# 5. What Each Directory Means

## `brainhealth/`

This is the **Django project configuration**.

It controls things such as:

* Django settings
* URL routing
* WSGI
* ASGI
* Installed applications
* Database configuration
* Middleware

---

## `predictor/`

This is the **main application**.

It contains the actual prediction functionality.

Important files:

```text
views.py
urls.py
models.py
apps.py
admin.py
tests.py
```

---

## `templates/`

Contains the HTML frontend.

Current file:

```text
templates/index.html
```

---

# 6. Important Files

## `manage.py`

Django's command-line entry point.

Used for:

```bash
python manage.py runserver
```

and other Django management commands.

Do not put application logic here.

---

# 7. `brainhealth/settings.py`

This is the main Django configuration file.

It controls:

```text
Installed applications
Middleware
Database
Templates
Static files
Secret key
Debug mode
Allowed hosts
CORS
```

The current project uses:

```text
Django
Django REST Framework
CORS Headers
predictor
SQLite
```

---

# 8. `brainhealth/urls.py`

This is the **project-level URL router**.

Think of it as:

```text
Internet request
      ↓
brainhealth/urls.py
      ↓
Which Django application should handle this?
```

The `predictor` application's routes are connected here.

---

# 9. `predictor/urls.py`

This contains the application-level routes.

Current important routes:

```text
/
```

and:

```text
/predict/
```

Conceptually:

```text
GET /
   ↓
Display frontend

POST /predict/
   ↓
Run machine-learning prediction
```

---

# 10. `predictor/views.py`

This is one of the most important files.

It contains the backend logic for:

1. Loading the trained model
2. Rendering the homepage
3. Receiving prediction requests
4. Reading request data
5. Converting values
6. Calling the ML model
7. Returning the prediction

The backend essentially performs:

```text
HTTP Request
     ↓
Read JSON
     ↓
Extract:
  age
  memory_score
  genetic_marker
     ↓
Convert to integers
     ↓
ML model
     ↓
Prediction
     ↓
Convert 0/1
     ↓
Yes/No
     ↓
JSON response
```

---

# 11. `predictor/models.py`

Currently this file does not contain a custom patient model.

It is essentially the standard Django models file.

This means:

**Do not assume patient data is currently stored in SQLite through Django models.**

The machine-learning dataset currently comes from:

```text
patients.csv
```

If we later build patient accounts/history, this file will become important.

---

# 12. `predictor/admin.py`

Standard Django admin configuration.

Currently there are no major custom admin features.

---

# 13. `predictor/apps.py`

Contains the Django application configuration.

Application name:

```text
predictor
```

---

# 14. `predictor/tests.py`

This is where automated Django tests should eventually go.

Currently, the project does not have a comprehensive test suite.

Future tests should cover:

```text
API
Input validation
Model loading
Prediction
Frontend/backend integration
```

---

# 15. `templates/index.html`

This is currently the main frontend.

It contains:

```text
Age input
Memory score input
Genetic marker selection
Predict button
Prediction output
```

The page uses JavaScript to communicate with Django.

---

# 16. Frontend → Backend Flow

When the user clicks **Predict**:

```text
User enters:

Age = 65
Memory Score = 72
Genetic Marker = 1
```

JavaScript collects the values.

It creates an object similar to:

```json
{
    "age": 65,
    "memory_score": 72,
    "genetic_marker": 1
}
```

Then sends:

```text
POST /predict/
```

with JSON.

---

# 17. API

## Endpoint

```text
POST /predict/
```

### Input

```json
{
    "age": 65,
    "memory_score": 72,
    "genetic_marker": 1
}
```

### Output

```json
{
    "prediction": "Yes"
}
```

or:

```json
{
    "prediction": "No"
}
```

---

# 18. API Input Fields

| Field            | Type    | Meaning                 |
| ---------------- | ------- | ----------------------- |
| `age`            | Integer | Patient age             |
| `memory_score`   | Integer | Memory assessment score |
| `genetic_marker` | Integer | Binary genetic marker   |

The current genetic marker representation is:

```text
0 = No
1 = Yes
```

---

# 19. API Error Handling

If the backend receives invalid numeric input:

```json
{
    "age": "hello"
}
```

the request should fail instead of passing invalid data into the model.

The current API returns an HTTP `400` response with an error message for invalid numeric inputs.

---

# 20. Machine Learning Pipeline

The ML code lives in:

```text
train_model.py
```

The pipeline is:

```text
patients.csv
     │
     ▼
Pandas
     │
     ▼
Preprocessing
     │
     ▼
Feature Selection
     │
     ▼
Train/Test Split
     │
     ▼
Decision Tree
     │
     ▼
Evaluation
     │
     ▼
Joblib
     │
     ▼
prototype_model.pkl
```

---

# 21. Dataset

Current dataset:

```text
patients.csv
```

Expected fields:

```text
patient_id
age
memory_score
genetic_marker
early_decline
```

---

# 22. Dataset Meaning

## `patient_id`

Identifier for the patient.

This should generally **not** be used as an ML feature.

---

## `age`

Patient age.

Used as a model feature.

---

## `memory_score`

Numerical memory assessment score.

Used as a model feature.

---

## `genetic_marker`

Binary feature:

```text
0
1
```

Used as a model feature.

---

## `early_decline`

This is the **target variable**.

Current encoding:

```text
Yes → 1
No  → 0
```

---

# 23. ML Features

The model currently uses:

```python
X = df[
    [
        'age',
        'memory_score',
        'genetic_marker'
    ]
]
```

Therefore:

```text
X =
[
    age,
    memory_score,
    genetic_marker
]
```

---

# 24. ML Target

The target is:

```python
y = df['early_decline']
```

Before training:

```text
Yes → 1
No  → 0
```

---

# 25. Train/Test Split

The current model uses:

```text
80% Training
20% Testing
```

with:

```python
random_state=42
```

The `random_state` is important because it makes the split reproducible.

Do not randomly remove it unless we intentionally want different splits.

---

# 26. Current ML Model

The project currently uses:

```text
DecisionTreeClassifier
```

from:

```text
scikit-learn
```

The basic training process is:

```text
Create Decision Tree
       ↓
X_train + y_train
       ↓
model.fit()
       ↓
Trained model
```

---

# 27. Model Evaluation

The current training script calculates:

```text
Accuracy
Classification Report
```

The classification report contains:

```text
Precision
Recall
F1-score
Support
```

### Important

Because the current dataset is small, **do not treat the reported accuracy as clinically meaningful**.

It is currently only a prototype metric.

---

# 28. Model File

After training:

```text
prototype_model.pkl
```

is generated.

This is the trained Decision Tree.

The Django backend loads this file to perform predictions.

---

# 29. DO NOT Manually Edit `.pkl`

Never open:

```text
prototype_model.pkl
```

and attempt to modify it manually.

If the model needs to change:

```text
Modify training code
       ↓
Modify dataset if required
       ↓
Retrain
       ↓
Generate new .pkl
```

---

# 30. Retraining the Model

If we change:

* Dataset
* Features
* Target
* Algorithm
* Hyperparameters

we must retrain.

Run:

```bash
python train_model.py
```

This regenerates:

```text
prototype_model.pkl
```

---

# 31. Changing ML Features

Suppose we want to add:

```text
sleep_score
```

We need to modify the training pipeline.

For example:

```python
X = df[
    [
        'age',
        'memory_score',
        'genetic_marker',
        'sleep_score'
    ]
]
```

But that is **not enough**.

We must also update:

### Dataset

Add:

```text
sleep_score
```

### API

Accept:

```json
{
    "age": 65,
    "memory_score": 72,
    "genetic_marker": 1,
    "sleep_score": 80
}
```

### Frontend

Add a new input.

### Backend

Extract the new value.

### Model

Retrain the model.

### Important

The **feature order must remain identical between training and prediction**.

---

# 32. Changing the ML Algorithm

If we want to replace Decision Tree:

```text
Current:

DecisionTreeClassifier
```

with:

```text
RandomForestClassifier
```

the process should be:

```text
1. Modify train_model.py
2. Train new model
3. Evaluate new model
4. Save model
5. Test Django prediction
6. Verify frontend
```

The API does not necessarily need to change if the input/output format remains the same.

This is one advantage of keeping the ML model behind the API.

---

# 33. Why Model and Backend Are Separated

Current architecture:

```text
                Django
                  │
                  │
             API request
                  │
                  ▼
            ML inference
                  │
                  ▼
             API response
```

This means the model can eventually change from:

```text
Decision Tree
```

to:

```text
Random Forest
```

or:

```text
XGBoost
```

or eventually:

```text
CNN / 3D CNN
```

without completely rebuilding the frontend.

---

# 34. SQLite

Current database:

```text
db.sqlite3
```

Django uses SQLite.

At the moment, the ML training data is still stored in:

```text
patients.csv
```

rather than through a custom Django patient model.

---

# 35. Future Database Architecture

Eventually, we may want:

```text
Patient
   │
   ├── Personal Information
   ├── Cognitive Assessments
   ├── MRI Scans
   ├── Predictions
   └── Prediction History
```

Possible future tables:

```text
Patient
Assessment
MRI_Scan
Prediction
ModelVersion
```

---

# 36. Current Installation

Clone the repository:

```bash
git clone https://github.com/varssssz/MRI.git
```

Enter the repository:

```bash
cd MRI
```

Then:

```bash
cd PythonProject1/brainhealth
```

---

# 37. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 38. Install Dependencies

Current project dependencies include the packages required for:

```text
Django
Django REST Framework
Pandas
scikit-learn
Joblib
django-cors-headers
```

Install them with:

```bash
pip install django djangorestframework pandas scikit-learn joblib django-cors-headers
```

---

# 39. Train the Model

From:

```text
PythonProject1/brainhealth
```

run:

```bash
python train_model.py
```

Make sure:

```text
patients.csv
```

exists before doing this.

---

# 40. Start Django

Run:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# 41. Normal Development Workflow

Every developer should generally follow:

```text
Pull latest code
      ↓
Create/activate virtual environment
      ↓
Install/update dependencies
      ↓
Run application
      ↓
Make changes
      ↓
Test locally
      ↓
Commit
      ↓
Push branch
      ↓
Pull Request
      ↓
Review
      ↓
Merge
```

---

# 42. Git Workflow

## Before starting work

Always pull:

```bash
git pull
```

Check status:

```bash
git status
```

---

# 43. Branches

Do not develop major features directly on `main`.

Use feature branches.

Example:

```bash
git checkout -b feature/mri-upload
```

or:

```bash
git checkout -b feature/model-improvement
```

or:

```bash
git checkout -b feature/frontend-redesign
```

---

# 44. Commit Messages

Use meaningful commit messages.

Good:

```text
Add prediction API validation
```

```text
Add MRI upload interface
```

```text
Improve model preprocessing
```

```text
Fix prediction endpoint
```

Bad:

```text
stuff
```

```text
changes
```

```text
final
```

```text
finalfinal
```

---

# 45. Before Pushing

Run:

```bash
git status
```

Check what changed.

Then:

```bash
git diff
```

Make sure you are not accidentally committing:

```text
Passwords
API keys
.env
Virtual environments
Large datasets
Temporary files
IDE files
```

Then:

```bash
git add .
git commit -m "Describe the change"
git push
```

---

# 46. ⚠️ Important Git Rule

Never commit secrets.

Especially:

```text
SECRET_KEY
API keys
Passwords
Database credentials
Tokens
```

If credentials are accidentally committed, **deleting them in a later commit is not sufficient** because they remain in Git history.

---

# 47. `.gitignore`

The project should eventually have a proper `.gitignore`.

At minimum:

```text
venv/
.venv/
__pycache__/
*.pyc
.env
*.sqlite3
.idea/
.vscode/
.DS_Store
```

Depending on how we handle ML artifacts, we may also choose whether large datasets and model files belong in Git.

---

# 48. ⚠️ Current Security Issue

The current Django configuration is development-oriented.

Before production:

```text
DEBUG = False
```

and:

```text
SECRET_KEY
```

should be moved to environment variables.

Do not deploy the current development configuration as-is.

---

# 49. Troubleshooting

## Problem: `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named 'django'
```

Fix:

```bash
pip install django
```

or install all project dependencies.

---

## Problem: Model not found

If Django cannot find:

```text
prototype_model.pkl
```

run:

```bash
python train_model.py
```

---

## Problem: CSV not found

Make sure:

```text
patients.csv
```

is in the location expected by `train_model.py`.

Run the training command from:

```text
PythonProject1/brainhealth
```

---

## Problem: Server does not start

Run:

```bash
python manage.py check
```

This asks Django to check for configuration problems.

Then:

```bash
python manage.py runserver
```

---

## Problem: Prediction API returns 400

Check that the request contains:

```text
age
memory_score
genetic_marker
```

and that the values are numeric.

---

# 50. Common Development Mistake

Do not change the frontend input names without changing the backend.

For example, if frontend changes:

```text
memory_score
```

to:

```text
memoryScore
```

the backend will no longer receive the expected field.

Frontend and backend must agree on the API contract.

---

# 51. API Contract

Current contract:

```text
POST /predict/
```

Input:

```json
{
    "age": number,
    "memory_score": number,
    "genetic_marker": number
}
```

Output:

```json
{
    "prediction": "Yes" | "No"
}
```

If we change this structure, update:

```text
Frontend
Backend
Tests
Documentation
```

---

# 52. Future MRI Integration

This is where the project will become significantly more advanced.

The intended future pipeline is:

```text
MRI Image
    │
    ▼
Upload
    │
    ▼
DICOM / NIfTI
    │
    ▼
Preprocessing
    │
    ├── Normalization
    ├── Resampling
    ├── Registration
    ├── Skull Stripping
    └── Noise Reduction
    │
    ▼
MRI Model
    │
    ├── CNN
    ├── 3D CNN
    └── Vision Transformer
    │
    ▼
MRI Features
    │
    └─────────────┐
                  │
                  ▼
          Multimodal Model
                  ▲
                  │
        ┌─────────┴─────────┐
        │                   │
Clinical Data        Cognitive Scores
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
             Prediction
```

Actual MRI-processing repositories typically introduce additional preprocessing and model pipelines—for example DICOM/NIfTI handling, registration, skull stripping, resampling, and 3D models.

Those components are **future work for this project**, not current functionality.

---

# 53. Proposed Future MRI Structure

When MRI functionality is added, don't dump everything into `views.py`.

Instead, separate responsibilities:

```text
mri/
│
├── preprocessing/
│   ├── dicom.py
│   ├── nifti.py
│   ├── normalization.py
│   └── registration.py
│
├── models/
│   ├── cnn.py
│   └── inference.py
│
├── visualization/
│   └── slices.py
│
└── utils/
```

Django should handle:

```text
HTTP
Upload
Authentication
API
Response
```

while the ML/MRI layer handles:

```text
Image
Preprocessing
Inference
Analysis
```

---

# 54. Proposed Future ML Architecture

Eventually:

```text
                  MRI
                   │
                   ▼
             MRI Encoder
                   │
                   ▼
              MRI Vector
                   │
                   │
                   ├─────────────┐
                   │             │
                   ▼             ▼
             Clinical Data   Cognitive Data
                   │             │
                   └──────┬──────┘
                          ▼
                   Feature Fusion
                          │
                          ▼
                  Prediction Model
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            Risk       Probability  Explanation
```

---

# 55. Explainability

A future model should ideally not return only:

```text
Yes
```

It should eventually provide information such as:

```text
Prediction:
Elevated Risk

Probability:
87%

Important factors:
- Memory score
- Age
- MRI-derived features
```

For image models, possible explainability tools include:

```text
Grad-CAM
Saliency maps
Attention maps
```

---

# 56. Current Limitations

The team should be aware of these limitations.

## Dataset

Current dataset is small.

Therefore:

```text
High accuracy ≠ clinically reliable model
```

---

## Features

Only three predictive features are currently used.

Real-world cognitive assessment would require significantly more information.

---

## Model

Only one basic classifier is currently implemented.

There is no model comparison.

---

## Validation

Current validation is based on a simple train/test split.

There is no:

```text
Cross-validation
External validation
Prospective validation
```

---

## MRI

MRI analysis is not implemented yet.

---

# 57. Medical/Research Warning

This project should currently be treated as:

```text
Educational / Research Prototype
```

not:

```text
Clinical Diagnostic System
```

The model must not be used to make actual medical decisions.

---

# 58. Development Priorities

Recommended order:

## Priority 1 — Clean the foundation

```text
[ ] requirements.txt
[ ] .gitignore
[ ] Environment variables
[ ] Clean project structure
[ ] Basic automated tests
```

---

## Priority 2 — Improve ML

```text
[ ] Better dataset
[ ] Better preprocessing
[ ] Cross-validation
[ ] Multiple models
[ ] Hyperparameter tuning
[ ] Proper evaluation
```

---

## Priority 3 — Improve Backend

```text
[ ] Better API validation
[ ] API documentation
[ ] Model versioning
[ ] Prediction logging
[ ] Authentication
```

---

## Priority 4 — Build MRI Pipeline

```text
[ ] MRI upload
[ ] DICOM support
[ ] NIfTI support
[ ] Preprocessing
[ ] MRI dataset
[ ] CNN baseline
[ ] Evaluation
```

---

## Priority 5 — Multimodal AI

```text
[ ] MRI features
[ ] Clinical features
[ ] Cognitive features
[ ] Feature fusion
[ ] Explainability
```

---

# 59. Definition of "Done"

A feature is **not considered finished** just because the code works locally.

For a feature to be considered complete:

```text
Code
  +
Testing
  +
Documentation
  +
Git commit
  +
Team review
```

Example:

```text
MRI upload

❌ Code works on developer's laptop

Not done.

✅ Upload works
✅ Invalid files rejected
✅ Tests added
✅ API documented
✅ Error handling added
✅ Other team members can run it
✅ Changes committed
```

---

# 60. Team Rule — Don't Break Existing Components

Before changing an existing component, understand its dependencies.

Example:

```text
patients.csv
      ↓
train_model.py
      ↓
prototype_model.pkl
      ↓
views.py
      ↓
/predict/
      ↓
index.html
```

Changing one component can affect everything downstream.

---

# 61. If You Change the Dataset

You may need to update:

```text
patients.csv
train_model.py
views.py
index.html
tests.py
```

and retrain:

```bash
python train_model.py
```

---

# 62. If You Change the API

Update:

```text
views.py
urls.py
index.html
tests.py
README.md
```

---

# 63. If You Change the Model

Update:

```text
train_model.py
prototype_model.pkl
tests.py
README.md
```

and verify the API still works.

---

# 64. If You Change the Frontend

Usually modify:

```text
templates/index.html
```

But if you change input names or API requests, also update:

```text
views.py
```

---

# 65. If You Add MRI

Do **not** simply put all MRI code inside:

```text
views.py
```

Keep:

```text
Django
```

separate from:

```text
MRI processing
```

and:

```text
Machine learning
```

This will save us a lot of problems later.

---

# 66. Recommended Long-Term Architecture

```text
MRI/
│
├── backend/
│   │
│   ├── brainhealth/
│   │
│   ├── predictor/
│   │
│   └── manage.py
│
├── ml/
│   │
│   ├── data/
│   ├── preprocessing/
│   ├── training/
│   ├── evaluation/
│   ├── inference/
│   └── models/
│
├── mri/
│   │
│   ├── preprocessing/
│   ├── segmentation/
│   ├── registration/
│   └── visualization/
│
├── frontend/
│
├── tests/
│
├── docs/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 67. Quick Start — Team Cheat Sheet

For someone who has just cloned the project:

```bash
git clone https://github.com/varssssz/MRI.git

cd MRI

cd PythonProject1/brainhealth

python -m venv venv

venv\Scripts\activate

pip install django djangorestframework pandas scikit-learn joblib django-cors-headers

python train_model.py

python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# 68. Quick ML Cheat Sheet

### Train

```bash
python train_model.py
```

### Model

```text
prototype_model.pkl
```

### Dataset

```text
patients.csv
```

### Features

```text
age
memory_score
genetic_marker
```

### Target

```text
early_decline
```

### Algorithm

```text
Decision Tree
```

---

# 69. Quick API Cheat Sheet

### Endpoint

```text
POST /predict/
```

### Input

```json
{
    "age": 65,
    "memory_score": 72,
    "genetic_marker": 1
}
```

### Output

```json
{
    "prediction": "Yes"
}
```

---

# 70. Quick Git Cheat Sheet

### Check status

```bash
git status
```

### Pull

```bash
git pull
```

### Create branch

```bash
git checkout -b feature/name
```

### Stage

```bash
git add .
```

### Commit

```bash
git commit -m "Describe change"
```

### Push

```bash
git push -u origin feature/name
```

---

# 71. Final Project State

## CURRENT

```text
                    STRUCTURED DATA
                          │
                          ▼
                     Pandas
                          │
                          ▼
                 Decision Tree ML
                          │
                          ▼
                  prototype_model.pkl
                          │
                          ▼
                       Django
                          │
                          ▼
                     REST API
                          │
                          ▼
                  HTML + JavaScript
                          │
                          ▼
                    Prediction
```

---

# 72. TARGET

Eventually:

```text
                         MRI
                          │
                          ▼
                  MRI Preprocessing
                          │
                          ▼
                     MRI Model
                          │
                          ▼
                    MRI Features
                          │
                          │
Clinical Data ────────────┤
                          │
Cognitive Data ───────────┤
                          │
Genetic Data ─────────────┤
                          │
                          ▼
                  Multimodal AI
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Risk Score   Explanation   History
             │            │            │
             └────────────┼────────────┘
                          ▼
                    Django API
                          │
                          ▼
                    Web Dashboard
```

---

# 73. 🚧 Current TODO

The following list is the team's working backlog.

```text
[ ] Clean project structure
[ ] Add requirements.txt
[ ] Add .gitignore
[ ] Move Django secret to environment variable
[ ] Add automated tests
[ ] Improve dataset
[ ] Add proper validation
[ ] Compare ML models
[ ] Add probability output
[ ] Add explainability
[ ] Add patient database
[ ] Add prediction history
[ ] Add MRI upload
[ ] Add MRI preprocessing
[ ] Add MRI dataset
[ ] Train first MRI model
[ ] Integrate MRI model with Django
[ ] Build dashboard
[ ] Add authentication
[ ] Add model versioning
[ ] Deploy
```

---

# 74. One Rule To Remember

Before making a major change, ask:

> **"What part of the pipeline does this change affect?"**

The current pipeline is:

```text
DATA
 ↓
TRAINING
 ↓
MODEL
 ↓
BACKEND
 ↓
API
 ↓
FRONTEND
```

If you change something upstream, check everything downstream.

---

# 75. Project Philosophy

The goal is **not** to make everything work as quickly as possible.

The goal is to build the project in a way that allows us to progressively move from:

```text
Simple prototype
```

to:

```text
Reliable ML system
```

to:

```text
MRI analysis pipeline
```

to:

```text
Multimodal brain-health platform
```

without having to rewrite the entire project every time.

---

# 76. TL;DR

If you're new to the project, understand these six things first:

```text
1. patients.csv
       ↓
2. train_model.py
       ↓
3. prototype_model.pkl
       ↓
4. predictor/views.py
       ↓
5. /predict/
       ↓
6. templates/index.html
```

That is the **entire current application pipeline**.

Everything else is supporting infrastructure.

---

# 🧠 END OF INTERNAL DOCUMENTATION

**Current project:** Brain-health / cognitive-decline ML prototype

**Current ML:** Decision Tree

**Current backend:** Django

**Current API:** `/predict/`

**Current frontend:** HTML + JavaScript

**Current dataset:** `patients.csv`

**Current model:** `prototype_model.pkl`

**MRI processing:** Not implemented yet

**Long-term goal:** Multimodal MRI + clinical-data brain-health analysis
