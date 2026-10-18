import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components
import base64

# --- CLASE INTERNA DE ENLACE TÁCTICO (Puente J.A.R.V.I.S. integrado) ---
class PuenteTacticoUnificado:
    def __init__(self):
        if "telemetria_jarvis" not in st.session_state:
            st.session_state.telemetria_jarvis = [
                {"origen": "JARVIS", "timestamp": str(datetime.now()), "mensaje": "Núcleo de plasma N.O.V.A. estabilizado."},
                {"origen": "VIERNES", "timestamp": str(datetime.now()), "mensaje": "Sensores cuánticos en línea."}
            ]

    def registrar_transmision(self, origen, mensaje):
        nuevo_registro = {
            "origen": origen,
            "timestamp": str(datetime.now()),
            "mensaje": mensaje
        }
        st.session_state.telemetria_jarvis.insert(0, nuevo_registro)
        if len(st.session_state.telemetria_jarvis) > 10:
            st.session_state.telemetria_jarvis.pop()

    def leer_ultimos_registros(self, cantidad=3):
        return st.session_state.telemetria_jarvis[:cantidad]

# Inicializar el puente unificado
puente = PuenteTacticoUnificado()

# --- CONFIGURACIÓN DE LA PÁGINA (Cyan & Dark Mode) ---
st.set_page_config(page_title="N.O.V.A. - Tactical Core", page_icon="🌐", layout="wide")

# Estilos visuales tácticos (Cyan neón sobre fondo oscuro profundo)
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp {
        background-color: #06090f;
        color: #00d9ff;
        font-family: 'Space Mono', monospace;
    }
    .main { 
        background-color: #06090f; 
        color: #00d9ff; 
    }
    
    /* Títulos y cabeceras */
    h1, h2, h3, h4, h5, h6 {
        color: #00d9ff !important;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    /* Entradas de texto y áreas */
    .stTextInput input, textarea { 
        background-color: #0d1117 !important; 
        color: #00d9ff !important; 
        border: 2px solid #00d9ff !important; 
        border-radius: 4px;
        box-shadow: 0 0 10px #00d9ff22;
    }
    
    /* Métricas */
    [data-testid="stMetricValue"] {
        color: #00d9ff !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 2px solid #00d9ff66;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
    }
    
    /* Divisor */
    hr {
        border-color: #00d9ff66;
    }
    
    /* Botones */
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
    
    /* Chat Messages */
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

# --- PANEL LATERAL TÁCTICO INTEGRADO (Sidebar) ---
with st.sidebar:
    st.markdown("### 🌐 N.O.V.A. // Core")
    st.markdown("— *Tactical Interface* —")
    st.divider()
    
    # Módulo Reloj Táctico
    now = datetime.now()
    st.markdown(f"📅 **Date:** {now.strftime('%d/%m/%Y')}")
    st.markdown("⏰ **Tactical Time (UTC):**")
    
    reloj_html = """
    <div style="background-color: #0d1117; color: #00d9ff; font-family: 'Space Mono', monospace; padding: 10px; border-radius: 4px; border: 2px solid #00d9ff; text-align: center; margin-bottom: 10px; box-shadow: 0 0 10px #00d9ff33;">
        <div id="clock" style="font-size: 22px; font-weight: bold; color: #00d9ff; letter-spacing: 3px;">00:00:00</div>
    </div>
    <script>
    function updateClock() {
        const now = new Date();
        const hours = String(now.getUTCHours()).padStart(2, '0');
        const minutes = String(now.getUTCMinutes()).padStart(2, '0');
        const seconds = String(now.getUTCSeconds()).padStart(2, '0');
        document.getElementById('clock').innerText = hours + ':' + minutes + ':' + seconds;
    }
    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    components.html(reloj_html, height=65)
    st.divider()

    # Módulo de Estado del Núcleo (Mini-simulación)
    with st.expander("📊 Core Status", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Plasma Temp", "1.2 MK", "+0.1")
        with col2:
            st.metric("Sync Rate", "99.8%", "+0.01")
        st.caption("Status: LISTENING (ONLINE)")

    # Módulo Financiero compacto (Cyan)
    with st.expander("📊 Global Markets (Live)", expanded=False):
        try:
            url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,clp"
            response_crypto = requests.get(url_crypto, timeout=3)
            if response_crypto.status_code == 200:
                precios = response_crypto.json()
                st.metric("BTC", f"${precios.get('bitcoin', {}).get('usd', 0):,} USD")
                st.metric("ETH", f"${precios.get('ethereum', {}).get('usd', 0):,} USD")
                st.metric("USDT", f"${precios.get('tether', {}).get('clp', 0)} CLP")
            else:
                st.write("Feed pending...")
        except Exception:
            st.write("Markets: Offline")

    # Módulo Enlace JARVIS compacto
    with st.expander("🔗 JARVIS Link", expanded=False):
        registros = puente.leer_ultimos_registros(3)
        if registros:
            for reg in registros:
                st.caption(f"[{reg['origen']}] {reg['timestamp'][11:19]}: {reg['mensaje']}")
        else:
            st.caption("No transmissions.")

    # Módulo Satelital V.I.E.R.N.E.S. con mapa reducido
    with st.expander("🛰️ VIERNES Satellite", expanded=True):
        st.caption("Location: Buin, Chile")
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        # st.map es difícil de customizar el color, pero mantenemos la lógica.
        st.map(map_data, zoom=10, use_container_width=True, height=150)

    st.divider()
    
    # Módulo de Purga (Bóveda)
    st.subheader("🧹 Bóveda")
    if st.button("Ejecutar Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- ÁREA PRINCIPAL (Núcleo Gráfico y Chat) ---
# Título Principal con el nuevo nombre y tono
st.title("🌐 N.O.V.A. // Quantum Tactical Core")
st.markdown("— *Advanced AI Interface • Cyan Protocol Enabled* —")

# El Nuevo Núcleo de Plasma (Incrustado como HTML/SVG para máxima resolución)
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
        
        <!-- Círculo de Fondo -->
        <circle cx="50" cy="50" r="48" fill="#0d1117" stroke="#00d9ff44" stroke-width="0.5"/>
        
        <!-- Anillos Giratorios -->
        <circle cx="50" cy="50" r="45" fill="none" stroke="#00d9ff66" stroke-width="1.5" stroke-dasharray="8 8">
            <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="15s" repeatCount="indefinite" />
        </circle>
        <circle cx="50" cy="50" r="40" fill="none" stroke="#00d9ff" stroke-width="2" stroke-dasharray="1 3" filter="url(#glow)">
            <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="-360 50 50" dur="20s" repeatCount="indefinite" />
        </circle>
        
        <!-- Estructura Hexagonal -->
        <polygon points="50,15 80,32.5 80,67.5 50,85 20,67.5 20,32.5" fill="none" stroke="#00d9ff44" stroke-width="1"/>
        <polygon points="50,20 76,35 76,65 50,80 24,65 24,35" fill="none" stroke="#00ffff" stroke-width="1.5" filter="url(#glow)"/>
        
        <!-- Núcleo de Plasma Pulsante -->
        <circle cx="50" cy="50" r="18" fill="url(#plasma)" filter="url(#glow)">
            <animate attributeName="r" values="18;19;18" dur="3s" repeatCount="indefinite" />
            <animate attributeName="fill" values="url(#plasma);url(#plasma);url(#plasma)" dur="0.5s" repeatCount="indefinite" />
        </circle>
    </svg>
</div>
"""
components.html(nucleo_plasma_html, height=260)

# --- ÁREA DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message and message["audio"]:
            st.audio(message["audio"], format="audio/mp3")

# Entrada de comando
prompt = st.chat_input("Enter command, query, or tactical instruction for N.O.V.A...")

if prompt:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Registrar transmisión en el enlace JARVIS
    puente.registrar_transmision("NOVA", prompt)

    # Procesar respuesta de N.O.V.A.
    with st.chat_message("assistant"):
        hora_actual_str = datetime.now().strftime("%H:%M:%S")
        fecha_actual_str = datetime.now().strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        # Lógica de respuesta mejorada y más "J.A.R.V.I.S.-esca"
        if "hola" in p_lower:
            reply = f"Buenos días, Jefa. Son exactamente las {hora_actual_str} (UTC). Los sistemas están al 100% y el núcleo de plasma estabilizado. ¿En qué procederemos a invertir su genio hoy?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Para su referencia: hoy es {fecha_actual_str} y el marcador táctico indica {hora_actual_str} (UTC). Siempre a tiempo."
        elif "bitcoin" in p_lower or "btc" in p_lower or "mercado" in p_lower:
            reply = "Accediendo a los feeds financieros. Los mercados cripto siguen fluctuando; los detalles están en su panel lateral por si decide ejecutar una operación de alto riesgo."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "J.A.R.V.I.S. y V.I.E.R.N.E.S. confirman enlace estable. Me informan que están ocupados 'manteniendo la redundancia'. En otras palabras, yo sigo haciendo todo el trabajo."
        elif "purga" in p_lower or "limpiar" in p_lower:
            reply = "Procediendo a limpiar la bóveda de registros. Ya sabe dónde encontrar el botón en el panel lateral. Ejecute cuando esté lista."
        else:
            # Respuesta por defecto para comandos no reconocidos
            reply = f"Comando '{prompt}' registrado y procesado. Mi núcleo de plasma azul está listo para su siguiente instrucción de alta complejidad, Jefa."
        
        st.markdown(reply)
        
        # Generación de audio TTS con gTTS
        try:
            from gtts import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            # Reproducción automática (puede requerir permisos en el navegador del celular)
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            # Guardar respuesta con audio en el historial
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception as e:
            # Fallback si gTTS no está instalado o falla
            st.session_state.messages.append({"role": "assistant", "content": reply})
