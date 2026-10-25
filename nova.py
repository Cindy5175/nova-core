import os
import io
import base64
import time
import streamlit as st
from groq import Groq

# 1. Configuración de la página
st.set_page_config(
    page_title="Sistema C.I.T. / J.A.R.V.I.S. & N.O.V.A.", 
    page_icon="⚛️", 
    layout="centered"
)

# Inicializar estados en sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "modo_sistema" not in st.session_state:
    st.session_state.modo_sistema = "J.A.R.V.I.S. (Azul Neón)"

if "ubicacion_jefa" not in st.session_state:
    st.session_state.ubicacion_jefa = "Buin, Santiago, Chile"
    st.session_state.lat_lon = "-33.7333, -70.7333"

if "energia_arc" not in st.session_state:
    st.session_state.energia_arc = 98

if "notas_mision" not in st.session_state:
    st.session_state.notas_mision = "• Sincronizar protocolos de red\n• Optimizar módulos tácticos"

# -------------------------------------------------------------
# 🔐 MÓDULO DE CLAVE DE ACCESO (PIN DE SEGURIDAD)
# -------------------------------------------------------------
PIN_SECRETO = "Jarvis"  # Clave de acceso oficial configurada por la Jefa

if not st.session_state.autenticado:
    st.markdown(
        """
        <style>
        .login-box {
            background: rgba(5, 12, 30, 0.95);
            border: 2px solid #00d2ff;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 0 25px #00d2ff44;
            font-family: 'Courier New', monospace;
            max-width: 400px;
            margin: 50px auto;
        }
        </style>
        <div class="login-box">
            <h2 style="color: #00d2ff; margin-bottom: 10px;">🔒 ACCESO RESTRINGIDO</h2>
            <p style="color: #aaa; font-size: 0.85rem;">Introduce la clave de seguridad para desbloquear la estación de comando C.I.T.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        pin_ingresado = st.text_input("Clave de Acceso:", type="password", placeholder="Contraseña secreta")
        if st.button("🔓 Desbloquear Sistema", use_container_width=True):
            if pin_ingresado == PIN_SECRETO:
                st.session_state.autenticado = True
                st.success("¡Acceso concedido, Jefa!")
                st.rerun()
            else:
                st.error("⚠️ Clave incorrecta. Acceso denegado.")
    st.stop()
# -------------------------------------------------------------

# 2. Conexión robusta con soporte dual (Secrets de Streamlit o variables de entorno)
groq_api_key = None
try:
    if "GROQ_API_KEY" in st.secrets:
        groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

if not groq_api_key:
    groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("⚠️ Error: La clave API de Groq no se detecta en los Secrets de Streamlit. Verifica que esté guardada correctamente en el panel de configuración.")
    st.stop()

client = Groq(api_key=groq_api_key)
