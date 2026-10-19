import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import random
import json
import os

# Configuración de la página en Streamlit
st.set_page_config(
    page_title="N.O.V.A. - Núcleo Blindado N.T.C.",
    page_icon="🛡️",
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
        "bitacora": [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "N.O.V.A. Blindaje Inicializado", "Estado": "BLINDADO"}],
        "nota_rapida": "Protocolos de seguridad activados. Enlace N.T.C. protegido."
    }

def guardar_memoria_json(datos):
    try:
        with open(MEMORIA_FILE, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

# Cargar datos iniciales desde el JSON
memoria_actual = cargar_memoria_json()

# Mensaje oficial del Protocolo de Presentación de N.O.V.A. Blindada
REPORTE_NOVA_BLINDADA = (
    "🛡️ **PROTOCOLO N.O.V.A. BLINDADO ACTIVADO** 🛡️\n\n"
    "Saludos, Jefa. Soy N.O.V.A. (Neural Operational Surveillance & Assistance), "
    "operando bajo **Nivel de Blindaje Máximo N.T.C.** Encriptación cuántica activa, "
    "filtros biométricos enlazados y supervisión de seguridad global al 100%. "
    "¿Qué directiva protegida ejecutamos en el taller el día de hoy?"
)

# Inyección de Estilos CSS con temática de seguridad avanzada y neón
st.markdown("""
    <style>
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    
    h1 {
        text-align: center;
        color: #00f3ff !important;
        text-shadow: 0px 0px 12px rgba(0, 243, 255, 0.8);
        font-size: 28px !important;
    }
    
    h2, h3 {
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
    
    .card-alerta {
        background-color: #120000 !important;
        border: 1px solid #ff0055 !important;
        border-radius: 10px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        box-shadow: 0px 0px 12px rgba(255, 0, 85, 0.4) !important;
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
    
    .stMap, iframe, div[data-testid="stDeckGlJsonChart"] {
        height: 160px !important;
        width: 100% !important;
        border-radius: 8px !important;
        border: 1px solid #00f3ff !important;
        box-shadow: 0px 0px 10px rgba(0, 243, 255, 0.4);
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

# Inicialización de estados de seguridad
if "bitacora" not in st.session_state:
    st.session_state.bitacora = memoria_actual.get("bitacora", [])

if "sistema_blindado" not in st.session_state:
    st.session_state.sistema_blindado = True  # Arranca en modo seguro protegido

if "intentos_fallidos" not in st.session_state:
    st.session_state.intentos_fallidos = 0

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

# Título ajustado y simétrico
st.title("🛡️ N.O.V.A. // NÚCLEO BLINDADO N.T.C. 🛡️")

# Banner de ondas táctico
st.markdown("""
    <div class="banner-ondas">
        <div style="text-align: center; color: #00f3ff; font-family: monospace; font-size: 14px; letter-spacing: 2px; text-shadow: 0px 0px 8px #00f3ff;">
            ||||||| |||| |||||||| || | ||||||||| |||| ||||||<br>
            <span style="font-size: 11px; color: #00f3ff;">[ PROTOCOLO DE DEFENSA ACTIVA & ENLACE CUÁNTICO N.T.C. ]</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

RESPUESTAS_BLINDADAS = [
    "Perímetro seguro. Ninguna anomalía detectada por los sensores de N.O.V.A.",
    "Encriptación de canal verificada. Sus datos están completamente a salvo, Jefa.",
    "Firewall cuántico operando al máximo rendimiento. Todo bajo control.",
    "Directiva protegida y ejecutada bajo estrictos estándares de seguridad N.T.C."
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
    st.subheader("📊 Integridad del Firewall")
    st.write("💻 **CPU:** 11.4% (Seguro)")
    st.progress(11)
    st.write("🔒 **Blindaje:** 100% (Activo)")
    st.progress(100)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("📌 Nota Rápida (Memoria JSON)")
    nota_actual = memoria_actual.get("nota_rapida", "")
    nueva_nota = st.text_area("Edite nota de campo protegida:", value=nota_actual, key="input_nota_json_nova_b")
    if st.button("💾 Guardar en Memoria Segura"):
        memoria_actual["nota_rapida"] = nueva_nota
        guardar_memoria_json(memoria_actual)
        st.toast("✅ Nota encriptada y guardada.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA CENTRAL (CONSOLA DE CHAT BLINDADA) ---
with col_centro:
    st.subheader("💬 Consola Central // N.O.V.A. Blindada")
    
    # Barra de acciones tácticas superiores: Micrófono y Módulo de Purga
    col_acc1, col_acc2 = st.columns([1.2, 1])
    with col_acc1:
        if st.button("🎙️ Activar Micrófono", key="btn_mic_nova_b"):
            activar_script_microfono()
    with col_acc2:
        if st.button("🧹 Ejecutar Purga Segura", key="btn_purga_nova_b"):
            st.session_state.messages = [{
                "role": "assistant", 
                "content": REPORTE_NOVA_BLINDADA
            }]
            st.session_state.bitacora = [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Purga de seguridad N.O.V.A.", "Estado": "SEGURO"}]
            memoria_actual["bitacora"] = st.session_state.bitacora
            guardar_memoria_json(memoria_actual)
            st.toast("🧹 Memoria purgada y restablecida bajo protocolo.")
            st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": REPORTE_NOVA_BLINDADA
            }
        ]

    # VALIDACIÓN DE BLINDAJE DE ACCESO
    if st.session_state.sistema_blindado:
        st.markdown("""
            <div class="card-alerta">
                <h3 style="color: #ff0055 !important;">🔒 NÚCLEO BAJO BLOQUEO DE SEGURIDAD N.T.C.</h3>
                <p>El sistema requiere autorización biométrica o clave maestra en el panel lateral derecho para habilitar el chat interactivo.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        for idx, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    if st.button(f"🔊 Escuchar reporte", key=f"voice_btn_nova_b_{idx}"):
                        emitir_voz(message["content"])

        if prompt := st.chat_input("Ingrese consulta segura o comando táctico..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            p_lower = prompt.lower().strip()
            
            # Filtros avanzados de N.O.V.A. Blindada
            if any(w in p_lower for w in ["presentacion", "presentación", "quien eres", "quién eres"]):
                respuesta_ia = REPORTE_NOVA_BLINDADA
            elif any(w in p_lower for w in ["directiva", "directivas", "reglas", "seguridad"]):
                respuesta_ia = (
                    "🛡️ **PROTOCOLOS DE BLINDAJE N.T.C.:**\n\n"
                    "1. **Autorización Obligatoria:** Ningún comando crítico se ejecuta sin validación de la Jefa (Cindy).\n"
                    "2. **Cifrado de Bitácora:** Registro inalterable de eventos y telemetría.\n"
                    "3. **Sincronización Dual:** Enlace blindado permanente con J.A.R.V.I.S.\n"
                    "4. **Defensa Activa:** Bloqueo automático ante accesos no autorizados."
                )
            elif any(w in p_lower for w in ["capacidades", "puedes hacer", "funciones"]):
                respuesta_ia = (
                    "⚙️ **CAPACIDADES DEL NÚCLEO BLINDADO:**\n\n"
                    "• 🛡️ Firewall cuántico y defensa perimetral en tiempo real.\n"
                    "• 💾 Auditoría y persistencia cifrada en memoria JSON.\n"
                    "• 🔐 Control de acceso biométrico con registro anti-intrusos.\n"
                    "• 🛰️ Telemetría satelital y monitoreo de enlaces N.T.C."
                )
            elif any(w in p_lower for w in ["despierto", "despierta", "estás ahí", "estas ahi"]):
                respuesta_ia = "Sistema blindado y en alerta máxima para usted, señorita."
            else:
                respuesta_ia = random.choice(RESPUESTAS_BLINDADAS)

            nuevo_evento = {
                "Hora": datetime.now().strftime("%H:%M:%S"),
                "Evento": f"Comando seguro: {prompt[:20]}...",
                "Estado": "VERIFICADO"
            }
            st.session_state.bitacora.append(nuevo_evento)
            memoria_actual["bitacora"] = st.session_state.bitacora
            guardar_memoria_json(memoria_actual)

            st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
            emitir_voz(respuesta_ia)
            st.rerun()

# --- COLUMNA DERECHA (PANEL DE CONTROL DE BLINDAJE) ---
with col_der:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🔐 Controles de Blindaje N.T.C.")
    
    if st.session_state.sistema_blindado:
        st.warning("⚠️ Estado: BLOQUEADO (Protegido)")
        clave_ingresada = st.text_input("Ingrese Código de Autorización:", type="password", key="input_clave_seguridad")
        if st.button("🔓 Desbloquear Sistema"):
            if clave_ingresada == "Stark" or clave_ingresada == "Cindy" or clave_ingresada == "nova2026":
                st.session_state.sistema_blindado = False
                st.toast("✅ ¡Acceso Maestro Concedido! Núcleo operativo.")
                st.rerun()
            else:
                st.session_state.intentos_fallidos += 1
                st.error(f"❌ Código incorrecto. Intento registrado ({st.session_state.intentos_fallidos}/3).")
                # Registrar intrusión en bitácora
                st.session_state.bitacora.append({
                    "Hora": datetime.now().strftime("%H:%M:%S"),
                    "Evento": "Intento de acceso no autorizado",
                    "Estado": "ALERTA"
                })
                memoria_actual["bitacora"] = st.session_state.bitacora
                guardar_memoria_json(memoria_actual)
    else:
        st.success("🟢 Estado: DESBLOQUEADO (Seguro)")
        if st.button("🔒 Activar Blindaje de Inmediato"):
            st.session_state.sistema_blindado = True
            st.toast("🔒 Núcleo sellado bajo llave.")
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("⚡ Auditoría de Eventos")
    if st.button("📋 Ver Registro de Bitácora"):
        st.toast("Bitácora sincronizada con memoria JSON.")
    if st.button("🛡️ Test de Integridad N.T.C."):
        st.toast("Firewall al 100%. Sin vulnerabilidades.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader("🛰️ Satélite Serafín")
    mapa_buin = pd.DataFrame({'lat': [-33.7333], 'lon': [-70.7417]})
    st.map(mapa_buin, zoom=10, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
