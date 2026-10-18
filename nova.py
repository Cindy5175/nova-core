import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
import streamlit.components.v1 as components

# Configuración de la zona horaria de Chile (UTC-4 / UTC-3 según corresponda)
# Para evitar dependencias externas, definimos UTC-3 (horario de verano / actual de Chile)
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
    
    h1, h2, h3, h4, h5, h6 {
        color: #00d9ff !important;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .stTextInput input, textarea { 
        background-color: #0d1117 !important; 
        color: #00d9ff !important; 
        border: 2px solid #00d9ff !important; 
        border-radius: 4px;
        box-shadow: 0 0 10px #00d9ff22;
    }
    
    [data-testid="stMetricValue"] {
        color: #00d9ff !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 2px solid #00d9ff66;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
    }
    
    hr {
        border-color: #00d9ff66;
    }
    
    .stButton > button {
        background-color: transparent;
        color: #00d9ff;
        border: 2px solid #00d9ff;
        font-weight: bold;
        text-transform: uppercase;
        box-shadow: 0 0 5px #00d9ff22;
    }
    .stButton > button:hover {
        background-color: #00d9ff11;
        border-color: #00ffff;
        box-shadow: 0 0 15px #00d9ff44;
    }
    
    [data-testid="stChatMessage"] {
        background-color: #0d1117;
        border: 1px solid #00d9ff44;
        border-radius: 8px;
    }
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        color: #aae0ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- PANEL LATERAL TÁCTICO (Sidebar) ---
with st.sidebar:
    st.markdown("### 🌐 N.O.V.A. // Núcleo")
    st.markdown("— *Interfaz Táctica* —")
    st.divider()
    
    # Módulo Reloj Táctico en Vivo
    ahora_local = datetime.now(CHILE_TZ)
    st.markdown(f"📅 **Fecha:** {ahora_local.strftime('%d/%m/%Y')}")
    st.markdown("⏰ **Hora Táctica (Local):**")
    
    reloj_html = """
    <div style="background-color: #0d1117; color: #00d9ff; font-family: 'Space Mono', monospace; padding: 10px; border-radius: 4px; border: 2px solid #00d9ff; text-align: center; margin-bottom: 10px; box-shadow: 0 0 10px #00d9ff33;">
        <div id="clock" style="font-size: 22px; font-weight: bold; color: #00d9ff; letter-spacing: 3px;">00:00:00</div>
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
    components.html(reloj_html, height=65)
    st.divider()

    # Módulo de Estado del Núcleo
    with st.expander("📊 Estado del Núcleo", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temp. Plasma", "1.2 MK", "+0.1")
        with col2:
            st.metric("Sincronía", "99.8%", "+0.01")
        st.caption("Estado: ESCUCHANDO (EN LÍNEA)")

    # Módulo Financiero
    with st.expander("📊 Mercados Globales (En Vivo)", expanded=False):
        try:
            url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,clp"
            response_crypto = requests.get(url_crypto, timeout=3)
            if response_crypto.status_code == 200:
                precios = response_crypto.json()
                st.metric("BTC", f"${precios.get('bitcoin', {}).get('usd', 0):,} USD")
                st.metric("ETH", f"${precios.get('ethereum', {}).get('usd', 0):,} USD")
                st.metric("USDT", f"${precios.get('tether', {}).get('clp', 0)} CLP")
            else:
                st.write("Cargando datos...")
        except Exception:
            st.write("Mercados: Fuera de línea")

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
        st.caption("Ubicación: Buin, Chile")
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=10, use_container_width=True, height=150)

    st.divider()
    
    # Módulo de Purga
    st.subheader("🧹 Bóveda")
    if st.button("Ejecutar Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- ÁREA PRINCIPAL ---
st.title("🌐 N.O.V.A. // Núcleo Táctico Cuántico")
st.markdown("— *Interfaz IA Avanzada • Protocolo Cyan Activado* —")

nucleo_plasma_html = """
<div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
    <svg viewBox="0 0 100 100" style="width: 250px; height: 250px;">
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
components.html(nucleo_plasma_html, height=260)

# --- ÁREA DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message and message["audio"]:
            st.audio(message["audio"], format="audio/mp3")

prompt = st.chat_input("Ingrese comando, consulta o instrucción táctica para N.O.V.A...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    puente.registrar_transmision("NOVA", prompt)

    with st.chat_message("assistant"):
        ahora = datetime.now(CHILE_TZ)
        hora_num = ahora.hour
        hora_actual_str = ahora.strftime("%H:%M:%S")
        fecha_actual_str = ahora.strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        # Saludo dinámico según la hora local
        if 5 <= hora_num < 12:
            saludo = "Buenos días"
        elif 12 <= hora_num < 20:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"
        
        if "hola" in p_lower:
            reply = f"{saludo}, Jefa. Son exactamente las {hora_actual_str} del {fecha_actual_str}. El reloj táctico y el núcleo de plasma están operando en perfecta sincronía. ¿Qué orden ejecutamos hoy?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Confirmado, Jefa: hoy es {fecha_actual_str} y la hora exacta en su ubicación es {hora_actual_str}."
        elif "bitcoin" in p_lower or "btc" in p_lower or "mercado" in p_lower:
            reply = "Accediendo a las métricas del mercado en tiempo real. Los paneles secundarios están disponibles a su izquierda."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "Enlace con J.A.R.V.I.S. activo. Reportan telemetría estable."
        elif "purga" in p_lower or "limpiar" in p_lower:
            reply = "Módulo de purga preparado. Puede ejecutar la limpieza desde el panel lateral."
        else:
            reply = f"Comando '{prompt}' recibido y en procesamiento, Jefa. Sistemas en alerta constante."
        
        st.markdown(reply)
        
        try:
            from gTTS import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
