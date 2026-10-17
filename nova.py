import streamlit as st
import os
import requests
from google import genai
from puente_jarvis_nova import PuenteTactico

# Inicializar el puente dual y cliente de Gemini
puente = PuenteTactico()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

st.set_page_config(page_title="N.O.V.A. - Núcleo Táctico", page_icon="🟢", layout="wide")

# Estilos visuales tácticos
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff66; }
    .stTextInput input { background-color: #161b22; color: #00ff66; border: 1px solid #00ff66; }
    </style>
""", unsafe_allow_html=True)

st.title("🟢 N.O.V.A. // IA Autónoma II")
st.markdown("— *Enlace táctico con J.A.R.V.I.S. & Gemini Activo (Modo Dual)* —")

# Sección de Módulos Tácticos superiores
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Módulo Financiero en Vivo")
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,clp"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            precios = response.json()
            st.metric("Bitcoin (BTC)", f"${precios.get('bitcoin', {}).get('usd', 0):,} USD")
            st.metric("Ethereum (ETH)", f"${precios.get('ethereum', {}).get('usd', 0):,} USD")
            st.metric("USDT (Stablecoin)", f"${precios.get('tether', {}).get('clp', 0)} CLP aprox.")
        else:
            st.info("Sistemas de cotización en espera de reintento.")
    except Exception:
        st.warning("Módulo Financiero: Enlace de red offline temporalmente.")

with col2:
    st.subheader("🔗 Enlace Dual JARVIS")
    registros = puente.leer_ultimos_registros(3)
    if registros:
        for reg in registros:
            st.text(f"[{reg['origen']}] {reg['timestamp'][11:19]}: {reg['mensaje']}")
    else:
        st.text("Sin transmisiones recientes en el puente.")

st.divider()

# Consola Central de Chat con Gemini
st.subheader("Consola Central de Operaciones")

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
                model='gemini-2.5-flash',
                contents=prompt,
            )
            reply = response.text
        except Exception as e:
            reply = f"Error en el motor táctico de IA: {e}"
        
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
