import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import random
import json
import os

# Configuración de la página en Streamlit
st.set_page_config(
    page_title="Centro de Conocimiento - J.A.R.V.I.S. & N.O.V.A.",
    page_icon="🧠",
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
        "bitacora": [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Base de Conocimiento Inicializada", "Estado": "ÓPTIMO"}],
        "nota_rapida": "Sincronización total de núcleos y bases de datos activa.",
        "biblioteca_tecnica": "1. Python/Streamlit: Usar st.fragment para relojes en vivo.\n2. GitHub: Mantener sincronizados los repositorios de cloud.\n3. Seguridad: Validar claves maestras antes de abrir consola.",
        "financiero_fintual": "1. Objetivos a mediano plazo.\n2. Revisión de rentabilidad de fondos mutuos.\n3. Educación financiera y diversificación sin activos digitales.",
        "productividad_tareas": "1. Mantener limpio el espacio de trabajo.\n2. Optimizar almacenamiento en dispositivos móviles.\n3. Monitoreo constante de rendimiento de red."
    }

def guardar_memoria_json(datos):
    try:
        with open(MEMORIA_FILE, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

memoria_actual = cargar_memoria_json()

# Mensajes oficiales de presentación
REPORTE_JARVIS = (
    "⚡ **PROTOCOLO DE CONOCIMIENTO ACTIVADO** ⚡\n\n"
    "Saludos, Jefa. J.A.R.V.I.S. en línea con acceso total a la Base de Conocimiento N.T.C. "
    "Biblioteca técnica, finanzas tradicionales y flujos de productividad sincronizados. ¿Qué consulta o análisis técnico realizamos hoy?"
)

REPORTE_NOVA = (
    "🛡️ **NÚCLEO DE INTELIGENCIA TÁCTICA ACTIVO** 🛡️\n\n"
    "Saludos, Jefa. N.O.V.A. operando con la Base de Conocimiento encriptada. "
    "Parámetros de seguridad, manuales y registros de eficiencia listos para su despliegue. ¿Qué directiva procesamos?"
)

# Inyección de Estilos CSS
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

# Estados de sesión
if "bitacora" not in st.session_state:
    st.session_state.bitacora = memoria_actual.get("bitacora", [])

if "sistema_blindado" not in st.session_state:
    st.session_state.sistema_blindado = False

# Funciones multimedia
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

# Selector Maestro de Núcleo en la Barra Lateral
st.sidebar.title("🧠 Centro de Inteligencia")
nucleo_activo = st.sidebar.radio("Seleccione Operador:", ["⚡ J.A.R.V.I.S. AI", "🛡️ N.O.V.A. Blindada"])

st.sidebar.markdown("---")
st.sidebar.subheader("📚 Base de Conocimiento")
seccion_conocimiento = st.sidebar.selectbox("Consultar Módulo:", ["Panel Principal", "1. Biblioteca Técnica", "2. Finanzas & Fintual", "3. Productividad & Tareas"])

if "nucleo_previo" not in st.session_state:
    st.session_state.nucleo_previo = nucleo_activo

if st.session_state.nucleo_previo != nucleo_activo:
    st.session_state.nucleo_previo = nucleo_activo
    if "⚡ J.A.R.V.I.S." in nucleo_activo:
        st.session_state.messages = [{"role": "assistant", "content": REPORTE_JARVIS}]
    else:
        st.session_state.messages = [{"role": "assistant", "content": REPORTE_NOVA}]
    st.rerun()

# Título y Banner dinámicos
if "⚡ J.A.R.V.I.S." in nucleo_activo:
    st.title("⚡ J.A.R.V.I.S. // CENTRO DE CONOCIMIENTO ⚡")
    banner_texto = "[ NÚCLEO NEURAL & BASE DE DATOS TÉCNICA ]"
    respuestas_rand = [
        "Consultando los registros del taller. Todo está bajo control, Jefa.",
        "Información procesada y validada con éxito en la base de datos.",
        "Conocimiento al servicio del taller. ¿Qué otra duda resolvemos?"
    ]
else:
    st.title("🛡️ N.O.V.A. // BASE DE INTELIGENCIA N.T.C. 🛡️")
    banner_texto = "[ ARCHIVO TÁCTICO & PROTOCOLOS DE EFICIENCIA ]"
    respuestas_rand = [
        "Parámetros verificados en los manuales de seguridad.",
        "Base de datos táctica sincronizada y protegida.",
        "Análisis de registros completado sin anomalías."
    ]

st.markdown(f"""
    <div class="banner-ondas">
        <div style="text-align: center; color: #00f3ff; font-family: monospace; font-size: 14px; letter-spacing: 2px; text-shadow: 0px 0px 8px #00f3ff;">
            ||||||| |||| |||||||| || | ||||||||| |||| ||||||<br>
            <span style="font-size: 11px; color: #00f3ff;">{banner_texto}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- VISTA CONDICIONAL SEGÚN SECCIÓN DE CONOCIMIENTO ---
if seccion_conocimiento == "1. Biblioteca Técnica":
    st.subheader("🛠️ Módulo 1: Biblioteca Técnica del Taller")
    st.markdown("Edite y consulte los manuales y referencias rápidas guardadas en la memoria JSON del taller:")
    bib_actual = memoria_actual.get("biblioteca_tecnica", "")
    nueva_bib = st.text_area("Editar Biblioteca Técnica:", value=bib_actual, height=200, key="txt_bib")
    if st.button("💾 Guardar Biblioteca Técnica"):
        memoria_actual["biblioteca_tecnica"] = nueva_bib
        guardar_memoria_json(memoria_actual)
        st.toast("✅ Biblioteca técnica actualizada en la nube.")

elif seccion_conocimiento == "2. Finanzas & Fintual":
    st.subheader("📊 Módulo 2: Centro Financiero & Fintual")
    st.markdown("Gestión de fondos mutuos, proyecciones e inversión tradicional (sin activos digitales):")
    fin_actual = memoria_actual.get("financiero_fintual", "")
    nuevo_fin = st.text_area("Editar Registros Financieros:", value=fin_actual, height=200, key="txt_fin")
    if st.button("💾 Guardar Registros Financieros"):
        memoria_actual["financiero_fintual"] = nuevo_fin
        guardar_memoria_json(memoria_actual)
        st.toast("✅ Registros financieros actualizados.")

elif seccion_conocimiento == "3. Productividad & Tareas":
    st.subheader("📋 Módulo 3: Eficiencia y Productividad")
    st.markdown("Organización de flujos de trabajo, metas y tareas del taller:")
    prod_actual = memoria_actual.get("productividad_tareas", "")
    nuevo_prod = st.text_area("Editar Productividad y Tareas:", value=prod_actual, height=200, key="txt_prod")
    if st.button("💾 Guardar Productividad"):
        memoria_actual["productividad_tareas"] = nuevo_prod
        guardar_memoria_json(memoria_actual)
        st.toast("✅ Módulo de productividad actualizado.")

else:
    # --- PANEL PRINCIPAL (CONSOLA DE CHAT Y WIDGETS) ---
    col_izq, col_centro, col_der = st.columns([1.1, 2.2, 1.1])

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
        st.subheader("🧠 Estado del Conocimiento")
        st.write("📚 **Biblioteca:** Sincronizada")
        st.write("📊 **Finanzas:** Activas (Fintual)")
        st.write("📋 **Tareas:** Óptimas")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_centro:
        st.subheader(f"💬 Consola de Consulta // {nucleo_activo}")
        
        col_acc1, col_acc2 = st.columns([1.2, 1])
        with col_acc1:
            if st.button("🎙️ Activar Micrófono", key="btn_mic_conocimiento"):
                activar_script_microfono()
        with col_acc2:
            if st.button("🧹 Ejecutar Purga", key="btn_purga_conocimiento"):
                reporte_inicial = REPORTE_JARVIS if "⚡ J.A.R.V.I.S." in nucleo_activo else REPORTE_NOVA
                st.session_state.messages = [{"role": "assistant", "content": reporte_inicial}]
                st.session_state.bitacora = [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Purga de consola", "Estado": "LIMPIO"}]
                memoria_actual["bitacora"] = st.session_state.bitacora
                guardar_memoria_json(memoria_actual)
                st.toast("🧹 Memoria purgada con éxito.")
                st.rerun()

        if "messages" not in st.session_state:
            reporte_inicial = REPORTE_JARVIS if "⚡ J.A.R.V.I.S." in nucleo_activo else REPORTE_NOVA
            st.session_state.messages = [{"role": "assistant", "content": reporte_inicial}]

        for idx, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    if st.button(f"🔊 Escuchar", key=f"voice_btn_con_{idx}"):
                        emitir_voz(message["content"])

        if prompt := st.chat_input("Consulte la base de conocimiento o ingrese directiva..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            p_lower = prompt.lower().strip()
            
            if "biblioteca" in p_lower or "técnica" in p_lower or "manual" in p_lower:
                respuesta_ia = f"📖 **Biblioteca Técnica del Taller:**\n\n{memoria_actual.get('biblioteca_tecnica', 'Sin registros.')}"
            elif "finanza" in p_lower or "fintual" in p_lower or "inversión" in p_lower:
                respuesta_ia = f"📊 **Centro Financiero & Fintual:**\n\n{memoria_actual.get('financiero_fintual', 'Sin registros.')}"
            elif "tarea" in p_lower or "productividad" in p_lower or "método" in p_lower:
                respuesta_ia = f"📋 **Productividad y Tareas:**\n\n{memoria_actual.get('productividad_tareas', 'Sin registros.')}"
            elif any(w in p_lower for w in ["presentacion", "presentación", "quien eres", "quién eres"]):
                respuesta_ia = REPORTE_JARVIS if "⚡ J.A.R.V.I.S." in nucleo_activo else REPORTE_NOVA
            else:
                respuesta_ia = random.choice(respuestas_rand)

            nuevo_evento = {
                "Hora": datetime.now().strftime("%H:%M:%S"),
                "Evento": f"Consulta de conocimiento: {prompt[:20]}...",
                "Estado": "CONSULTADO"
            }
            st.session_state.bitacora.append(nuevo_evento)
            memoria_actual["bitacora"] = st.session_state.bitacora
            guardar_memoria_json(memoria_actual)

            st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
            emitir_voz(respuesta_ia)
            st.rerun()

    with col_der:
        st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
        st.subheader("🔒 Estado de Seguridad")
        st.success("🟢 Base de Datos Segura")
        st.write("• Encriptación JSON activa.")
        st.write("• Cero criptomonedas (Finanzas tradicionales).")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
        st.subheader("🛰️ Satélite Serafín")
        mapa_buin = pd.DataFrame({'lat': [-33.7333], 'lon': [-70.7417]})
        st.map(mapa_buin, zoom=10, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
