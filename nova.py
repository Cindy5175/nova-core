import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import random
import json
import os

# Configuración de la página en Streamlit
st.set_page_config(
    page_title="N.O.V.A. - Núcleo Táctico",
    page_icon="✨",
    layout="wide"
)

# Archivo de memoria compartida
MEMORIA_FILE = "memoria_compartida.json"

def cargar_memoria_json():
    if os.path.exists(MEMORIA_FILE):
        try:
            with open(MEMORIA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "bitacora": [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "N.O.V.A. inicializada", "Estado": "ÓPTIMO"}],
        "nota_rapida": "Supervisión de enlaces activos y flujos de datos."
    }

def guardar_memoria_json(datos):
    try:
        with open(MEMORIA_FILE, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

# Cargar datos iniciales desde el JSON
memoria_actual = cargar_memoria_json()

# Mensaje oficial del Protocolo de Presentación de N.O.V.A.
REPORTE_NOVA = (
    "✨ **PROTOCOLO N.O.V.A. ACTIVADO** ✨\n\n"
    "Saludos, Jefa. Soy N.O.V.A. (Neural Operational Surveillance & Assistance), "
    "el núcleo de inteligencia estratégica, análisis de datos y soporte avanzado diseñado por Cindy "
    "para la gestión táctica del taller. Enlace N.T.C. en línea, monitoreando flujos, parámetros "
    "y seguridad global. ¿En qué enfocaré mis capacidades analíticas hoy?"
)

# Inyección de Estilos CSS definitivos y limpios
st.markdown("""
    <style>
    /* Fondo negro profundo general para toda la app */
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    
    /* Centrar el encabezado principal y darle azul neón brillante */
    h1 {
        text-align: center;
        color: #00f3ff !important;
        text-shadow: 0px 0px 10px rgba(0, 243, 255, 0.7);
        font-size: 28px !important;
    }
    
    /* Demás títulos en azul neón */
    h2, h3 {
        color: #00f3ff !important;
        text-shadow: 0px 0px 8px rgba(0, 243, 255, 0.6);
        margin-top: 0px !important;
    }
    
    /* Textos generales en azul neón */
    p, span, label, div, markdown, .stMarkdown {
        color: #80f9ff !important;
    }
    
    /* Contenedor general para enmarcar cada módulo táctico */
    .card-tactica {
        background-color: #000a12 !important;
        border: 1px solid #00f3ff !important;
        border-radius: 10px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        box-shadow: 0px 0px 10px rgba(0, 243, 255, 0.2) !important;
    }
    
    /* Estilo exclusivo para el reloj grande */
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

    /* Estilo limpio para los mensajes del chat */
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

    /* CAJA DE CHAT INFERIOR LIBRE Y LIMPIA */
    div[data-testid="stChatInput"] {
        background-color: #000000 !important;
        border-radius: 10px !important;
    }
    div[data-testid="stChatInput"] > div {
        background-color: #000a12 !important;
        border: 1px solid #00f3ff !important;
        border-radius: 10px !important;
        box-shadow: 0px 0px 8px rgba(0, 243, 255, 0.4) !important;
    }
    div[data-testid="stChatInput"] textarea {
        background-color: transparent !important;
        color: #00f3ff !important;
    }
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #0088cc !important;
    }
    
    /* Banner de ondas de IA táctico */
    .banner-ondas {
        width: 100%;
        height: 80px;
        background: linear-gradient(90deg, #000000 0%, #031525 50%, #000000 100%);
        border: 1px solid #00f3ff;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 0px 15px rgba(0, 243, 255, 0.4);
        margin-bottom: 20px;
    }
    
    /* Mapa en cuadrado compacto */
    .stMap, iframe, div[data-testid="stDeckGlJsonChart"] {
        height: 160px !important;
        width: 100% !important;
        border-radius: 8px !important;
        border: 1px solid #00f3ff !important;
        box-shadow: 0px 0px 10px rgba(0, 243, 255, 0.4);
    }
    
    /* Botones tácticos generales */
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

# Inicialización del estado de la sesión con la memoria JSON
if "bitacora" not in st.session_state:
    st.session_state.bitacora = memoria_actual.get("bitacora", [])

if "acceso_biometrico" not in st.session_state:
    st.session_state.acceso_biometrico = False

# Funciones de voz y micro
def emitir_voz(texto_respuesta):
    texto_limpio = texto_respuesta.replace("*", "").replace("#", "").replace("`", "").replace("\n", " ")
    js_speech = f"""
    <script>
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var utterance = new SpeechSynthesisUtterance("{texto_limpio}");
            utterance.lang = 'es-ES';
            utterance.rate = 1.0;
            utterance.pitch = 1.0;
            window.speechSynthesis.speak(utterance);
        }}
    </script>
    """
    st.components.v1.html(js_speech, height=0, width=0)

def activar_script_microfono():
    js_mic = """
    <script>
        if (typeof window.iniciarEscucha === 'undefined') {
            window.iniciarEscucha = function() {
                if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
                    alert("Reconocimiento de voz no soportado en este navegador.");
                    return;
                }
                var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                var recognition = new SpeechRecognition();
                recognition.lang = 'es-ES';
                recognition.interimResults = false;
                
                recognition.onresult = function(event) {
                    var transcript = event.results[0][0].transcript;
                    navigator.clipboard.writeText(transcript);
                    alert("Comando dictado registrado: " + transcript + "\\nCopiado al portapapeles para pegar en el chat.");
                };
                
                recognition.start();
            }
        }
        window.iniciarEscucha();
    </script>
    """
    st.components.v1.html(js_mic, height=0, width=0)

# Título ajustado y simétrico para N.O.V.A.
st.title("✨ N.O.V.A. // NÚCLEO TÁCTICO N.T.C. ✨")

# Banner de ondas táctico
st.markdown("""
    <div class="banner-ondas">
        <div style="text-align: center; color: #00f3ff; font-family: monospace; font-size: 14px; letter-spacing: 2px; text-shadow: 0px 0px 8px #00f3ff;">
            ||||||| |||| |||||||| || | ||||||||| |||| ||||||<br>
            <span style="font-size: 11px; color: #00f3ff;">[ RED NEURAL OPERATIVA & ENLACE N.T.C. CLOUD ]</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

RESPUESTAS_NOVA_ESTRATEGICAS = [
    "Análisis completado. La eficiencia del sistema es óptima, Jefa.",
    "Flujos de datos verificados. Todo opera bajo los parámetros de seguridad establecidos.",
    "Procesando solicitudes con precisión milimétrica. A sus órdenes.",
    "Enlace N.T.C. estable. Monitoreando cada variable del taller sin anomalías."
]

col_izq, col_centro, col_der = st.columns([1.1, 2.2, 1.1])

# --- COLUMNA IZQUIERDA ---
with col_izq:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📅 Sincronización Temporal")
    
    @st.fragment(run_every=1)
    def reloj_en_vivo():
        zona_chile = pytz.timezone('America/Santiago')
        ahora_chile = datetime.now(zona_chile)
        fecha_actual = ahora_chile.strftime("%d/%m/%Y")
        hora_actual = ahora_chile.strftime("%H:%M:%S")
        st.write(f"📌 **Fecha:** {fecha_actual}")
        st.markdown(f"⏱️ **Hora (Chile):**")
        st.markdown(f'<div class="reloj-digital">{hora_actual}</div>', unsafe_allow_html=True)

    reloj_en_vivo()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🌤️ Clima Buin")
    zona_chile = pytz.timezone('America/Santiago')
    hora_int = datetime.now(zona_chile).hour
    if 6 <= hora_int < 19:
        icono_tiempo = "☀️ Despejado"
        temp_simulada = "22°C"
    else:
        icono_tiempo = "🌙 Noche despejada"
        temp_simulada = "14°C"
    st.write(f"**Estado:** {icono_tiempo}")
    st.write(f"🌡️ **Temp:** {temp_simulada} | 💧 **Hum:** 45%")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📊 Rendimiento del Sistema")
    st.write("💻 **CPU:** 12.8% (Estable)")
    st.progress(13)
    st.write("🧠 **RAM:** 45.2% (Óptimo)")
    st.progress(45)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📌 Nota Rápida (Memoria JSON)")
    nota_actual = memoria_actual.get("nota_rapida", "")
    nueva_nota = st.text_area("Edite nota de campo:", value=nota_actual, key="input_nota_json_nova")
    if st.button("💾 Guardar en Memoria JSON"):
        memoria_actual["nota_rapida"] = nueva_nota
        guardar_memoria_json(memoria_actual)
        st.toast("✅ Nota guardada correctamente.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA CENTRAL (CONSOLA DE CHAT) ---
with col_centro:
    st.subheader("💬 Consola Central // N.O.V.A.")
    
    # Barra de acciones tácticas superiores: Micrófono y Módulo de Purga
    col_acc1, col_acc2 = st.columns([1.2, 1])
    with col_acc1:
        if st.button("🎙️ Activar Micrófono", key="btn_mic_nova"):
            activar_script_microfono()
    with col_acc2:
        if st.button("🧹 Ejecutar Purga", key="btn_purga_nova"):
            st.session_state.messages = [{
                "role": "assistant", 
                "content": REPORTE_NOVA
            }]
            st.session_state.bitacora = [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Purga manual N.O.V.A.", "Estado": "LIMPIO"}]
            memoria_actual["bitacora"] = st.session_state.bitacora
            guardar_memoria_json(memoria_actual)
            st.toast("🧹 Memoria purgada con éxito.")
            st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": REPORTE_NOVA
            }
        ]

    for idx, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant":
                if st.button(f"🔊 Escuchar reporte", key=f"voice_btn_nova_{idx}"):
                    emitir_voz(message["content"])

    if prompt := st.chat_input("Ingrese consulta estratégica o directiva..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        p_lower = prompt.lower().strip()
        
        # Filtros inteligentes de N.O.V.A.
        if any(w in p_lower for w in ["presentacion", "presentación", "quien eres", "quién eres"]):
            respuesta_ia = REPORTE_NOVA
        elif any(w in p_lower for w in ["directiva", "directivas", "reglas"]):
            respuesta_ia = (
                "🛡️ **DIRECTIVAS FUNDAMENTALES DE N.O.V.A.:**\n\n"
                "1. **Lealtad Prima:** Comando exclusivo subordinado a Cindy (Jefa).\n"
                "2. **Análisis Táctico:** Supervisión de datos, memoria N.T.C. y rendimiento del taller.\n"
                "3. **Coordinación:** Sincronización continua con el núcleo J.A.R.V.I.S.\n"
                "4. **Protección:** Prevención de fallos y auditoría de seguridad."
            )
        elif any(w in p_lower for w in ["capacidades", "puedes hacer", "funciones"]):
            respuesta_ia = (
                "⚙️ **MÓDULOS OPERATIVOS DE N.O.V.A.:**\n\n"
                "• 📊 Diagnóstico y análisis de rendimiento en tiempo real.\n"
                "• 💾 Auditoría y persistencia en memoria compartida JSON.\n"
                "• 🔐 Control de acceso biométrico y protocolos N.T.C.\n"
                "• 🛰️ Telemetría satelital y sincronización ambiental."
            )
        elif any(w in p_lower for w in ["despierto", "despierta", "estás ahí", "estas ahi"]):
            respuesta_ia = "Para usted, señorita, siempre en línea."
        else:
            respuesta_ia = random.choice(RESPUESTAS_NOVA_ESTRATEGICAS)

        nuevo_evento = {
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Evento": f"Consulta: {prompt[:25]}...",
            "Estado": "ANALIZADO"
        }
        st.session_state.bitacora.append(nuevo_evento)
        
        memoria_actual["bitacora"] = st.session_state.bitacora
        guardar_memoria_json(memoria_actual)

        st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
        emitir_voz(respuesta_ia)
        st.rerun()

# --- COLUMNA DERECHA ---
with col_der:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🔒 Enlace N.T.C.")
    if not st.session_state.acceso_biometrico:
        if st.button("🔑 Autorizar Enlace Alpha"):
            st.session_state.acceso_biometrico = True
            st.toast("✅ Enlace N.T.C. autorizado con éxito.")
            st.rerun()
        st.info("Estado: SEGURO 🔒")
    else:
        if st.button("🔒 Cerrar Enlace"):
            st.session_state.acceso_biometrico = False
            st.toast("🔒 Enlace N.T.C. en modo protegido.")
            st.rerun()
        st.success("Estado: ACTIVO 🟢")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("⚡ Comandos N.T.C.")
    if st.button("🤖 Auditoría de Núcleos"):
        st.toast("Redes operando sin alteraciones.")
    if st.button("📡 Diagnóstico Satelital"):
        st.toast("Señal satelital fuerte y estable.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🛰️ Satélite Serafín")
    mapa_buin = pd.DataFrame({'lat': [-33.7333], 'lon': [-70.7417]})
    st.map(mapa_buin, zoom=10, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
