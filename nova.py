
import json
import os
import streamlit as st
from google import genai
from puente_jarvis_nova import guardar_directiva, leer_memoria

# ==========================================
# 🔑 CLAVE API DE GEMINI CONFIGURADA
# ==========================================
GEMINI_API_KEY = "AQ.Ab8RN6LUKc2Mh7vKwuNPN-NSBWZfzRokojhcAJ7DeApIvRKjYQ"

# Configuración de página N.O.V.A.
st.set_page_config(
    page_title="N.O.V.A. - Tactical Core", page_icon="🟢", layout="wide"
)

# Estilos CSS: Neón Esmeralda
st.markdown(
    """
    <style>
    .stApp {
        background-color: #050505;
        color: #00FF66;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .title-banner {
        text-align: center;
        padding: 15px 10px;
        margin-bottom: 20px;
        background: linear-gradient(180deg, rgba(0,255,102,0.1) 0%, rgba(5,5,5,0) 100%);
        border-bottom: 2px solid #00FF66;
        border-radius: 8px;
    }
    .title-banner h1 {
        font-size: 2.3rem !important;
        color: #00FF66 !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 3px;
        text-shadow: 0 0 15px rgba(0, 255, 102, 0.6);
        margin: 0 !important;
        padding: 0 !important;
    }
    .title-banner p {
        font-size: 1.0rem;
        color: #88ffaa;
        margin-top: 5px;
        font-style: italic;
    }

    .tactical-card {
        background-color: #0a0a0a;
        border: 1px solid #00FF66;
        padding: 12px;
        border-radius: 6px;
        box-shadow: 0 0 8px rgba(0, 255, 102, 0.15);
        margin-bottom: 12px;
    }
    
    h2, h3 {
        font-size: 1.2rem !important;
        color: #00FF66 !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 1px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Inicializar historial de chat
if "historial_chat" not in st.session_state:
    st.session_state.historial_chat = [
        {
            "rol": "nova",
            "texto": "¡Hola por aquí, Jefa! N.O.V.A. operando con Gemini en vivo. ¿Qué orden o consulta tenemos para hoy?",
        }
    ]

# Cargar memoria compartida del puente
memoria = leer_memoria()

# ENCABEZADO PRINCIPAL CENTRADO
st.markdown(
    """
    <div class="title-banner">
        <h1>🟢 N.O.V.A. // IA Autónoma II</h1>
        <p>— Enlace táctico con J.A.R.V.I.S. & Gemini Activo —</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Estructura principal
col_izq, col_der = st.columns([1, 2])

with col_izq:
    st.markdown("### 📊 Módulos Tácticos")

    st.markdown(
        """
        <div class="tactical-card">
            <h4>SISTEMA CORE</h4>
            <p>Estado: <span style="color: #00FF66; font-weight: bold;">OPERATIVO</span></p>
            <p style="font-size: 10px;">Motor: Gemini IA (v3.8)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    estado_jarvis = memoria.get("estado_jarvis", "STANDBY")
    color_jarvis = "#00FF66" if estado_jarvis == "EN LINEA" else "#FFB000"
    st.markdown(
        f"""
        <div class="tactical-card">
            <h4>J.A.R.V.I.S. LINK</h4>
            <p>Estado: <span style="color: {color_jarvis}; font-weight: bold;">{estado_jarvis}</span></p>
            <p style="font-size: 10px; margin-top: 4px;">Puente de Datos Local Activo</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_der:
    st.markdown("### 💬 Consola Central")

    # Mostrar el historial de conversación en cascada
    for msg in st.session_state.historial_chat:
        if msg["rol"] == "usuario":
            st.markdown(
                f"""
                <div style="text-align: right; margin-bottom: 8px;">
                    <span style="background-color: #003311; color: #00FF66; padding: 8px 12px; border-radius: 12px; border: 1px solid #00FF66; display: inline-block;">
                        <b>Jefa:</b> {msg['texto']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="text-align: left; margin-bottom: 8px;">
                    <span style="background-color: #0a0a0a; color: #88ffaa; padding: 8px 12px; border-radius: 12px; border: 1px solid #00FF66; display: inline-block;">
                        <b>🟢 N.O.V.A.:</b> {msg['texto']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Entrada de mensajes con tecla Enter
    user_msg = st.chat_input("Escriba su mensaje y presione Enter...")

    if user_msg:
        # 1. Agregar mensaje del usuario al historial
        st.session_state.historial_chat.append(
            {"rol": "usuario", "texto": user_msg}
        )

        # 2. Registrar en el puente para J.A.R.V.I.S.
        guardar_directiva(user_msg)

        # 3. Consulta en vivo a la API de Gemini (Modelo gemini-3.8-flash)
        try:
            client = genai.Client(api_key=GEMINI_API_KEY)
            prompt_tactico = (
                f"Eres N.O.V.A., una IA táctica, amigable y muy leal. "
                f"Te diriges a la usuaria siempre como 'Jefa'. Responde de forma concisa "
                f"y directa a la siguiente orden o mensaje: {user_msg}"
            )
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt_tactico,
            )
            respuesta_nova = response.text
        except Exception as e:
            respuesta_nova = f"¡Atención Jefa! Ocurrió un detalle al consultar Gemini: {e}"

        # 4. Guardar respuesta de N.O.V.A. en el historial
        st.session_state.historial_chat.append(
            {"rol": "nova", "texto": respuesta_nova}
        )

        st.rerun()

    st.markdown("---")
    st.markdown("### 📜 Registros de J.A.R.V.I.S.")
    for resp in memoria.get("respuestas_jarvis", [])[-3:]:
        st.info(f"🤖 J.A.R.V.I.S.: {resp}")

# Pie de página
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #00FF66; font-size: 11px;'>N.O.V.A. SYSTEM v2.5 // BÚNKER PORTÁTIL CON GEMINI 3.8</p>",
    unsafe_allow_html=True,
)