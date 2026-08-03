#  Telco Customer Churn Prediction

An end-to-end Machine Learning project that predicts customer churn using customer demographics, services, contract information, and billing data.

This project combines Machine Learning, Exploratory Data Analysis, Power BI, and Streamlit into a complete data science workflow.

##  Live Demo

 [Launch the Telco Customer Churn Prediction App](https://telco-customer-churn-odxghtzssr7vln88vckrpz.streamlit.app/)

---

##  Project Overview

Customer churn is a major challenge for subscription-based businesses. Predicting which customers are likely to leave can help organizations take proactive retention measures.

This project develops a machine learning solution to identify customers who are at risk of churn and provides an interactive web application for making predictions.

### Key Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature preparation and encoding
- Multiple classification models
- Model evaluation and comparison
- Machine Learning prediction pipeline
- Interactive Streamlit application
- Power BI business intelligence dashboard
- Visual analysis of customer churn patterns

---

##  Business Problem

The objective is to predict whether a customer is likely to churn based on information such as:

- Customer demographics
- Tenure
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Additional services

The model can help businesses identify high-risk customers and support data-driven customer retention strategies.

---

##  Dataset

The project uses the Telco Customer Churn dataset containing customer demographic, service, contract, and billing information.

### Target Variable

**Churn**

- `Yes` → Customer churned
- `No` → Customer remained

The dataset was cleaned and prepared before model training.

---

##  Data Preprocessing

The preprocessing workflow included:

- Handling missing values
- Converting `TotalCharges` into numeric format
- Removing unnecessary identifiers such as `customerID`
- Encoding categorical variables
- Separating features and target variable
- Splitting data into training and testing sets
- Preparing the data for machine learning models

---

##  Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer behavior and identify patterns associated with churn.

The analysis includes visualizations covering customer churn, contracts, tenure, charges, and feature relationships.

### EDA Visualizations

![EDA Visualization 1](reports/figures/churn_distribution.png)

![EDA Visualization 2](reports/figures/contract_vs_churn.png)

![EDA Visualization 3](reports/figures/correlation_heatmap.png)

![EDA Visualization 4](reports/figures/monthly_charges_vs_churn.png)

![EDA Visualization 5](reports/figures/tenure_vs_churn.png)

> The complete set of visualization figures is available in `reports/figures/`.

---

##  Power BI Dashboard

An interactive Power BI dashboard was created to analyze customer churn from a business intelligence perspective.

The dashboard provides insights into:

- Overall customer churn
- Customer demographics
- Contract types
- Service usage
- Tenure
- Monthly charges
- Customer behavior patterns

### Dashboard Preview

![Telco Customer Churn Power BI Dashboard](reports/Telco_Churn_Dashbaord.PNG)

The complete Power BI dashboard file is available in the `reports/` directory.

---

##  Machine Learning

Multiple classification algorithms were evaluated for the churn prediction task.

### Models Used

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline classification model |
| Decision Tree Classifier | Rule-based classification |
| Random Forest Classifier | Ensemble learning |
| Gradient Boosting Classifier | Boosting-based classification |

The selected model was integrated into a reusable prediction pipeline and used by the Streamlit application.

---

##  Model Evaluation

The models were evaluated using standard classification metrics including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The evaluation process was used to compare model performance and select a suitable model for deployment.

---

##  Streamlit Application

The trained prediction pipeline was integrated into an interactive Streamlit application.

Users can enter customer information and receive a churn prediction through the deployed application.

### Application Features

- Interactive customer input form
- Real-time churn prediction
- Machine learning pipeline integration
- User-friendly interface
- Deployed online using Streamlit

 [Open Live Application](https://telco-customer-churn-odxghtzssr7vln88vckrpz.streamlit.app/)

---

##  Project Structure


Telco-Customer-Churn/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── Telco Customer Churn Dataset
│
├── models/
│   └── churn_prediction_pipeline.pkl
│
├── reports/
│   ├── figures/
│   │   ├── EDA visualization 1
│   │   ├── EDA visualization 2
│   │   ├── EDA visualization 3
│   │   ├── EDA visualization 4
│   │   └── EDA visualization 5
│   │
│   ├── Power BI Dashboard (.pbix)
│   └── Telco_churn_Dashbaord.PNG
│
├── src/
│   ├── data_loading.py
│   ├── eda.py
│   ├── prediction.py
│   └── trainmodel.py
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore

## Tech Stack

Programming
Python
Data Analysis
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Power BI
Machine Learning
Scikit-learn
Logistic Regression
Decision Tree
Random Forest
Gradient Boosting
Deployment
Streamlit
Joblib
Development Tools
Jupyter Notebook
VS Code
Git
GitHub

## Installation

Clone the repository:

git clone https://github.com/hammeshkh5446-sudo/Telco-Customer-Churn.git

Navigate to the project directory:

cd Telco-Customer-Churn

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

##  Project Workflow

Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Preparation
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Best Model / Pipeline
     ↓
Streamlit Deployment
     ↓
Customer Churn Prediction

## Future Improvements

Possible future improvements include:

Hyperparameter tuning
Cross-validation
Advanced feature engineering
Model explainability using SHAP
Improved prediction interface
Automated model monitoring
Cloud-based data pipeline
Customer retention recommendation system

## Author

M. Hammad Shahbaz

Software Engineering Undergraduate | Aspiring Data Scientist

Areas of Interest
Data Science
Machine Learning
Data Analysis
Data Visualization
Business Intelligence

## Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
