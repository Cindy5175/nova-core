import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
import streamlit.components.v1 as components
import string
import random

# Configuración de la zona horaria de Chile (UTC-3)
CHILE_TZ = timezone(timedelta(hours=-3))

# --- CLASE INTERNA DE ENLACE TÁCTICO ---
class PuenteTacticoUnificado:
    def __init__(self):
        if "telemetria_jarvis" not in st.session_state:
            ahora_cl = datetime.now(CHILE_TZ)
            st.session_state.telemetria_jarvis = [
                {"origen": "JARVIS", "timestamp": ahora_cl.strftime("%Y-%m-%d %H:%M:%S"), "mensaje": "Núcleo de plasma N.O.V.A. estabilizado."},
                {"origen": "VIERNES", "timestamp": ahora_cl.strftime("%Y-%m-%d %H:%M:%S"), "mensaje": "Sensores cuánticos en línea."}
            ]

    def registrar_transmision(self, origen, mensaje):
        ahora_cl = datetime.now(CHILE_TZ)
        nuevo_registro = {
            "origen": origen,
            "timestamp": ahora_cl.strftime("%Y-%m-%d %H:%M:%S"),
            "mensaje": mensaje
        }
        st.session_state.telemetria_jarvis.insert(0, nuevo_registro)
        if len(st.session_state.telemetria_jarvis) > 10:
            st.session_state.telemetria_jarvis.pop()

    def leer_ultimos_registros(self, cantidad=3):
        return st.session_state.telemetria_jarvis[:cantidad]

# Inicializar el puente unificado
puente = PuenteTacticoUnificado()

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="N.O.V.A. - Núcleo Táctico", page_icon="🌐", layout="wide")

# Estilos visuales tácticos (Cyan neón) con tipografía reducida
st.markdown("""
    <style>
    .stApp {
        background-color: #06090f;
        color: #00d9ff;
        font-family: 'Space Mono', monospace;
    }
    .main { 
        background-color: #06090f; 
        color: #00d9ff; 
    }
    
    /* Reducción de tamaños de encabezados */
    h1 {
        font-size: 22px !important;
        color: #00d9ff !important;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    h2 {
        font-size: 18px !important;
        color: #00d9ff !important;
    }
    h3 {
        font-size: 14px !important;
        color: #00d9ff !important;
        letter-spacing: 1px;
    }
    
    .stTextInput input, textarea { 
        background-color: #0d1117 !important; 
        color: #00d9ff !important; 
        border: 1px solid #00d9ff !important; 
        border-radius: 4px;
        font-size: 12px !important;
    }
    
    [data-testid="stMetricValue"] {
        color: #00d9ff !important;
        font-size: 16px !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 11px !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #00d9ff66;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
    }
    
    hr {
        border-color: #00d9ff44;
        margin: 10px 0;
    }
    
    .stButton > button {
        background-color: transparent;
        color: #00d9ff;
        border: 1px solid #00d9ff;
        font-weight: bold;
        font-size: 11px;
        text-transform: uppercase;
        box-shadow: 0 0 5px #00d9ff22;
        padding: 4px 8px;
    }
    .stButton > button:hover {
        background-color: #00d9ff11;
        border-color: #00ffff;
        box-shadow: 0 0 10px #00d9ff44;
    }
    
    [data-testid="stChatMessage"] {
        background-color: #0d1117;
        border: 1px solid #00d9ff33;
        border-radius: 6px;
        padding: 8px;
        margin-bottom: 6px;
    }
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        color: #aae0ff;
        font-size: 13px;
    }

    /* Enlaces compactos tácticos */
    .tactical-link {
        display: block;
        width: 100%;
        padding: 6px;
        margin: 4px 0;
        background-color: #0d1117;
        color: #00d9ff !important;
        text-align: center;
        text-decoration: none;
        border: 1px solid #00d9ff44;
        border-radius: 4px;
        font-weight: bold;
        font-size: 11px;
        transition: 0.2s;
    }
    .tactical-link:hover {
        background-color: #00d9ff22;
        border-color: #00ffff;
    }
    </style>
""", unsafe_allow_html=True)

# --- PANEL LATERAL TÁCTICO (Sidebar) ---
with st.sidebar:
    st.markdown("### 🌐 N.O.V.A. // Núcleo")
    st.caption("Interfaz Táctica")
    st.divider()
    
    # Módulo Reloj Táctico en Vivo
    ahora_local = datetime.now(CHILE_TZ)
    st.markdown(f"📅 **Fecha:** {ahora_local.strftime('%d/%m/%Y')}")
    st.markdown("⏰ **Hora Táctica (Local):**")
    
    reloj_html = """
    <div style="background-color: #0d1117; color: #00d9ff; font-family: 'Space Mono', monospace; padding: 6px; border-radius: 4px; border: 1px solid #00d9ff; text-align: center; margin-bottom: 8px;">
        <div id="clock" style="font-size: 18px; font-weight: bold; color: #00d9ff; letter-spacing: 2px;">00:00:00</div>
    </div>
    <script>
    function updateClock() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        document.getElementById('clock').innerText = hours + ':' + minutes + ':' + seconds;
    }
    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    components.html(reloj_html, height=55)
    st.divider()

    # Módulo de Estado del Núcleo
    with st.expander("📊 Estado del Núcleo", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Plasma", "1.2 MK")
        with col2:
            st.metric("Sincronía", "99.8%")
        st.caption("Estado: ONLINE")

    # Módulo Enlace JARVIS
    with st.expander("🔗 Enlace JARVIS", expanded=False):
        registros = puente.leer_ultimos_registros(3)
        if registros:
            for reg in registros:
                st.caption(f"[{reg['origen']}] {reg['timestamp'][11:19]}: {reg['mensaje']}")
        else:
            st.caption("Sin transmisiones.")

    # Módulo Satelital V.I.E.R.N.E.S.
    with st.expander("🛰️ Satélite V.I.E.R.N.E.S.", expanded=True):
        st.caption("Buin, Chile")
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=10, use_container_width=True, height=120)

    st.divider()
    
    # Módulo de Purga
    if st.button("Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- ÁREA PRINCIPAL EN 3 COLUMNAS ---
st.title("🌐 N.O.V.A. // Núcleo Táctico Cuántico")

# Núcleo de Plasma Integrado
nucleo_plasma_html = """
<div style="display: flex; justify-content: center; align-items: center; margin: 10px 0;">
    <svg viewBox="0 0 100 100" style="width: 170px; height: 170px;">
        <defs>
            <filter id="glow">
                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                <feMerge>
                    <feMergeNode in="coloredBlur"/>
                    <feMergeNode in="SourceGraphic"/>
                </feMerge>
            </filter>
            <radialGradient id="plasma">
                <stop offset="10%" stop-color="#ffffff"/>
                <stop offset="40%" stop-color="#00ffff"/>
                <stop offset="90%" stop-color="#0080ff"/>
                <stop offset="100%" stop-color="#000033"/>
            </radialGradient>
        </defs>
        
        <circle cx="50" cy="50" r="48" fill="#0d1117" stroke="#00d9ff44" stroke-width="0.5"/>
        
        <circle cx="50" cy="50" r="45" fill="none" stroke="#00d9ff66" stroke-width="1.5" stroke-dasharray="8 8">
            <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="15s" repeatCount="indefinite" />
        </circle>
        <circle cx="50" cy="50" r="40" fill="none" stroke="#00d9ff" stroke-width="2" stroke-dasharray="1 3" filter="url(#glow)">
            <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="-360 50 50" dur="20s" repeatCount="indefinite" />
        </circle>
        
        <polygon points="50,15 80,32.5 80,67.5 50,85 20,67.5 20,32.5" fill="none" stroke="#00d9ff44" stroke-width="1"/>
        <polygon points="50,20 76,35 76,65 50,80 24,65 24,35" fill="none" stroke="#00ffff" stroke-width="1.5" filter="url(#glow)"/>
        
        <circle cx="50" cy="50" r="18" fill="url(#plasma)" filter="url(#glow)">
            <animate attributeName="r" values="18;19;18" dur="3s" repeatCount="indefinite" />
        </circle>
    </svg>
</div>
"""
components.html(nucleo_plasma_html, height=180)

# Disposición en 3 columnas: Izquierda (Clima), Centro (CHAT PRIORITARIO), Derecha (Bóveda/Enlaces)
col_izq, col_centro, col_der = st.columns([1, 2, 1])

# --- COLUMNA IZQUIERDA: TELEMETRÍA CLIMÁTICA ---
with col_izq:
    st.markdown("### 🌤️ Clima Buin")
    try:
        url_clima = "https://api.open-meteo.com/v1/forecast?latitude=-33.7331&longitude=-70.7423&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"
        res_clima = requests.get(url_clima, timeout=3)
        if res_clima.status_code == 200:
            data_clima = res_clima.json().get("current", {})
            temp = data_clima.get("temperature_2m", "--")
            hum = data_clima.get("relative_humidity_2m", "--")
            viento = data_clima.get("wind_speed_10m", "--")
            
            st.metric("Temperatura", f"{temp} °C")
            st.metric("Humedad", f"{hum} %")
            st.metric("Viento", f"{viento} km/h")
        else:
            st.caption("Reconectando clima...")
    except Exception:
        st.caption("Clima no disponible")

# --- COLUMNA CENTRAL: ÁREA DE CHAT (PRIORIDAD) ---
with col_centro:
    st.markdown("### 💬 Consola de Mando")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Contenedor con altura limitada para mantener el chat acortado y centrado
    with st.container(height=320):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "audio" in message and message["audio"]:
                    st.audio(message["audio"], format="audio/mp3")

    prompt = st.chat_input("Comando para N.O.V.A...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        puente.registrar_transmision("NOVA", prompt)

        ahora = datetime.now(CHILE_TZ)
        hora_num = ahora.hour
        hora_actual_str = ahora.strftime("%H:%M:%S")
        fecha_actual_str = ahora.strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        if 5 <= hora_num < 12:
            saludo = "Buenos días"
        elif 12 <= hora_num < 20:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"
        
        if "hola" in p_lower:
            reply = f"{saludo}, Jefa. Son exactamente las {hora_actual_str} del {fecha_actual_str}. El núcleo opera en sincronía. ¿Instrucciones?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Confirmado: hoy es {fecha_actual_str} y la hora exacta en Buin es {hora_actual_str}."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "Enlace activo. Telemetría estable."
        elif "purga" in p_lower or "limpiar" in p_lower:
            reply = "Ejecute la limpieza desde la barra lateral."
        else:
            reply = f"Comando '{prompt}' procesado, Jefa. Sistemas en alerta."
        
        try:
            from gtts import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

# --- COLUMNA DERECHA: CIFRADO Y ACCESOS RÁPIDOS ---
with col_der:
    st.markdown("### 🔐 Cifrado Cuántico")
    longitud = st.slider("Longitud", min_value=8, max_value=24, value=12)
    if st.button("Generar Clave", use_container_width=True):
        caracteres = string.ascii_letters + string.digits + "!@#$"
        clave_gen = ''.join(random.choice(caracteres) for _ in range(longitud))
        st.code(clave_gen, language="")

    st.markdown("### 🔗 Accesos Rápidos")
    st.markdown('<a href="https://crypto.com" target="_blank" class="tactical-link">🪙 Crypto.com</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://fintual.cl" target="_blank" class="tactical-link">📈 Fintual</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://scribd.com" target="_blank" class="tactical-link">📚 Scribd</a>', unsafe_allow_html=True)
