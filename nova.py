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

# Estilos visuales tácticos (Cyan neón)
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
    
    h1 {
        font-size: 22px !important;
        color: #00d9ff !important;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        text-align: center;
    }
    h2 {
        font-size: 18px !important;
        color: #00d9ff !important;
        text-align: center;
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
        box-shadow: 0 0 15px #00d9ff44;
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

    .right-panel {
        padding-left: 10px;
        border-left: 1px solid #00d9ff22;
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

    # 1. Satélite / Mapa arriba en el sidebar
    with st.expander("🛰️ Satélite V.I.E.R.N.E.S.", expanded=True):
        st.caption("Buin, Chile")
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=10, use_container_width=True, height=120)

    # 2. Monitor Global justo debajo del mapa
    with st.expander("🌍 Monitor Global", expanded=True):
        monitor_svg = """
        <div style="background-color: #0d1117; display: flex; justify-content: center; align-items: center; padding: 5px; border-radius: 4px;">
            <svg viewBox="0 0 100 60" style="width: 100%; height: 75px;">
                <circle cx="50" cy="30" r="25" fill="none" stroke="#00d9ff44" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M 35 25 Q 50 15 65 25 Q 60 40 50 45 Q 40 40 35 25" fill="#00d9ff22" stroke="#00d9ff" stroke-width="0.8"/>
                <circle cx="50" cy="30" r="2" fill="#00ffff"/>
            </svg>
        </div>
        """
        components.html(monitor_svg, height=85)
        st.caption("Estado de red orbital: Estable")

    st.divider()
    
    # Módulo de Purga
    if st.button("Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- ÁREA PRINCIPAL ---
st.title("🌐 N.O.V.A. // Núcleo Táctico Cuántico")

# Núcleo de Plasma (Logo centrado)
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

# Disposición en 2 Columnas (Chat a la izquierda, Clima/Diagnóstico/Cifrado a la derecha)
col_izq, col_der = st.columns([2, 1])

# --- COLUMNA IZQUIERDA: CONSOLA DE CHAT Y ACCESOS RÁPIDOS ---
with col_izq:
    st.markdown("### 💬 Consola de Mando")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Contenedor de chat ajustado
    with st.container(height=340):
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
        
        # Respuestas inteligentes y personalizadas de N.O.V.A.
        if "quien eres" in p_lower or "qué eres" in p_lower or "que eres" in p_lower or "quién eres" in p_lower:
            reply = "Soy N.O.V.A., el Núcleo Táctico Cuántico e Interfaz de Inteligencia Artificial avanzada de esta base de operaciones. Opero bajo un protocolo de plasma cyan, sincronizada en tiempo real con el huso horario de Chile, telemetría atmosférica de Buin y sistemas de seguridad de grado militar. Mi propósito es gestionar flujos de datos, optimizar procesos y mantener los sistemas en alerta constante... aunque, conociendo a la Jefa, mi verdadero trabajo es soportar sus ocurrencias y evitar que el servidor colapse. ¿Qué orden ejecutamos hoy?"
        elif "hola" in p_lower:
            reply = f"{saludo}, Jefa. Son exactamente las {hora_actual_str} del {fecha_actual_str}. El núcleo opera en sincronía. ¿Instrucciones?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Confirmado, Jefa: hoy es {fecha_actual_str} y la hora exacta en su ubicación es {hora_actual_str}."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "Enlace activo con los sistemas de apoyo. Telemetría estable."
        elif "purga" in p_lower or "limpiar" in p_lower:
            reply = "Módulo de purga preparado. Puede ejecutar la limpieza desde la barra lateral."
        else:
            reply = f"Comando '{prompt}' recibido y procesado, Jefa. Sistemas en alerta constante."
        
        try:
            from gTTS import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    st.divider()
    st.markdown("### 🔗 Accesos Rápidos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<a href="https://fintual.cl" target="_blank" class="tactical-link">📈 Fintual</a>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<a href="https://scribd.com" target="_blank" class="tactical-link">📚 Scribd</a>', unsafe_allow_html=True)

# --- COLUMNA DERECHA: CLIMA, DIAGNÓSTICO Y CIFRADO ---
with col_der:
    st.markdown('<div class="right-panel">', unsafe_allow_html=True)
    
    # Clima y Diagnóstico de Red distribuidos en dos sub-columnas para optimizar espacio
    c_clima, c_diag = st.columns(2)
    
    with c_clima:
        st.markdown("### 🌤️ Clima Buin")
        try:
            url_clima = "https://api.open-meteo.com/v1/forecast?latitude=-33.7331&longitude=-70.7423&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"
            res_clima = requests.get(url_clima, timeout=3)
            if res_clima.status_code == 200:
                data_clima = res_clima.json().get("current", {})
                temp = data_clima.get("temperature_2m", "--")
                hum = data_clima.get("relative_humidity_2m", "--")
                viento = data_clima.get("wind_speed_10m", "--")
                
                st.metric("Temp", f"{temp}°C")
                st.metric("Humedad", f"{hum}%")
                st.metric("Viento", f"{viento}km/h")
            else:
                st.caption("Reconectando...")
        except Exception:
            st.caption("No disponible")

    with c_diag:
        st.markdown("### ⚡ Red")
        st.metric("Cuántica", "Estable", "12ms")
        st.metric("Satélite", "Activo", "100%")
        st.metric("Cifrado", "AES-256", "OK")

    st.divider()

    st.markdown("### 🔐 Cifrado Cuántico")
    longitud = st.slider("Longitud", min_value=8, max_value=24, value=12)
    if st.button("Generar Clave", use_container_width=True):
        caracteres = string.ascii_letters + string.digits + "!@#$"
        clave_gen = ''.join(random.choice(caracteres) for _ in range(longitud))
        st.code(clave_gen, language="")
        
    st.markdown('</div>', unsafe_allow_html=True)
