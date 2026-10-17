import streamlit as st
import requests
from google import genai
from puente_jarvis_nova import PuenteTactico

# Inicializar el puente dual y cliente de Gemini con la llave activa
puente = PuenteTactico()
client = genai.Client(api_key="AQ.Ab8RN6JrkHX_Qfqyas6PskPgyzhJiKj6E-wuy62AJdUh9OQAhg")

st.set_page_config(page_title="N.O.V.A. - Núcleo Táctico", page_icon="🟢", layout="wide")

# Estilos visuales tácticos (Verde Matrix)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff66;
    }
    .main { 
        background-color: #0e1117; 
        color: #00ff66; 
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00ff66 !important;
    }
    .stTextInput input, textarea { 
        background-color: #161b22 !important; 
        color: #00ff66 !important; 
        border: 1px solid #00ff66 !important; 
    }
    [data-testid="stMetricValue"] {
        color: #00ff66 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Módulos compactos ubicados en la barra lateral izquierda
with st.sidebar:
    st.markdown("### 🟢 N.O.V.A. // Panel")
    st.markdown("— *Modo Dual Activo* —")
    st.divider()
    
    st.subheader("📊 Módulo Financiero")
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,clp"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            precios = response.json()
            st.metric("BTC", f"${precios.get('bitcoin', {}).get('usd', 0):,} USD")
            st.metric("ETH", f"${precios.get('ethereum', {}).get('usd', 0):,} USD")
            st.metric("USDT", f"${precios.get('tether', {}).get('clp', 0)} CLP")
        else:
            st.write("Cotización en espera...")
    except Exception:
        st.write("Finanzas: Offline")

    st.divider()
    st.subheader("🔗 Enlace JARVIS")
    registros = puente.leer_ultimos_registros(3)
    if registros:
        for reg in registros:
            st.caption(f"[{reg['origen']}] {reg['timestamp'][11:19]}: {reg['mensaje']}")
    else:
        st.caption("Sin transmisiones recientes.")

# Consola Central de Operaciones principal (arriba y con todo el espacio)
st.title("🟢 N.O.V.A. // Consola Central de Operaciones")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ingrese comando o consulta para N.O.V.A..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Registrar en el puente dual
    puente.registrar_transmision("NOVA", prompt)

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt,
            )
            reply = response.text
        except Exception as e:
            reply = f"Error en el motor táctico de IA: {e}"
        
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
