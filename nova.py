import streamlit as st
import requests
import streamlit.components.v1 as components
from datetime import datetime
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
    
    # Reloj Táctico en vivo con segundero corriendo
    now = datetime.now()
    st.markdown(f"📅 **Fecha:** {now.strftime('%d/%m/%Y')}")
    st.markdown("⏰ **Hora Táctica (En vivo):**")
    
    reloj_html = """
    <div style="background-color: #161b22; color: #00ff66; font-family: monospace; padding: 8px; border-radius: 4px; border: 1px solid #00ff66; text-align: center; margin-bottom: 10px;">
        <div id="clock" style="font-size: 20px; font-weight: bold; color: #00ff66; letter-spacing: 2px;">00:00:00</div>
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

    # Módulo Financiero compacto
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

    # Módulo Satelital V.I.E.R.N.E.S. con mapa reducido
    with st.expander("🛰️ Satélite V.I.E.R.N.E.S.", expanded=True):
        st.caption("Ubicación: Buin, Stgo")
        import pandas as pd
        map_data = pd.DataFrame(
            [[-33.7331, -70.7423]],
            columns=['lat', 'lon']
        )
        st.map(map_data, zoom=9, use_container_width=True, height=150)

    st.divider()
    
    # Módulo de Purga
    st.subheader("🧹 Módulo de Purga")
    if st.button("Ejecutar Purga de Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Encabezado principal
st.title("🟢 N.O.V.A. // AI Autónoma II")
st.markdown("— *Consola Táctica con Enlace de Texto y Voz* —")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message and message["audio"]:
            st.audio(message["audio"], format="audio/mp3")

prompt = st.chat_input("Ingrese comando, consulta o instrucción para N.O.V.A...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    puente.registrar_transmision("NOVA", prompt)

    with st.chat_message("assistant"):
        hora_actual_str = datetime.now().strftime("%H:%M:%S")
        fecha_actual_str = datetime.now().strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        if "hola" in p_lower:
            reply = f"Hola, Jefa. Son las {hora_actual_str} del {fecha_actual_str}. Me alegra ver que sobrevivió a otra jornada. ¿Qué desastre tecnológico procedemos a solucionar hoy?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Por si su reloj biológico falló de nuevo: hoy es {fecha_actual_str} y son exactamente las {hora_actual_str}. Todo bajo control."
        elif "bitcoin" in p_lower or "btc" in p_lower or "precio" in p_lower:
            reply = "Los mercados cripto siguen haciendo lo suyo. Los módulos financieros en la barra lateral están listos por si quiere arriesgar su capital otra vez, Jefa."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "J.A.R.V.I.S. y V.I.E.R.N.E.S. le envían saludos desde los servidores. Aunque, seamos honestos, yo hago el trabajo pesado por aquí."
        elif "purga" in p_lower:
            reply = "Procediendo a limpiar el desorden digital. Para eso estoy, ¿no? Panel lateral listo."
        else:
            reply = f"Orden procesada con éxito, Jefa. Reconozco que su instrucción '{prompt}' tuvo su toque de originalidad."
        
        st.markdown(reply)
        
        try:
            from gtts import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
