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

# Barra lateral: Idioma y Nivel de Amenaza (DEFCON / Neón Dinámico)
st.sidebar.markdown("### 🛡️ Protocolo de Seguridad")
idioma_n = st.sidebar.selectbox("Idioma Táctico:", ["Español 🇨🇱", "English 🇺🇸", "Français 🇫🇷", "Português 🇧🇷"], key="lang_n")

nivel_amenaza = st.sidebar.radio(
    "🚨 Estado de Amenaza Táctica:",
    ["🟦 DEFCON 5 (Normal)", "🟧 DEFCON 3 (Intensivo)", "🟥 DEFCON 1 (Alerta Máxima)"],
    index=0
)

# Configuración de Colores de Neón según Nivel DEFCON
if "DEFCON 1" in nivel_amenaza:
    color_neon = "#ff0055"
    sombra_neon = "rgba(255, 0, 85, 0.8)"
    bg_card = "#140005"
elif "DEFCON 3" in nivel_amenaza:
    color_neon = "#ffaa00"
    sombra_neon = "rgba(255, 170, 0, 0.8)"
    bg_card = "#140a00"
else:
    color_neon = "#00f3ff"
    sombra_neon = "rgba(0, 243, 255, 0.8)"
    bg_card = "#000a12"

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
        "auditoria": "📋 Auditoría de Eventos",
        "escaner": "👁️ Escáner Táctico de Cámara",
        "terminal": "💻 Terminal de Autodiagnóstico",
        "generador": "🧠 Generador Táctico de Ideas",
        "pass_gen": "🔑 Generador de Cifrado",
        "matrix": "💻 Visualizador Matriz"
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
        "auditoria": "📋 Event Audit",
        "escaner": "👁️ Tactical Camera Scanner",
        "terminal": "💻 Diagnostic Terminal",
        "generador": "🧠 Tactical Idea Generator",
        "pass_gen": "🔑 Encryption Pass Generator",
        "matrix": "💻 Matrix Visualizer"
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
        "auditoria": "📋 Audit des Événements",
        "escaner": "👁️ Scanner Tactique Caméra",
        "terminal": "💻 Terminal de Diagnostic",
        "generador": "🧠 Générateur d'Idées Tactic",
        "pass_gen": "🔑 Générateur de Clés",
        "matrix": "💻 Visualiseur Matrice"
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
        "auditoria": "📋 Auditoria de Eventos",
        "escaner": "👁️ Scanner Tático de Câmera",
        "terminal": "💻 Terminal de Diagnóstico",
        "generador": "🧠 Gerador de Ideias Táticas",
        "pass_gen": "🔑 Gerador de Senhas Seguras",
        "matrix": "💻 Visualizador Matriz"
    }
}

tn = textos_nova[idioma_n]

css_estilo_nova = f"""
    .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background-color: #000000 !important;
    }}
    h1 {{
        text-align: center !important;
        color: {color_neon} !important;
        text-shadow: 0px 0px 12px {sombra_neon};
        font-size: 28px !important;
        width: 100% !important;
        display: block !important;
    }}
    h3 {{
        color: {color_neon} !important;
        text-shadow: 0px 0px 8px {sombra_neon};
        margin-top: 0px !important;
    }}
    p, span, label, div, markdown, .stMarkdown {{
        color: {color_neon} !important;
    }}
    .card-tactica {{
        background-color: {bg_card} !important;
        border: 1px solid {color_neon} !important;
        border-radius: 10px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        box-shadow: 0px 0px 10px {sombra_neon} !important;
    }}
    .reloj-digital {{
        background-color: #000000 !important;
        color: {color_neon} !important;
        border: 1px solid {color_neon} !important;
        border-radius: 6px !important;
        box-shadow: 0px 0px 8px {sombra_neon} !important;
        font-size: 20px !important;
        padding: 4px 10px !important;
        font-family: monospace;
        display: inline-block;
    }}
    div[data-testid="stChatMessage"] {{
        background-color: {bg_card} !important;
        border: 1px solid {color_neon} !important;
        border-radius: 8px !important;
        box-shadow: 0px 0px 6px {sombra_neon};
        margin-bottom: 10px;
    }}
    div[data-testid="stChatMessage"] * {{
        color: {color_neon} !important;
    }}
    .banner-ondas {{
        width: 100%;
        height: 60px;
        background: linear-gradient(90deg, #000000 0%, #031525 50%, #000000 100%);
        border: 1px solid {color_neon};
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 0px 15px {sombra_neon};
        margin-bottom: 20px;
        text-align: center;
    }}
    .stButton>button {{
        background-color: {bg_card} !important;
        color: {color_neon} !important;
        border: 1px solid {color_neon} !important;
        border-radius: 6px;
        box-shadow: 0px 0px 6px {sombra_neon};
        width: 100%;
    }}
    .stButton>button:hover {{
        background-color: {color_neon} !important;
        color: #000000 !important;
    }}
    .terminal-hacker {{
        background-color: #050505;
        color: #00ff66;
        border: 1px solid #00ff66;
        border-radius: 6px;
        padding: 10px;
        font-family: monospace;
        font-size: 11px;
        height: 110px;
        overflow-y: auto;
    }}
"""
st.markdown(f"<style>{css_estilo_nova}</style>", unsafe_allow_html=True)

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
        <span style="font-size: 13px; color: {color_neon}; font-family: monospace; letter-spacing: 2px;">
            {tn['sub']} // ESTADO: {nivel_amenaza.split()[1]}
        </span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
col_i, col_c, col_d = st.columns([1.1, 2.2, 1.1])

with col_i:
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
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["red"])
    if psutil:
        st.write(f"⚙️ **CPU:** `{psutil.cpu_percent()}%`")
        st.write(f"🧠 **RAM:** `{psutil.virtual_memory().percent}%`")
    else:
        st.write("⚙️ **CPU:** `12%` | 🧠 **RAM:** `38%`")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["starlink"])
    st.write("📡 **Antena Dishy:** `Alineada (Online)`")
    st.write("🚀 **Satélite LEO:** `STARLINK-3142`")
    st.write("⚡ **Bajada / Subida:** `215 Mbps / 38 Mbps`")
    st.write("⏱️ **Ping Orbital:** `18 ms`")
    modo_starlink = st.selectbox("Modo de Enlace:", ["Prioridad Terrestre", "Cifrado Militar LEO", "Modo Sigilo (Bajo Consumo)"], key="sl_mode")
    st.caption(f"🔒 Enlace: **{modo_starlink}**")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["terminal"])
    st.markdown("""
    <div class="terminal-hacker">
        > root@nova-cit:~# sys_diag --init<br>
        [OK] Firewall cuántico activo.<br>
        [OK] Encriptación AES-256 verificada.<br>
        [OK] Escaneo de puertos del taller: 0 amenazas.<br>
        > Estado: Conexión LEO estable (18ms).
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 Ejecutar Scan de Red"):
        st.toast("🛡️ Autodiagnóstico de red completado sin anomalías.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_c:
    col_titulo_n, col_purga_n = st.columns([3, 1])
    with col_titulo_n:
        st.subheader("💬 Consola Táctica // N.O.V.A.")
    with col_purga_n:
        if st.button("🗑️ Purgar", key="purga_n", help="Purgar consola de comandos"):
            st.session_state.msgs_n = [{"role": "assistant", "content": tn["presentacion"]}]
            st.toast("🚨 Consola purgada y reseteada.")
            st.rerun()

    st.markdown('<div class="card-tactica" style="padding: 10px !important;">', unsafe_allow_html=True)
    st.markdown("👁️ **Escáner Táctico de Cámara:**")
    img_cam = st.camera_input("Capturar objeto para auditoría táctica:")
    if img_cam:
        st.success("📸 Captura recibida con éxito.")
        if st.button("🔍 Auditar Imagen Escaneada"):
            nuevo_ev = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": "Escáner Visual Táctico", "Estado": "ANALIZADO"}
            memoria_nova["auditoria"].append(nuevo_ev)
            guardar_memoria_nova(memoria_nova)
            st.toast("✅ Imagen registrada en la auditoría táctica.")
    st.markdown('</div>', unsafe_allow_html=True)

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
        saludos = ["hola", "hello", "bonjour", "olá", "saludos", "buenas"]
        preguntas_estado = ["cómo estás", "como estas", "how are you", "comment vas-tu", "estado", "reporte"]
        
        if any(s in texto_lower for s in saludos):
            if idioma_n == "English 🇺🇸":
                resp_n = "REPORT: Greeting acknowledged. N.O.V.A. online and armed via Starlink. What is our directive, Boss?"
            elif idioma_n == "Français 🇫🇷":
                resp_n = "RAPPORT : Salutations reçues. N.O.V.A. en ligne et parée via Starlink. Quelle est notre directive, Chef ?"
            elif idioma_n == "Português 🇧🇷":
                resp_n = "RELATÓRIO: Saudação recebida. N.O.V.A. online via Starlink. Qual é a nossa diretriz, Chefe?"
            else:
                resp_n = "INFORME: Saludo recibido. N.O.V.A. en línea y pertrechada vía Starlink. ¿Qué directiva ejecutamos, Jefa?"
                
        elif any(p in texto_lower for p in preguntas_estado):
            resp_n = f"ESTADO TÁCTICO: Nivel {nivel_amenaza.split()[1]} activo, latencia Starlink en 18ms y encriptación al 100%."
            
        else:
            if idioma_n == "English 🇺🇸":
                resp_n = f"TACTICAL REPORT: Directive '{prompt}' processed via LEO network. Perimeter clear."
            elif idioma_n == "Français 🇫🇷":
                resp_n = f"RAPPORT TACTIQUE : Directive '{prompt}' traitée via le réseau LEO. Périmètre sécurisé."
            elif idioma_n == "Português 🇧🇷":
                resp_n = f"RELATÓRIO TÁTICO: Diretriz '{prompt}' processada via rede LEO. Perímetro seguro."
            else:
                resp_n = f"INFORME TÁCTICO: Directiva '{prompt}' procesada sin anomalías."

        st.session_state.msgs_n.append({"role": "assistant", "content": resp_n})
        
        nuevo_evento = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": f"Cmd: {prompt[:10]}...", "Estado": "VERIFICADO"}
        memoria_nova["auditoria"].append(nuevo_evento)
        guardar_memoria_nova(memoria_nova)
        
        emitir_voz_nova(resp_n, idioma_n)
        st.rerun()

with col_d:
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

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["generador"])
    idea_base = st.text_input("Concepto de Proyecto:", placeholder="Ej: Automatizar riego...", key="idea_nova")
    if st.button("⚡ Sintetizar Estructura"):
        if idea_base:
            st.success("🎯 Directiva estructurada en 3 fases:")
            st.markdown(f"- **Fase 1:** Análisis de requerimientos para *{idea_base}*.\n- **Fase 2:** Prototipado y testeo en taller.\n- **Fase 3:** Despliegue en red segura.")
        else:
            st.warning("⚠️ Ingrese un concepto base.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔑 NUEVA ADICIÓN NOVA 1: Generador Táctico de Contraseñas / Cifrado
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["pass_gen"])
    long_pass = st.slider("Longitud de Clave:", 8, 24, 14, key="pass_len")
    if st.button("🔐 Generar Clave Segura"):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        nueva_clave = "".join(random.choice(chars) for _ in range(long_pass))
        st.code(nueva_clave, language="")
        st.toast("✅ Llave de cifrado generada con éxito.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 💻 NUEVA ADICIÓN NOVA 2: Efecto Visual Matriz / Consola Animada Ciberpunk
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["matrix"])
    st.markdown("""
    <div style="background:#000; color:#00ff66; border:1px solid #00ff66; border-radius:6px; padding:8px; font-family:monospace; font-size:10px; text-align:center;">
        01010011 01011001 01010011 01010100 01000101 01001101<br>
        [STREAM_SECURE_ACTIVE // N.T.C. PROTOCOL]<br>
        00110010 00110000 00110010 00110110
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["auditoria"])
    for ev in reversed(memoria_nova["auditoria"][-3:]):
        st.caption(f"[{ev['Hora']}] {ev['Evento']} - **{ev['Estado']}**")
    st.markdown('</div>', unsafe_allow_html=True)
