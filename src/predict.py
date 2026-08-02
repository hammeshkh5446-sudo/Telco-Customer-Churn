import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "models" /
    "churn_prediction_pipeline.pkl"
)


# ============================================================
# LOAD MODEL PIPELINE
# ============================================================

model = joblib.load(MODEL_PATH)

print("=" * 60)
print("CUSTOMER CHURN PREDICTION")
print("=" * 60)


# ============================================================
# NEW CUSTOMER
# ============================================================

customer = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.50,
    "TotalCharges": 846.00
}


# Convert customer data into DataFrame
customer_df = pd.DataFrame([customer])


# ============================================================
# PREDICTION
# ============================================================

prediction = model.predict(
    customer_df
)[0]

probability = model.predict_proba(
    customer_df
)[0][1]


# ============================================================
# RESULT
# ============================================================

print("\nPrediction:")

if prediction == 1:

    print("❌ Customer is likely to CHURN")

else:

    print("✅ Customer is likely to STAY")


print(
    f"Churn Probability: {probability:.2%}"
)

print("=" * 60)
