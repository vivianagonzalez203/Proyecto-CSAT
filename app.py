# app.py
import streamlit as st
import pandas as pd
import joblib

# ===========================
# Título y descripción
# ===========================
st.markdown(
    "<h2 style='text-align:center;'>📞 Predicción de Riesgo de Insatisfacción (CSAT) y asignación a CSR</h2>",
    unsafe_allow_html=True
)


# ===========================
# Cargar modelo y datos de referencia
# ===========================
rf_model = joblib.load("rf_final.pkl")
X_train_ref = pd.read_csv("X_train.csv")

# ===========================
# Función Frequency Encoding
# ===========================
def frequency_encoding(df, reference_df):
    df_fe = df.copy()
    for col in df.columns:
        freq = reference_df[col].value_counts(normalize=True)
        df_fe[col] = df[col].map(freq)
    df_fe.fillna(0, inplace=True)
    return df_fe

# ===========================
# Inputs del usuario
# ===========================
st.header("Ingrese los datos del cliente:")

channel_name = st.selectbox("Channel Name", sorted(X_train_ref['channel_name'].unique()))
category = st.selectbox("Category", sorted(X_train_ref['category'].unique()))
sub_category = st.selectbox("Sub-category", sorted(X_train_ref['Sub-category'].unique()))
agent_shift = st.selectbox("Agent Shift", sorted(X_train_ref['Agent Shift'].unique()))
tenure_bucket = st.selectbox("Tenure Bucket", sorted(X_train_ref['Tenure Bucket'].unique()))

# Crear DataFrame con input
input_df = pd.DataFrame({
    "channel_name": [channel_name],
    "category": [category],
    "Sub-category": [sub_category],
    "Agent Shift": [agent_shift],
    "Tenure Bucket": [tenure_bucket]
})

# ===========================
# Preprocesamiento
# ===========================
input_fe = frequency_encoding(input_df, X_train_ref)

# ===========================
# Predicción
# ===========================
pred_proba = rf_model.predict_proba(input_fe)[:, 1][0]  # Probabilidad clase 1
threshold = 0.55
pred_class = int(pred_proba >= threshold)

# ===========================
# Resultados (más grandes y visuales)
# ===========================
st.subheader("Resultado de la predicción")

if pred_class == 1:
    # Cliente en riesgo → rojo y alerta
    st.markdown(
        f"<h1 style='color:red;'>Atención prioritaria 🚨</h1>"
        f"<h3>Probabilidad: {pred_proba:.2f}</h3>",
        unsafe_allow_html=True
    )
else:
    # Cliente no en riesgo → verde y check
    st.markdown(
        f"<h1 style='color:green;'>✅ Sin alertas</h1>"
        f"<h3>Probabilidad: {pred_proba:.2f}</h3>",
        unsafe_allow_html=True
    )