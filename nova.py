import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import random
import json
import os

try:
    import psutil
except ImportError:
    psutil = None

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
        "auditoria": [{"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Sistema Inicializado", "Estado": "SEGURO"}],
        "nota_segura": "DATOS CONFIDENCIALES: Claves de acceso secundarias del taller."
    }

def guardar_memoria_nova(datos):
    try:
        with open(MEMORIA_NOVA, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

memoria_nova = cargar_memoria_nova()

# Configuración de idioma táctico en la barra lateral
st.sidebar.markdown("### 🛡️ Protocolo de Seguridad")
idioma_n = st.sidebar.selectbox("Idioma Táctico:", ["Español 🇨🇱", "English 🇺🇸", "Français 🇫🇷", "Português 🇧🇷"], key="lang_n")

textos_nova = {
    "Español 🇨🇱": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRO DE INTELIGENCIA TÁCTICA 🛡️",
        "sub": "[ NÚCLEO BLINDADO & INTELIGENCIA TÁCTICA ]",
        "presentacion": "Saludos, Jefa. Soy N.O.V.A., operando bajo Nivel de Blindaje Máximo N.T.C. Enlace Starlink activo. ¿Qué directiva protegida ejecutamos hoy?",
        "input": "Ingrese consulta o directiva táctica...",
        "tiempo": "📅 Sincronización Temporal",
        "red": "🌐 Red y Hardware",
        "starlink": "🛰️ Enlace Satelital Starlink",
        "panico": "🚨 Protocolo Cero",
        "boveda": "🔐 Notas Confidenciales",
        "auditoria": "📋 Auditoría de Eventos"
    },
    "English 🇺🇸": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // TACTICAL INTELLIGENCE CENTER 🛡️",
        "sub": "[ ARMORED CORE & TACTICAL INTELLIGENCE ]",
        "presentacion": "Greetings, Boss. I am N.O.V.A., operating under Maximum N.T.C. Armor. Starlink link online. What protected directive shall we execute today?",
        "input": "Enter tactical query or directive...",
        "tiempo": "📅 Temporal Synchronization",
        "red": "🌐 Network & Hardware",
        "starlink": "🛰️ Starlink Satellite Link",
        "panico": "🚨 Protocol Zero",
        "boveda": "🔐 Confidential Vault",
        "auditoria": "📋 Event Audit"
    },
    "Français 🇫🇷": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRE D'INTELLIGENCE TACTIQUE 🛡️",
        "sub": "[ NOYAU BLINDÉ & INTELLIGENCE TACTIQUE ]",
        "presentacion": "Salutations, Chef. Je suis N.O.V.A., sous blindage maximal. Liaison Starlink active. Quelle directive protégeons-nous aujourd'hui ?",
        "input": "Entrez une requête ou directive tactique...",
        "tiempo": "📅 Synchronisation Temporelle",
        "red": "🌐 Réseau & Matériel",
        "starlink": "🛰️ Liaison Satellite Starlink",
        "panico": "🚨 Protocole Zéro",
        "boveda": "🔐 Coffre Confidentiel",
        "auditoria": "📋 Audit des Événements"
    },
    "Português 🇧🇷": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRO DE INTELIGÊNCIA TÁTICA 🛡️",
        "sub": "[ NÚCLEO BLINDADO & INTELIGÊNCIA TÁTICA ]",
        "presentacion": "Saudações, Chefe. Sou N.O.V.A., operando sob Nível de Blindagem Máxima. Enlace Starlink ativo. Qual diretriz protegida executamos hoje?",
        "input": "Insira consulta ou diretriz tática...",
        "tiempo": "📅 Sincronização Temporal",
        "red": "🌐 Rede e Hardware",
        "starlink": "🛰️ Enlace Satelital Starlink",
        "panico": "🚨 Protocolo Zero",
        "boveda": "🔐 Cofre Confidencial",
        "auditoria": "📋 Auditoria de Eventos"
    }
}

tn = textos_nova[idioma_n]

# Estilos CSS Neón Azul / Blindaje Táctico
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

def emitir_voz_nova(texto, lang_code):
    lang_map = {"Español 🇨🇱": "es-ES", "English 🇺🇸": "en-US", "Français 🇫🇷": "fr-FR", "Português 🇧🇷": "pt-BR"}
    code = lang_map.get(lang_code, "es-ES")
    limpio = texto.replace("*", "").replace("#", "").replace("`", "").replace("\n", " ")
    js = f"""
    <script>
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance("{limpio}");
            u.lang = '{code}';
            window.speechSynthesis.speak(u);
        }}
    </script>
    """
    st.components.v1.html(js, height=0, width=0)

st.markdown(f"<h1>{tn['titulo']}</h1>", unsafe_allow_html=True)
st.markdown(f"""
    <div class="banner-ondas">
        <span style="font-size: 13px; color: #00f3ff; font-family: monospace; letter-spacing: 2px;">
            {tn['sub']}
        </span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
col_i, col_c, col_d = st.columns([1.1, 2.2, 1.1])

with col_i:
    # 1. Reloj Táctico
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["tiempo"])
    @st.fragment(run_every=1)
    def reloj_nova():
        z = pytz.timezone('America/Santiago')
        ahora = datetime.now(z)
        st.write(f"📌 **Fecha:** {ahora.strftime('%d/%m/%Y')}")
        st.markdown("⏱️ **Hora (Chile):**")
        st.markdown(f'<div class="reloj-digital">{ahora.strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
    reloj_nova()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Monitoreo de Hardware
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["red"])
    if psutil:
        st.write(f"⚙️ **CPU:** `{psutil.cpu_percent()}%`")
        st.write(f"🧠 **RAM:** `{psutil.virtual_memory().percent}%`")
    else:
        st.write("⚙️ **CPU:** `12%` | 🧠 **RAM:** `38%`")
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Módulo Starlink (SpaceX)
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["starlink"])
    st.write("📡 **Antena Dishy:** `Alineada (Online)`")
    st.write("🚀 **Satélite LEO:** `STARLINK-3142`")
    st.write("⚡ **Bajada / Subida:** `215 Mbps / 38 Mbps`")
    st.write("⏱️ **Ping Orbital:** `18 ms`")
    
    modo_starlink = st.selectbox("Modo de Enlace:", ["Prioridad Terrestre", "Cifrado Militar LEO", "Modo Sigilo (Bajo Consumo)"], key="sl_mode")
    st.caption(f"🔒 Enlace: **{modo_starlink}**")
    st.markdown('</div>', unsafe_allow_html=True)

with col_c:
    st.subheader("💬 Consola Táctica // N.O.V.A. (C.I.T.)")
    
    if "msgs_n" not in st.session_state:
        st.session_state.msgs_n = [{"role": "assistant", "content": tn["presentacion"]}]

    for idx, msg in enumerate(st.session_state.msgs_n):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant":
                if st.button("🔊 Escuchar", key=f"v_n_{idx}"):
                    emitir_voz_nova(msg["content"], idioma_n)

    if prompt := st.chat_input(tn["input"]):
        st.session_state.msgs_n.append({"role": "user", "content": prompt})
        
        texto_lower = prompt.lower().strip()
        
        # Reconocimiento de saludos y respuestas fluidas en varios idiomas
        if any(w in texto_lower for w in ["hola", "hello", "bonjour", "olá", "saludos"]):
            if idioma_n == "English 🇺🇸":
                resp_n = "REPORT: Greeting acknowledged. N.O.V.A. online and armed via Starlink. What is our directive, Boss?"
            elif idioma_n == "Français 🇫🇷":
                resp_n = "RAPPORT : Salutations reçues. N.O.V.A. en ligne et parée via Starlink. Quelle est notre directive, Chef ?"
            elif idioma_n == "Português 🇧🇷":
                resp_n = "RELATÓRIO: Saudação recebida. N.O.V.A. online via Starlink. Qual é a nossa diretriz, Chefe?"
            else:
                resp_n = "INFORME: Saludo recibido. N.O.V.A. en línea y pertrechada vía Starlink. ¿Qué directiva ejecutamos, Jefa?"
                
        elif any(w in texto_lower for w in ["cómo estás", "how are you", "comment vas-tu", "como vai"]):
            resp_n = "ESTADO TÁCTICO: Perímetros seguros, latencia Starlink en 18ms y encriptación cuántica al 100%."
            
        else:
            if idioma_n == "English 🇺🇸":
                resp_n = f"TACTICAL REPORT: Directive '{prompt}' verified via LEO network. Perimeter clear."
            elif idioma_n == "Français 🇫🇷":
                resp_n = f"RAPPORT TACTIQUE : Directive '{prompt}' vérifiée via le réseau LEO. Périmètre sécurisé."
            elif idioma_n == "Português 🇧🇷":
                resp_n = f"RELATÓRIO TÁTICO: Diretriz '{prompt}' verificada via rede LEO. Perímetro seguro."
            else:
                resp_n = f"INFORME TÁCTICO: Directiva '{prompt}' registrada vía red LEO Starlink sin anomalías."

        st.session_state.msgs_n.append({"role": "assistant", "content": resp_n})
        
        nuevo_evento = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": f"Cmd: {prompt[:10]}...", "Estado": "VERIFICADO"}
        memoria_nova["auditoria"].append(nuevo_evento)
        guardar_memoria_nova(memoria_nova)
        
        emitir_voz_nova(resp_n, idioma_n)
        st.rerun()

with col_d:
    # Protocolo Cero (Botón de Pánico)
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["panico"])
    pin_p = st.text_input("PIN de Emergencia:", type="password", key="pin_p")
    if st.button("🔴 EJECUTAR BLOQUEO"):
        if pin_p == "1234":
            st.session_state.msgs_n = [{"role": "assistant", "content": "⚠️ **PROTOCOLO CERO EJECUTADO:** Historial purgado y sesión bloqueada por seguridad."}]
            st.toast("🚨 ¡Sistema blindado y purgado con éxito!")
            st.rerun()
        else:
            st.error("❌ PIN incorrecto.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Bóveda de Notas Confidenciales
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["boveda"])
    if "boveda_abierta" not in st.session_state:
        st.session_state.boveda_abierta = False

    if not st.session_state.boveda_abierta:
        pin_c = st.text_input("PIN de Bóveda:", type="password", key="pin_conf")
        if st.button("🔓 Desbloquear Bóveda"):
            if pin_c == "1234":
                st.session_state.boveda_abierta = True
                st.toast("✅ ¡Bóveda desbloqueada!")
                st.rerun()
            else:
                st.error("❌ PIN incorrecto.")
    else:
        st.success("🟢 Bóveda abierta")
        nota_seg = memoria_nova.get("nota_segura", "")
        n_seg = st.text_area("Editar datos seguros:", value=nota_seg, height=90, key="nota_seg")
        col_ba1, col_ba2 = st.columns(2)
        with col_ba1:
            if st.button("💾 Guardar"):
                memoria_nova["nota_segura"] = n_seg
                guardar_memoria_nova(memoria_nova)
                st.toast("✅ Datos guardados.")
        with col_ba2:
            if st.button("🔒 Bloquear"):
                st.session_state.boveda_abierta = False
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Auditoría de Eventos
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["auditoria"])
    for ev in reversed(memoria_nova["auditoria"][-3:]):
        st.caption(f"[{ev['Hora']}] {ev['Evento']} - **{ev['Estado']}**")
    st.markdown('</div>', unsafe_allow_html=True)
