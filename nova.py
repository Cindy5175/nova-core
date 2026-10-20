import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import random
import json
import os

st.set_page_config(
    page_title="Centro de Mando - N.O.V.A. (C.I.T.)",
    page_icon="🛡️",
    layout="wide"
)

MEMORIA_NOVA = "memoria_nova.json"

def cargar_memoria_nova():
    if os.path.exists(MEMORIA_NOVA):
        try:
            with open(MEMORIA_NOVA, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "auditoria": [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Sistema Blindado Inicializado", "Estado": "SEGURO"}],
        "nota_segura": "Bitácora protegida de N.O.V.A."
    }

def guardar_memoria_nova(datos):
    try:
        with open(MEMORIA_NOVA, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

memoria_nova = cargar_memoria_nova()

REPORTE_NOVA = (
    "🛡️ **PROTOCOLO N.O.V.A. (C.I.T.) ACTIVADO** 🛡️\n\n"
    "Saludos, Jefa. Soy N.O.V.A. (Centro de Inteligencia Táctica), "
    "operando bajo **Nivel de Blindaje Máximo N.T.C.** Encriptación cuántica activa "
    "y monitoreo de seguridad operativo. ¿Qué directiva protegida ejecutamos hoy?"
)

# Estilos CSS Neón Azul / Blindaje
st.markdown("""
    <style>
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    h1 {
        text-align: center !important;
        color: #00f3ff !important;
        text-shadow: 0px 0px 12px rgba(0, 243, 255, 0.8);
        font-size: 28px !important;
        width: 100% !important;
        display: block !important;
    }
    h3 {
        color: #00f3ff !important;
        text-shadow: 0px 0px 8px rgba(0, 243, 255, 0.6);
        margin-top: 0px !important;
    }
    p, span, label, div, markdown, .stMarkdown {
        color: #80f9ff !important;
    }
    .card-tactica {
        background-color: #000a12 !important;
        border: 1px solid #00f3ff !important;
        border-radius: 10px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        box-shadow: 0px 0px 10px rgba(0, 243, 255, 0.3) !important;
    }
    .reloj-digital {
        background-color: #000000 !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        border-radius: 6px !important;
        box-shadow: 0px 0px 8px rgba(0, 243, 255, 0.4) !important;
        font-size: 20px !important;
        padding: 4px 10px !important;
        font-family: monospace;
        display: inline-block;
    }
    div[data-testid="stChatMessage"] {
        background-color: #000a12 !important;
        border: 1px solid #00f3ff !important;
        border-radius: 8px !important;
        box-shadow: 0px 0px 6px rgba(0, 243, 255, 0.3);
        margin-bottom: 10px;
    }
    div[data-testid="stChatMessage"] * {
        color: #00f3ff !important;
    }
    .banner-ondas {
        width: 100%;
        height: 60px;
        background: linear-gradient(90deg, #000000 0%, #031525 50%, #000000 100%);
        border: 1px solid #00f3ff;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 0px 15px rgba(0, 243, 255, 0.4);
        margin-bottom: 20px;
        text-align: center;
    }
    .stButton>button {
        background-color: #000a12 !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        border-radius: 6px;
        box-shadow: 0px 0px 6px rgba(0, 243, 255, 0.4);
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00f3ff !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

def emitir_voz_nova(texto):
    limpio = texto.replace("*", "").replace("#", "").replace("`", "").replace("\n", " ")
    js = f"""
    <script>
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{limpio}");
            u.lang = 'es-ES';
            window.speechSynthesis.speak(u);
        }}
    </script>
    """
    st.components.v1.html(js, height=0, width=0)

st.markdown("<h1>🛡️ N.O.V.A (C.I.T) // CENTRO DE INTELIGENCIA TÁCTICA 🛡️</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class="banner-ondas">
        <span style="font-size: 13px; color: #00f3ff; font-family: monospace; letter-spacing: 2px;">
            [ NÚCLEO BLINDADO & CENTRO DE INTELIGENCIA TÁCTICA ]
        </span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
col_i, col_c, col_d = st.columns([1.1, 2.2, 1.1])

with col_i:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📅 Sincronización Temporal")
    @st.fragment(run_every=1)
    def reloj_nova():
        z = pytz.timezone('America/Santiago')
        ahora = datetime.now(z)
        st.write(f"📌 **Fecha:** {ahora.strftime('%d/%m/%Y')}")
        st.markdown("⏱️ **Hora (Chile):**")
        st.markdown(f'<div class="reloj-digital">{ahora.strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
    reloj_nova()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🔒 Estado del Blindaje")
    st.success("🟢 100% Seguro")
    st.write("• Encriptación cuántica activa")
    st.markdown('</div>', unsafe_allow_html=True)

with col_c:
    st.subheader("💬 Consola Táctica // N.O.V.A. (C.I.T.)")
    
    if "msgs_n" not in st.session_state:
        st.session_state.msgs_n = [{"role": "assistant", "content": REPORTE_NOVA}]

    for idx, msg in enumerate(st.session_state.msgs_n):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant":
                if st.button("🔊 Escuchar", key=f"v_n_{idx}"):
                    emitir_voz_nova(msg["content"])

    if prompt := st.chat_input("Ingrese consulta o directiva táctica..."):
        st.session_state.msgs_n.append({"role": "user", "content": prompt})
        respuestas_n = [
            "Perímetro seguro y parámetros verificados sin anomalías.",
            "Encriptación de canal activa al 100%. Directiva procesada.",
            "Informe recibido y registrado bajo estrictos estándares de seguridad."
        ]
        resp_n = random.choice(respuestas_n)
        st.session_state.msgs_n.append({"role": "assistant", "content": resp_n})
        
        # Guardar en auditoría
        nuevo_evento = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": f"Consulta: {prompt[:12]}...", "Estado": "REGISTRADO"}
        memoria_nova["auditoria"].append(nuevo_evento)
        guardar_memoria_nova(memoria_nova)
        
        emitir_voz_nova(resp_n)
        st.rerun()

with col_d:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📋 Registro de Auditoría")
    for ev in reversed(memoria_nova["auditoria"][-4:]):
        st.caption(f"[{ev['Hora']}] {ev['Evento']} - **{ev['Estado']}**")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🛰️ Monitoreo Satelital")
    mapa = pd.DataFrame({'lat': [-33.7333], 'lon': [-70.7417]})
    st.map(mapa, zoom=10, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
