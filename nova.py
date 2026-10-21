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
        "nota_segura": "DATOS CONFIDENCIALES: Claves de acceso."
    }

def guardar_memoria_nova(datos):
    try:
        with open(MEMORIA_NOVA, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        pass

memoria_nova = cargar_memoria_nova()

st.sidebar.markdown("### 🛡️ Secure Protocol")
idioma_n = st.sidebar.selectbox("Tactical Language:", ["Español 🇨🇱", "English 🇺🇸", "Français 🇫🇷", "Português 🇧🇷"], key="lang_n")

textos_nova = {
    "Español 🇨🇱": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRO DE INTELIGENCIA TÁCTICA 🛡️",
        "sub": "[ NÚCLEO BLINDADO & INTELIGENCIA TÁCTICA ]",
        "presentacion": "Saludos, Jefa. N.O.V.A. operativa bajo Nivel de Blindaje Máximo. ¿Qué directiva protegida ejecutamos?",
        "input": "Ingrese consulta o directiva táctica...",
        "tiempo": "📅 Sincronización Temporal",
        "red": "🌐 Red y Hardware",
        "panico": "🚨 Protocolo Cero",
        "boveda": "🔐 Notas Confidenciales",
        "auditoria": "📋 Auditoría de Eventos"
    },
    "English 🇺🇸": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // TACTICAL INTELLIGENCE CENTER 🛡️",
        "sub": "[ ARMORED CORE & TACTICAL INTELLIGENCE ]",
        "presentacion": "Greetings, Boss. N.O.V.A. active under Maximum Armor Level. What protected directive shall we execute?",
        "input": "Enter tactical query or directive...",
        "tiempo": "📅 Temporal Synchronization",
        "red": "🌐 Network & Hardware",
        "panico": "🚨 Protocol Zero",
        "boveda": "🔐 Confidential Vault",
        "auditoria": "📋 Event Audit"
    },
    "Français 🇫🇷": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRE D'INTELLIGENCE TACTIQUE 🛡️",
        "sub": "[ NOYAU BLINDÉ & INTELLIGENCE TACTIQUE ]",
        "presentacion": "Salutations, Chef. N.O.V.A. active sous blindage maximal. Quelle directive protégeons-nous ?",
        "input": "Entrez une requête tactique...",
        "tiempo": "📅 Synchronisation Temporelle",
        "red": "🌐 Réseau & Matériel",
        "panico": "🚨 Protocole Zéro",
        "boveda": "🔐 Coffre Confidentiel",
        "auditoria": "📋 Audit des Événements"
    },
    "Português 🇧🇷": {
        "titulo": "🛡️ N.O.V.A (C.I.T) // CENTRO DE INTELIGÊNCIA TÁTICA 🛡️",
        "sub": "[ NÚCLEO BLINDADO & INTELIGÊNCIA TÁTICA ]",
        "presentacion": "Saudações, Chefe. N.O.V.A. ativa sob Nível de Blindagem Máxima. Qual diretriz protegida executamos?",
        "input": "Insira consulta ou diretriz tática...",
        "tiempo": "📅 Sincronização Temporal",
        "red": "🌐 Rede e Hardware",
        "panico": "🚨 Protocolo Zero",
        "boveda": "🔐 Cofre Confidencial",
        "auditoria": "📋 Auditoria de Eventos"
    }
}

tn = textos_nova[idioma_n]

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
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["tiempo"])
    @st.fragment(run_every=1)
    def reloj_nova():
        z = pytz.timezone('America/Santiago')
        ahora = datetime.now(z)
        st.write(f"📌 **Fecha:** {ahora.strftime('%d/%m/%Y')}")
        st.markdown("⏱️ **Hora:**")
        st.markdown(f'<div class="reloj-digital">{ahora.strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
    reloj_nova()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["red"])
    st.write("🛰️ **Cloud:** `Online` | ⚡ **Lat:** `18ms`")
    if psutil:
        st.write(f"⚙️ **CPU:** `{psutil.cpu_percent()}%` | 🧠 **RAM:** `{psutil.virtual_memory().percent}%`")
    st.markdown('</div>', unsafe_allow_html=True)

with col_c:
    st.subheader("💬 Consola Táctica // N.O.V.A.")
    
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
        
        if idioma_n == "English 🇺🇸":
            resp_n = f"TACTICAL REPORT: Directive '{prompt}' verified. Perimeter secure."
        elif idioma_n == "Français 🇫🇷":
            resp_n = f"RAPPORT TACTIQUE : Directive '{prompt}' vérifiée. Périmètre sécurisé."
        elif idioma_n == "Português 🇧🇷":
            resp_n = f"RELATÓRIO TÁTICO: Diretriz '{prompt}' verificada. Perímetro seguro."
        else:
            resp_n = f"INFORME TÁCTICO: Directiva '{prompt}' verificada. Perímetro seguro."

        st.session_state.msgs_n.append({"role": "assistant", "content": resp_n})
        
        nuevo_evento = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": f"Cmd: {prompt[:10]}...", "Estado": "OK"}
        memoria_nova["auditoria"].append(nuevo_evento)
        guardar_memoria_nova(memoria_nova)
        
        emitir_voz_nova(resp_n, idioma_n)
        st.rerun()

with col_d:
    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["panico"])
    pin_p = st.text_input("PIN:", type="password", key="pin_p")
    if st.button("🔴 LOCKDOWN"):
        if pin_p == "1234":
            st.session_state.msgs_n = [{"role": "assistant", "content": "⚠️ PROTOCOL ZERO EXECUTED."}]
            st.rerun()
        else:
            st.error("Error")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["boveda"])
    if "bov" not in st.session_state: st.session_state.bov = False
    if not st.session_state.bov:
        pin_c = st.text_input("PIN Vault:", type="password", key="pin_c")
        if st.button("🔓 Unlock"):
            if pin_c == "1234": st.session_state.bov = True; st.rerun()
    else:
        st.success("Vault Open")
        nota_seg = st.text_area("Secure data:", value=memoria_nova.get("nota_segura",""), key="ns")
        if st.button("💾 Save"):
            memoria_nova["nota_segura"] = nota_seg
            guardar_memoria_nova(memoria_nova)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-tactica">', unsafe_allow_html=True)
    st.subheader(tn["auditoria"])
    for ev in reversed(memoria_nova["auditoria"][-3:]):
        st.caption(f"[{ev['Hora']}] {ev['Evento']}")
    st.markdown('</div>', unsafe_allow_html=True)
