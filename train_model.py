import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET LOADED ✅")
print("=" * 60)

print("Original Shape:", df.shape)


# ============================================================
# 3. DATA CLEANING
# ============================================================

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove rows with missing values
df.dropna(inplace=True)

# Remove customer ID
df.drop("customerID", axis=1, inplace=True)

print("After Cleaning:", df.shape)


# ============================================================
# 4. FEATURES & TARGET
# ============================================================

X = df.drop("Churn", axis=1)

y = df["Churn"].map({
    "No": 0,
    "Yes": 1
})


# ============================================================
# 5. IDENTIFY COLUMNS
# ============================================================

categorical_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

numeric_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical Columns:", len(categorical_columns))
print("Numerical Columns:", len(numeric_columns))


# ============================================================
# 6. PREPROCESSING PIPELINE
# ============================================================

numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        )
    ]
)


categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            numeric_columns
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_columns
        )
    ]
)


# ============================================================
# 7. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("TRAIN / TEST SPLIT")
print("=" * 60)

print("Training Shape:", X_train.shape)
print("Testing Shape :", X_test.shape)


# ============================================================
# 8. MODELS
# ============================================================

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=1000
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            random_state=42
        ),

    "Gradient Boosting":
        GradientBoostingClassifier(
            random_state=42
        )
}


# ============================================================
# 9. TRAIN MODELS
# ============================================================

results = {}
trained_pipelines = {}

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)


for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )

    pipeline.fit(
        X_train,
        y_train
    )

    y_pred = pipeline.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    results[name] = accuracy

    trained_pipelines[name] = pipeline

    print(
        f"{name:<22} : {accuracy:.4f}"
    )


# ============================================================
# 10. BEST MODEL
# ============================================================

best_model_name = max(
    results,
    key=results.get
)

best_pipeline = trained_pipelines[
    best_model_name
]

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(
    f"Model    : {best_model_name}"
)

print(
    f"Accuracy : {results[best_model_name]:.4f}"
)


# ============================================================
# 11. EVALUATION
# ============================================================

y_pred = best_pipeline.predict(
    X_test
)

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nClassification Report")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred
    )
)


# Confusion Matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot(
    cmap="Blues"
)

plt.title(
    f"Confusion Matrix - {best_model_name}"
)

plt.tight_layout()

plt.show()


# ============================================================
# 12. SAVE COMPLETE PIPELINE
# ============================================================

MODEL_PATH = (
    MODEL_DIR /
    "churn_prediction_pipeline.pkl"
)

joblib.dump(
    best_pipeline,
    MODEL_PATH
)

print("\n" + "=" * 60)
print("MODEL PIPELINE SAVED ✅")
print("=" * 60)

print(
    f"Saved at: {MODEL_PATH}"
)

print("=" * 60)