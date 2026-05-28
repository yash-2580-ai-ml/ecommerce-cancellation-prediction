# =============================================================================
# NEXUS: PREDICTIVE REVENUE & RISK INGESTION ENGINE
# Premium Enterprise-Grade Transaction Risk Predictor
# =============================================================================

import streamlit as st
from pathlib import Path
import pickle
import numpy as np

# CRITICAL: st.set_page_config() MUST be the absolute first Streamlit command
st.set_page_config(
    page_title="NEXUS - Transaction Risk Predictor",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================================================================
# PREMIUM CUSTOM CSS - GLASSMORPHIC DESIGN SYSTEM
# =============================================================================

def inject_premium_css():
    """Elite enterprise design with glassmorphism, smooth animations, and premium typography."""
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --bg-primary: #0F172A;
        --bg-secondary: #1E293B;
        --bg-tertiary: #334155;
        --accent-primary: #6366F1;
        --accent-hover: #818CF8;
        --accent-light: #A5B4FC;
        --success: #10B981;
        --success-light: #D1FAE5;
        --error: #EF4444;
        --error-light: #FEE2E2;
        --text-primary: #F1F5F9;
        --text-secondary: #CBD5E1;
        --text-muted: #94A3B8;
        --border: #475569;
        --border-subtle: #334155;
    }

    * {
        box-sizing: border-box;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.3px;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0F172A 0%, #1A1F3A 50%, #0F172A 100%);
        min-height: 100vh;
        position: relative;
    }

    [data-testid="stHeader"] {
        background-color: transparent !important;
        padding: 0 !important;
    }

    [data-testid="stDeployLogoContainer"] {
        display: none !important;
    }

    .stMainBlockContainer {
        padding: 0 !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    /* ─────────────────────────────────────────────────────────────────────
       PREMIUM HEADER & HERO
       ───────────────────────────────────────────────────────────────────── */

    .nexus-header {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(99, 102, 241, 0.02) 100%);
        border-bottom: 1px solid rgba(99, 102, 241, 0.15);
        padding: 3.5rem 2rem;
        margin: 0;
        border-radius: 0 0 28px 28px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        animation: headerFadeIn 0.8s ease-out;
    }

    @keyframes headerFadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .nexus-header::before {
        content: '';
        position: absolute;
        top: -40%;
        right: -5%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        animation: float 8s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(20px); }
    }

    .nexus-header::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: 5%;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .nexus-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
        text-align: center;
    }

    .nexus-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        color: var(--text-primary);
        margin: 0 0 0.75rem 0;
        line-height: 1.15;
        background: linear-gradient(135deg, #F1F5F9 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .nexus-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: 400;
        color: var(--text-muted);
        letter-spacing: 0.4px;
        margin: 0;
        line-height: 1.7;
    }

    /* ─────────────────────────────────────────────────────────────────────
       MAIN WRAPPER & LAYOUT
       ───────────────────────────────────────────────────────────────────── */

    .nexus-main {
        max-width: 1100px;
        margin: 3rem auto;
        padding: 0 1.5rem;
        position: relative;
        z-index: 1;
    }

    /* ─────────────────────────────────────────────────────────────────────
       INPUT CARDS - GLASSMORPHISM
       ───────────────────────────────────────────────────────────────────── */

    .nexus-inputs {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.75rem;
        margin-bottom: 2.5rem;
        animation: cardsAppear 0.6s ease-out 0.3s backwards;
    }

    @keyframes cardsAppear {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .nexus-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(25px) saturate(180%);
        border: 1.5px solid rgba(99, 102, 241, 0.12);
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }

    .nexus-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1.5px;
        background: linear-gradient(90deg, transparent 0%, rgba(99, 102, 241, 0.6) 50%, transparent 100%);
        opacity: 0.5;
    }

    .nexus-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.15);
        transform: translateY(-6px);
        background: rgba(30, 41, 59, 0.65);
    }

    .nexus-label {
        font-family: 'Poppins', sans-serif;
        font-size: 1rem;
        font-weight: 650;
        color: var(--text-primary);
        margin-bottom: 1rem;
        display: block;
        letter-spacing: 0.3px;
    }

    .nexus-range {
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-top: 0.75rem;
        letter-spacing: 0.2px;
        font-weight: 500;
        display: block;
    }

    /* Streamlit slider customization */
    [data-testid="stSlider"] {
        padding: 0.75rem 0;
    }

    /* ─────────────────────────────────────────────────────────────────────
       CTA BUTTON - PREMIUM ACTION
       ───────────────────────────────────────────────────────────────────── */

    .nexus-cta-wrap {
        display: flex;
        justify-content: center;
        margin: 3rem 0;
    }

    [data-testid="stButton"] > button {
        width: 100%;
        max-width: 420px !important;
        padding: 1.1rem 2.8rem !important;
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-hover) 100%) !important;
        color: white !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 1.08rem !important;
        font-weight: 750 !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        border-radius: 14px !important;
        cursor: pointer !important;
        box-shadow: 0 8px 28px rgba(99, 102, 241, 0.35) !important;
        transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
    }

    [data-testid="stButton"] > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
        transition: left 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    [data-testid="stButton"] > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 14px 40px rgba(99, 102, 241, 0.5) !important;
    }

    [data-testid="stButton"] > button:hover::before {
        left: 100%;
    }

    /* ─────────────────────────────────────────────────────────────────────
       RISK OUTPUT CARDS
       ───────────────────────────────────────────────────────────────────── */

    .nexus-output {
        animation: slideUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        margin-bottom: 2rem;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .nexus-risk-high {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.06) 0%, rgba(239, 68, 68, 0.01) 100%);
        border: 2px solid rgba(239, 68, 68, 0.3);
        border-left: 5px solid #EF4444;
        border-radius: 18px;
        padding: 2.25rem;
        box-shadow: 0 10px 40px rgba(239, 68, 68, 0.12);
    }

    .nexus-risk-low {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.06) 0%, rgba(16, 185, 129, 0.01) 100%);
        border: 2px solid rgba(16, 185, 129, 0.3);
        border-left: 5px solid #10B981;
        border-radius: 18px;
        padding: 2.25rem;
        box-shadow: 0 10px 40px rgba(16, 185, 129, 0.12);
    }

    .nexus-risk-header {
        display: flex;
        align-items: center;
        gap: 1.25rem;
        margin-bottom: 1.5rem;
    }

    .nexus-risk-icon {
        font-size: 2.2rem;
        line-height: 1;
    }

    .nexus-risk-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 750;
        letter-spacing: 0.4px;
        margin: 0;
    }

    .nexus-risk-title-high { color: #EF4444; }
    .nexus-risk-title-low { color: #10B981; }

    .nexus-prob-display {
        margin-top: 1.5rem;
        padding: 2rem;
        background: rgba(0, 0, 0, 0.25);
        border-radius: 14px;
        text-align: center;
        border: 1px solid rgba(99, 102, 241, 0.1);
    }

    .nexus-prob-label {
        font-size: 0.8rem;
        color: var(--text-muted);
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .nexus-prob-value {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1;
        margin: 0.75rem 0 0 0;
    }

    .nexus-prob-high {
        color: #EF4444;
        text-shadow: 0 0 24px rgba(239, 68, 68, 0.4);
    }

    .nexus-prob-low {
        color: #10B981;
        text-shadow: 0 0 24px rgba(16, 185, 129, 0.4);
    }

    .nexus-risk-msg {
        font-size: 0.98rem;
        line-height: 1.8;
        margin: 1.5rem 0 0 0;
        letter-spacing: 0.3px;
    }

    .nexus-risk-msg-high { color: #FCA5A5; }
    .nexus-risk-msg-low { color: #A7F3D0; }

    /* ─────────────────────────────────────────────────────────────────────
       METRICS GRID
       ───────────────────────────────────────────────────────────────────── */

    .nexus-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.25rem;
        margin-top: 1.5rem;
    }

    .nexus-metric {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid var(--border-subtle);
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
        backdrop-filter: blur(10px);
        transition: all 0.4s ease;
    }

    .nexus-metric:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-3px);
    }

    .nexus-metric-label {
        font-size: 0.8rem;
        color: var(--text-muted);
        font-weight: 650;
        letter-spacing: 0.4px;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
    }

    .nexus-metric-value {
        font-family: 'Poppins', sans-serif;
        font-size: 1.6rem;
        font-weight: 750;
        color: var(--accent-light);
        letter-spacing: -0.5px;
    }

    /* ─────────────────────────────────────────────────────────────────────
       FOOTER
       ───────────────────────────────────────────────────────────────────── */

    .nexus-footer {
        text-align: center;
        color: var(--text-muted);
        font-size: 0.8rem;
        margin-top: 3.5rem;
        padding-top: 2rem;
        border-top: 1px solid var(--border-subtle);
        letter-spacing: 0.3px;
    }

    .nexus-footer span {
        color: var(--accent-primary);
        font-weight: 600;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# =============================================================================
# MACHINE LEARNING BACKEND
# =============================================================================

@st.cache_resource
def load_ml_models():
    """Load pre-trained Logistic Regression model and StandardScaler with error handling."""
    try:
        model_path = Path("logistic_model.pkl")
        scaler_path = Path("scaler.pkl")

        if not model_path.exists() or not scaler_path.exists():
            st.error("❌ **Critical Error:** ML Artifact files (`logistic_model.pkl` / `scaler.pkl`) missing.")
            return None, None

        with open(model_path, "rb") as f:
            model = pickle.load(f)

        with open(scaler_path, "rb") as f:
            scaler = pickle.load(f)

        return model, scaler

    except Exception as e:
        st.error(f"❌ Error loading ML artifacts: {str(e)}")
        return None, None

def predict_risk(price, freight_value, installments, model, scaler):
    """Generate risk prediction using scaled inputs and logistic regression."""
    try:
        features = np.array([[price, freight_value, installments]])
        features_scaled = scaler.transform(features)

        prediction = int(model.predict(features_scaled)[0])
        probability = float(model.predict_proba(features_scaled)[0][1])

        return prediction, probability
    except Exception as e:
        st.error(f"❌ Prediction error: {str(e)}")
        return None, None

# =============================================================================
# UI RENDERING FUNCTIONS
# =============================================================================

def render_header():
    """Render premium animated header."""
    st.markdown(
        """
        <div class="nexus-header">
            <div class="nexus-content">
                <h1 class="nexus-title">🛒 NEXUS: Predictive Revenue & Risk Engine</h1>
                <p class="nexus-subtitle">Enterprise Machine Learning Pipeline for Automated Order Attrition Mapping</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_input_cards():
    """Render input cards with sliders in a responsive grid layout."""
    # Open the structural main container div wrapper
    st.markdown('<div class="nexus-main">', unsafe_allow_html=True)
    st.markdown('<div class="nexus-inputs">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="nexus-card">', unsafe_allow_html=True)
        st.markdown('<label class="nexus-label">💰 Product Price</label>', unsafe_allow_html=True)
        price = st.slider("Price", min_value=0.0, max_value=500.0, value=100.0, step=5.0, label_visibility="collapsed")
        st.markdown('<span class="nexus-range">$0.00 — $500.00</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="nexus-card">', unsafe_allow_html=True)
        st.markdown('<label class="nexus-label">📦 Shipping / Freight</label>', unsafe_allow_html=True)
        freight_value = st.slider("Freight", min_value=0.0, max_value=100.0, value=25.0, step=2.5, label_visibility="collapsed")
        st.markdown('<span class="nexus-range">$0.00 — $100.00</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="nexus-card">', unsafe_allow_html=True)
        st.markdown('<label class="nexus-label">📅 Payment Installments</label>', unsafe_allow_html=True)
        installments = st.slider("Installments", min_value=1, max_value=24, value=6, step=1, label_visibility="collapsed")
        st.markdown('<span class="nexus-range">1 — 24 Months</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # Close inputs grid div
    return price, freight_value, installments

def render_cta_button():
    """Render premium call-to-action button."""
    st.markdown('<div class="nexus-cta-wrap">', unsafe_allow_html=True)
    clicked = st.button("🎯 Analyze Transaction Risk", use_container_width=False)
    st.markdown("</div>", unsafe_allow_html=True)
    return clicked

def render_risk_high(probability):
    """Render high-risk alert card component layout."""
    risk_pct = int(probability * 100)
    st.markdown(
        f"""
        <div class="nexus-output">
            <div class="nexus-risk-high">
                <div class="nexus-risk-header">
                    <span class="nexus-risk-icon">⚠️</span>
                    <h2 class="nexus-risk-title nexus-risk-title-high">HIGH RISK TARGET</h2>
                </div>
                <div class="nexus-prob-display">
                    <div class="nexus-prob-label">Cancellation Risk Probability</div>
                    <div class="nexus-prob-value nexus-prob-high">{risk_pct}%</div>
                </div>
                <p class="nexus-risk-msg nexus-risk-msg-high">
                    Core parameters match historical revenue attrition models. 
                    Immediate order interception recommended. Enhanced identity verification protocols advised.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_risk_low(probability):
    """Render low-risk success card component layout."""
    # FIX: Correct score scaling parameters to map success profiles cleanly
    success_pct = int((1 - probability) * 100)
    st.markdown(
        f"""
        <div class="nexus-output">
            <div class="nexus-risk-low">
                <div class="nexus-risk-header">
                    <span class="nexus-risk-icon">✅</span>
                    <h2 class="nexus-risk-title nexus-risk-title-low">SECURED CONVERSION</h2>
                </div>
                <div class="nexus-prob-display">
                    <div class="nexus-prob-label">Fulfillment Success Probability</div>
                    <div class="nexus-prob-value nexus-prob-low">{success_pct}%</div>
                </div>
                <p class="nexus-risk-msg nexus-risk-msg-low">
                    Structural velocity profiles indicate high likelihood of successful fulfillment. 
                    Proceed with standard processing and optimize for rapid inventory shipment execution.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_metrics(price, freight_value, installments, probability):
    """Render metrics grid framework component matrix."""
    success_pct = (1 - probability) * 100
    st.markdown(
        f"""
        <div class="nexus-metrics">
            <div class="nexus-metric">
                <div class="nexus-metric-label">Order Value</div>
                <div class="nexus-metric-value">${price:.2f}</div>
            </div>
            <div class="nexus-metric">
                <div class="nexus-metric-label">Logistics Cost</div>
                <div class="nexus-metric-value">${freight_value:.2f}</div>
            </div>
            <div class="nexus-metric">
                <div class="nexus-metric-label">Payment Terms</div>
                <div class="nexus-metric-value">{int(installments)}mo</div>
            </div>
            <div class="nexus-metric">
                <div class="nexus-metric-label">Fulfillment Confidence</div>
                <div class="nexus-metric-value">{success_pct:.1f}%</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_footer():
    """Render clean administrative pipeline attribution signature footer."""
    st.markdown(
        """
        <div class="nexus-footer">
            NEXUS v1.0 • Enterprise Predictive Analytics • 
            <span>Powered by Logistic Regression ML Pipeline</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =============================================================================
# MAIN APPLICATION FLOW
# =============================================================================

def main():
    """Main execution sequence controller logic routing."""
    # Inject design system properties
    inject_premium_css()

    # Render landing branding elements
    render_header()

    # Ingest analytical model coefficients
    model, scaler = load_ml_models()

    if model is None or scaler is None:
        st.stop()

    # Mount UI slider components
    price, freight_value, installments = render_input_cards()

    # Mount primary action selector button
    button_clicked = render_cta_button()

    # Execute downstream model evaluation routing metrics on validation click
    if button_clicked:
        prediction, probability = predict_risk(
            price, freight_value, installments, model, scaler
        )

        if prediction is not None and probability is not None:
            if prediction == 1:
                render_risk_high(probability)
            else:
                render_risk_low(probability)

            # Render summary reporting container panels
            render_metrics(price, freight_value, installments, probability)

    # Balance structure layout nodes and mount footer
    st.markdown("</div>", unsafe_allow_html=True)  # Close main layout container wrapper safely
    render_footer()

if __name__ == "__main__":
    main()