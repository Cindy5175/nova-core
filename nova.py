import streamlit as st
import requests
from puente_jarvis_nova import PuenteTactico

# Inicializar el puente dual
puente = PuenteTactico()

st.set_page_config(page_title="N.O.V.A. - Núcleo Táctico", page_icon="🟢", layout="wide")

# Estilos visuales tácticos (Verde Matrix y módulos compactos en barra lateral)
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
    /* Estilo compacto para elementos en la barra lateral */
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Módulos compactos ubicados en la barra lateral izquierda
with st.sidebar:
    st.markdown("### 🟢 N.O.V.A. // Panel")
    st.markdown("— *Modo Dual Activo* —")
    st.divider()
    
    # Módulo Financiero compacto (usando un expander pequeño)
    with st.expander("📊 Finanzas (En vivo)", expanded=False):
        try:
            url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,clp"
            response_crypto = requests.get(url_crypto, timeout=3)
            if response_crypto.status_code == 200:
                precios = response_crypto.json()
                st.metric("BTC", f"${precios.get('bitcoin', {}).get('usd', 0):,} USD")
                st.metric("ETH", f"${precios.get('ethereum', {}).get('usd', 0):,} USD")
                st.metric("USDT", f"${precios.get('tether', {}).get('clp', 0)} CLP")
            else:
                st.write("Cotización en espera...")
        except Exception:
            st.write("Finanzas: Offline")

    # Módulo Enlace JARVIS compacto
    with st.expander("🔗 Enlace JARVIS", expanded=False):
        registros = puente.leer_ultimos_registros(3)
        if registros:
            for reg in registros:
                st.caption(f"[{reg['origen']}] {reg['timestamp'][11:19]}: {reg['mensaje']}")
        else:
            st.caption("Sin transmisiones.")

    # Módulo Satelital V.I.E.R.N.E.S. y Mapa de ubicación (Buin)
    with st.expander("🛰️ Satélite V.I.E.R.N.E.S.", expanded=True):
        st.caption("Ubicación: Buin, Stgo (Región Metropolitana)")
        import pandas as pd
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=10, use_container_width=True)

    st.divider()
    
    # Módulo de Purga (mismo color y estilo táctico)
    st.subheader("🧹 Módulo de Purga")
    if st.button("Ejecutar Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Encabezado principal actualizado
st.title("🟢 N.O.V.A. // AI Autónoma II")

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
        # Motor de respuestas de respaldo local inteligente y fluido
        p_lower = prompt.lower()
        if "hola" in p_lower:
            reply = "¡Saludos, Jefa! N.O.V.A. en línea y operando con el núcleo táctico de respaldo activo. ¿Qué órdenes tenemos para hoy?"
        elif "bitcoin" in p_lower or "btc" in p_lower or "precio" in p_lower:
            reply = "Los módulos financieros están enlazados en tiempo real en la barra lateral izquierda dentro de su respectivo panel compacto."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "Sistemas de enlace con J.A.R.V.I.S. y el satélite de V.I.E.R.N.E.S. sincronizados y monitoreando el sector de Buin."
        elif "purga" in p_lower:
            reply = "Secuencia de purga disponible desde el panel lateral izquierdo, Jefa."
        else:
            reply = f"Comando recibido y registrado en el sistema: '{prompt}'. Núcleo operativo y listo para la siguiente instrucción, Jefa."
        
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
