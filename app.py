import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="ChurnIQ | Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PROFESSIONAL UI THEME
# ============================================================
st.markdown(
    """
    <style>
    :root {
        --primary: #5B5FEF;
        --secondary: #8B5CF6;
        --accent: #14B8A6;
        --danger: #EF4444;
        --warning: #F59E0B;
        --success: #10B981;
        --dark: #172033;
        --muted: #64748B;
        --surface: rgba(255, 255, 255, 0.92);
        --border: rgba(91, 95, 239, 0.14);
    }

    html, body, [class*="css"] {
        font-family: Inter, ui-sans-serif, system-ui, -apple-system,
                     BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 7% 8%, rgba(59, 130, 246, 0.28), transparent 24%),
            radial-gradient(circle at 92% 8%, rgba(168, 85, 247, 0.28), transparent 25%),
            radial-gradient(circle at 85% 88%, rgba(20, 184, 166, 0.22), transparent 24%),
            radial-gradient(circle at 18% 88%, rgba(236, 72, 153, 0.15), transparent 22%),
            linear-gradient(135deg, #F8FBFF 0%, #EEF2FF 35%, #F5F3FF 68%, #ECFEFF 100%);
        background-attachment: fixed;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
            linear-gradient(rgba(255,255,255,0.18) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.18) 1px, transparent 1px);
        background-size: 44px 44px;
        mask-image: linear-gradient(to bottom, rgba(0,0,0,0.35), transparent 78%);
    }

    .block-container {
        max-width: 1280px;
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 38px 42px;
        border-radius: 28px;
        background:
            radial-gradient(circle at 82% 20%, rgba(255,255,255,0.17), transparent 24%),
            linear-gradient(120deg, #0F172A 0%, #312E81 33%, #4F46E5 62%, #9333EA 100%);
        border: 1px solid rgba(255,255,255,0.14);
        box-shadow:
            0 30px 70px rgba(49, 46, 129, 0.30),
            inset 0 1px 0 rgba(255,255,255,0.14);
        margin-bottom: 28px;
    }

    .hero::before,
    .hero::after {
        content: "";
        position: absolute;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
    }

    .hero::before {
        width: 220px;
        height: 220px;
        top: -100px;
        right: -40px;
    }

    .hero::after {
        width: 145px;
        height: 145px;
        bottom: -80px;
        right: 170px;
    }

    .hero-kicker {
        color: #E0E7FF;
        font-size: clamp(20px, 2.5vw, 27px);
        line-height: 1.2;
        font-weight: 850;
        letter-spacing: 0.02em;
        margin-bottom: 12px;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: clamp(34px, 5vw, 50px);
        line-height: 1.05;
        font-weight: 900;
        margin: 0;
    }

    .hero-subtitle {
        max-width: 760px;
        color: #E0E7FF;
        font-size: 17px;
        line-height: 1.7;
        margin-top: 12px;
    }

    .hero-tags {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 20px;
    }

    .hero-tag {
        padding: 8px 13px;
        border-radius: 999px;
        color: #FFFFFF;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.16);
        font-size: 12px;
        font-weight: 700;
    }

    .section-heading {
        margin-top: 20px;
        margin-bottom: 14px;
    }

    .section-title {
        color: var(--dark);
        font-size: 22px;
        font-weight: 900;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: var(--muted);
        font-size: 14px;
    }

    div[data-testid="stForm"] {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.96), rgba(248,250,252,0.90));
        border: 1px solid rgba(99,102,241,0.16);
        border-radius: 26px;
        padding: 26px 26px 14px 26px;
        box-shadow:
            0 24px 55px rgba(49,46,129,0.10),
            inset 0 1px 0 rgba(255,255,255,0.90);
        backdrop-filter: blur(18px);
    }

    label, .stSelectbox label, .stNumberInput label {
        color: #334155 !important;
        font-weight: 750 !important;
        font-size: 14px !important;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        min-height: 46px;
        border-radius: 12px !important;
        border: 1px solid #D8DEEF !important;
        background: rgba(255,255,255,0.96) !important;
        box-shadow: none !important;
    }

    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="input"] > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(91, 95, 239, 0.12) !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        min-height: 56px;
        border: none !important;
        border-radius: 15px !important;
        background: linear-gradient(90deg, #4F46E5, #7C3AED, #8B5CF6) !important;
        color: #FFFFFF !important;
        font-size: 16px !important;
        font-weight: 900 !important;
        letter-spacing: 0.02em;
        box-shadow: 0 14px 30px rgba(79, 70, 229, 0.26);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 34px rgba(79, 70, 229, 0.34);
    }

    .result-card {
        padding: 30px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 18px 44px rgba(30, 41, 59, 0.10);
        margin: 18px 0 22px 0;
    }

    .result-danger {
        background: linear-gradient(135deg, #FFF1F2, #FEE2E2);
        border: 1px solid #FECACA;
    }

    .result-safe {
        background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
        border: 1px solid #A7F3D0;
    }

    .result-label {
        color: #475569;
        font-size: 13px;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .result-title {
        color: var(--dark);
        font-size: 28px;
        font-weight: 950;
        margin-top: 8px;
    }

    .result-score {
        color: var(--dark);
        font-size: clamp(44px, 7vw, 66px);
        line-height: 1;
        font-weight: 950;
        margin: 12px 0;
    }

    .result-note {
        color: var(--muted);
        font-size: 14px;
    }

    div[data-testid="stMetric"] {
        height: 100%;
        min-height: 118px;
        background:
            linear-gradient(145deg, rgba(255,255,255,0.98), rgba(246,248,255,0.94));
        border: 1px solid rgba(99,102,241,0.16);
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 12px 30px rgba(30,41,59,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #6366F1 !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricValue"] {
        color: var(--dark) !important;
        font-weight: 900 !important;
        font-size: clamp(20px, 2vw, 30px) !important;
        line-height: 1.15 !important;
        white-space: normal !important;
        overflow-wrap: anywhere !important;
        word-break: normal !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 16px !important;
        border-width: 1px !important;
    }

    div[data-testid="stProgress"] > div {
        height: 14px;
        border-radius: 999px;
        overflow: hidden;
        background: #E2E8F0;
    }

    div[data-testid="stProgress"] > div > div > div {
        background: linear-gradient(90deg, #10B981 0%, #F59E0B 52%, #EF4444 100%);
    }

    .info-strip {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-bottom: 22px;
    }

    .info-chip {
        background:
            linear-gradient(145deg, rgba(255,255,255,0.92), rgba(245,247,255,0.82));
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 18px;
        padding: 16px 17px;
        color: #475569;
        font-size: 13px;
        box-shadow: 0 14px 30px rgba(49,46,129,0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .info-chip strong {
        display: block;
        color: var(--dark);
        font-size: 15px;
        margin-bottom: 3px;
    }

    .info-chip:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 38px rgba(49,46,129,0.13);
    }

    .footer-box {
        text-align: center;
        margin-top: 30px;
        padding: 22px;
        color: #64748B;
        font-size: 13px;
    }

    .footer-box strong {
        color: #3730A3;
    }

    @media (max-width: 800px) {
        .hero {
            padding: 28px 24px;
            border-radius: 22px;
        }

        .info-strip {
            grid-template-columns: 1fr;
        }

        div[data-testid="stForm"] {
            padding: 18px 16px 8px 16px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MODEL LOADING
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "churn_prediction_pipeline.pkl"


@st.cache_resource(show_spinner=False)
def load_model(model_path: Path):
    return joblib.load(model_path)


try:
    model = load_model(MODEL_PATH)
except FileNotFoundError:
    st.error(
        "Model file was not found. Check this path:\n\n"
        f"`{MODEL_PATH}`"
    )
    st.stop()
except Exception:
    import traceback
    st.error("The model could not be loaded.")
    st.code(traceback.format_exc())
    st.stop()


# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-kicker">Customer Churn Prediction</div>
        <h1 class="hero-title">ChurnIQ</h1>
        <div class="hero-subtitle">
            Analyze customer behavior, estimate churn probability, and identify retention risk with a clean machine learning dashboard.
        </div>
        <div class="hero-tags">
            <span class="hero-tag">Machine Learning</span>
            <span class="hero-tag">Risk Analytics</span>
            <span class="hero-tag">Business Intelligence</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="info-strip">
        <div class="info-chip">
            <strong>Single Customer Analysis</strong>
            Enter customer account information.
        </div>
        <div class="info-chip">
            <strong>Instant Prediction</strong>
            Generate an instant churn prediction.
        </div>
        <div class="info-chip">
            <strong>Clear Risk Level</strong>
            View a clear low, medium, or high risk level.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INPUT FORM
# ============================================================
with st.form("customer_churn_form"):
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Customer Profile</div>
            <div class="section-subtitle">
                Enter demographic and account information.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox(
            "Senior Citizen",
            [0, 1],
            format_func=lambda value: "Yes" if value == 1 else "No",
        )
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])

    with col2:
        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0,
            max_value=100,
            value=12,
            step=1,
        )
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"],
        )
        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"],
        )

    with col3:
        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"],
        )
        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"],
        )
        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Customer Services</div>
            <div class="section-subtitle">
                Select the customer's active telecom and internet services.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        online_security = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"],
        )
        online_backup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"],
        )

    with col2:
        device_protection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"],
        )
        tech_support = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"],
        )

    with col3:
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"],
        )
        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"],
        )

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Billing Information</div>
            <div class="section-subtitle">
                Enter the customer's billing information.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        monthly_charges = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            value=70.50,
            step=1.0,
            format="%.2f",
        )

    with col2:
        total_charges = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            value=846.0,
            step=10.0,
            format="%.2f",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    predict = st.form_submit_button("Run Churn Prediction")


# ============================================================
# PREDICTION
# ============================================================
if predict:
    customer = pd.DataFrame(
        [
            {
                "gender": gender,
                "SeniorCitizen": senior_citizen,
                "Partner": partner,
                "Dependents": dependents,
                "tenure": tenure,
                "PhoneService": phone_service,
                "MultipleLines": multiple_lines,
                "InternetService": internet_service,
                "OnlineSecurity": online_security,
                "OnlineBackup": online_backup,
                "DeviceProtection": device_protection,
                "TechSupport": tech_support,
                "StreamingTV": streaming_tv,
                "StreamingMovies": streaming_movies,
                "Contract": contract,
                "PaperlessBilling": paperless_billing,
                "PaymentMethod": payment_method,
                "MonthlyCharges": monthly_charges,
                "TotalCharges": total_charges,
            }
        ]
    )

    try:
        prediction = model.predict(customer)[0]

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(customer)[0]
            model_classes = list(getattr(model, "classes_", [0, 1]))

            if 1 in model_classes:
                churn_index = model_classes.index(1)
            elif "Yes" in model_classes:
                churn_index = model_classes.index("Yes")
            else:
                churn_index = min(1, len(probabilities) - 1)

            probability = float(probabilities[churn_index])
        else:
            probability = 1.0 if prediction in [1, "Yes", True] else 0.0

    except Exception as exc:
        st.error(
            "Prediction generate nahi ho saki. Model ke expected columns "
            f"aur input values ko check karein.\n\nError: `{exc}`"
        )
        st.stop()

    prediction_is_churn = prediction in [1, "Yes", True]

    if probability < 0.30:
        risk = "LOW"
        risk_icon = "🟢"
    elif probability < 0.60:
        risk = "MEDIUM"
        risk_icon = "🟡"
    else:
        risk = "HIGH"
        risk_icon = "🔴"

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Prediction Result</div>
            <div class="section-subtitle">
                Estimated churn outcome and probability.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    result_class = "result-danger" if prediction_is_churn else "result-safe"
    result_title = (
        "Customer Likely to Churn"
        if prediction_is_churn
        else "Customer Likely to Stay"
    )
    result_icon = "🔴" if prediction_is_churn else "🟢"

    st.markdown(
        f"""
        <div class="result-card {result_class}">
            <div class="result-label">AI Prediction</div>
            <div class="result-title">{result_icon} {result_title}</div>
            <div class="result-score">{probability:.1%}</div>
            <div class="result-note">Estimated churn probability</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Churn Probability", f"{probability:.1%}")

    with col2:
        st.metric("Risk Level", f"{risk_icon} {risk}")

    with col3:
        st.metric("Customer Tenure", f"{tenure} Months")

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Risk Analysis</div>
            <div class="section-subtitle">
                The probability bar represents the estimated churn risk.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(max(0.0, min(1.0, probability)))
    st.caption(f"Estimated churn probability: {probability:.1%}")

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Business Recommendation</div>
            <div class="section-subtitle">
                Recommended retention action based on the risk level.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if risk == "HIGH":
        st.error(
            "High risk customer. Immediate retention action recommended hai. "
            "Personalized discount, proactive support aur contract incentive offer karein."
        )
    elif risk == "MEDIUM":
        st.warning(
            "Medium risk customer. Customer ko monitor karein aur targeted offer "
            "ya proactive support provide karein."
        )
    else:
        st.success(
            "Low risk customer. Customer relationship stable lag rahi hai. "
            "Service quality maintain karein aur regular monitoring continue rakhein."
        )

    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Customer Summary</div>
            <div class="section-subtitle">
                Quick overview of the submitted customer information.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Tenure", f"{tenure} Months")

    with col2:
        st.metric("Monthly Charges", f"${monthly_charges:,.2f}")

    with col3:
        st.metric("Contract", contract)

    with col4:
        st.metric("Internet Service", internet_service)


# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="footer-box">
        <strong>ChurnIQ — Customer Churn Prediction System</strong><br>
        Python • Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
