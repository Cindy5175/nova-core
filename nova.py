import base64
import urllib.parse
from gtts import gTTS
import streamlit as st

# Configuración de la página para NOVA
st.set_page_config(
    page_title="Stark Core - C.I.T", page_icon="🟣", layout="centered"
)

# Estilos CSS (Forzando el magenta neón en toda la interfaz)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .console-title {
        color: #ff007f;
        font-family: monospace;
        font-size: 16px;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: 1.5px;
    }
    /* Forzar que los encabezados y alertas de seguridad adopten el tono C.I.T */
    h3 {
        color: #ff007f !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="console-title">N.O.V.A. — C.I.T</p>', unsafe_allow_html=True
)
st.markdown("---")


# Función para generar y reproducir la voz de NOVA automáticamente
def reproducir_voz(texto_limpio):
  try:
    texto_voz = (
        texto_limpio.replace("🟣", "")
        .replace("N.O.V.A.:", "")
        .replace("*", "")
        .replace("#", "")
    )
    tts = gTTS(text=texto_voz, lang="es", slow=False)
    tts.save("voz_nova.mp3")
    with open("voz_nova.mp3", "rb") as f:
      audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(audio_html, unsafe_allow_html=True)
  except Exception:
    pass


# Estados de sesión de NOVA
if "authenticated_nova" not in st.session_state:
  st.session_state.authenticated_nova = False
if "messages_nova" not in st.session_state:
  st.session_state.messages_nova = []
if "tareas_nova" not in st.session_state:
  st.session_state.tareas_nova = [
      "Calibrar matriz táctica",
      "Sincronizar redes",
  ]

# --- PANEL LATERAL OCULTO DE NOVA ---
with st.sidebar:
  st.markdown(
      "<h3 style='color: #ff007f;'>🔒 Panel Táctico C.I.T</h3>",
      unsafe_allow_html=True,
  )
  nueva_tarea = st.text_input("Añadir pendiente operativo:")
  if st.button("Registrar en C.I.T"):
    if nueva_tarea:
      st.session_state.tareas_nova.append(nueva_tarea)
      st.success("Registrado.")

  st.markdown("#### 📌 Pendientes Operativos:")
  for idx, t in enumerate(st.session_state.tareas_nova):
    st.write(f"{idx+1}. {t}")

  if st.button("🗑️ Limpiar Tareas C.I.T"):
    st.session_state.tareas_nova = []
    st.rerun()

# --- MÓDULO 1: BIOMETRÍA VOCAL (NOVA) ---
if not st.session_state.authenticated_nova:
  st.markdown(
      "<h3 style='text-align: center; color: #ff007f;'>🔒 ACCESO RESTRINGIDO"
      " — C.I.T</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #a0a0a0;'>Emita una orden vocal"
      " para validar su firma biométrica en el sistema C.I.T.</p>",
      unsafe_allow_html=True,
  )

  audio_data = st.audio_input("🎙️ Validación de Voz para C.I.T")

  if audio_data is not None:
    st.session_state.authenticated_nova = True
    bienvenida = (
        "🟣 **N.O.V.A.:** Biometría confirmada. Sistemas C.I.T. y holográficos"
        " desplegados, Jefa."
    )
    st.session_state.messages_nova.append(
        {"role": "user", "content": "🎙️ [Comando de Voz Válido]"}
    )
    st.session_state.messages_nova.append(
        {"role": "assistant", "content": bienvenida}
    )
    reproducir_voz(bienvenida)
    st.success("✅ [FIRMA VOCAL VALIDADA]: Acceso concedido a C.I.T.")
    st.rerun()

# --- MÓDULO 2: CHAT INTELIGENTE NOVA CON HOLO-TALLER ---
else:
  st.markdown(
      "<p style='color: #ff007f; font-weight: bold;'>🟣 C.I.T OPERATIVA —"
      " SISTEMA ACTIVO</p>",
      unsafe_allow_html=True,
  )

  for message in st.session_state.messages_nova:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])
      if "widget_custom" in message:
        with st.expander("📂 Panel Desplegable C.I.T (Holograma / Multimedia)"):
          st.markdown(message["widget_custom"], unsafe_allow_html=True)

  if prompt := st.chat_input(
      "¿Qué directiva táctica o plano ejecutamos, Jefa?"
  ):
    st.session_state.messages_nova.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    widget_html = None

    # Protocolos de NOVA / C.I.T
    if (
        "clean slate" in prompt_lower
        or "purga" in prompt_lower
        or "emergencia" in prompt_lower
    ):
      response = (
          "🟣 **N.O.V.A.:** Ejecutando purga táctica. Limpiando registros y"
          " sellando frecuencias, Jefa."
      )
      st.session_state.messages_nova = []
      st.rerun()
    elif "clima" in prompt_lower or "buin" in prompt_lower:
      response = (
          "🟣 **N.O.V.A.:** Escáneres meteorológicos en Buin estables. Cielos"
          " despejados en el sector."
      )
    elif (
        "cripto" in prompt_lower
        or "mercado" in prompt_lower
        or "inversion" in prompt_lower
    ):
      response = (
          "🟣 **N.O.V.A.:** Monitoreando carteras digitales sin anomalías."
      )
    elif (
        "musica" in prompt_lower
        or "cancion" in prompt_lower
        or "reproduce" in prompt_lower
        or "spotify" in prompt_lower
    ):
      response = (
          "🟣 **N.O.V.A.:** Desplegando el reproductor de audio en el panel"
          " oculto, Jefa."
      )
      widget_html = """
            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
    elif (
        "plano" in prompt_lower
        or "diseña" in prompt_lower
        or "genera" in prompt_lower
        or "prototipo" in prompt_lower
        or "holograma" in prompt_lower
    ):
      response = f"🟣 **N.O.V.A.:** Renderizando diseño táctico para: *'{prompt}'*. Desplegando plano holográfico, Jefa."
      prompt_url = urllib.parse.quote(prompt)
      widget_html = f"""
            <div style="text-align: center; border: 1px solid #ff007f; padding: 10px; border-radius: 10px; background-color: #050505;">
                <p style="color: #ff007f; font-family: monospace; margin-bottom: 5px;">HOLO-TALLER C.I.T // PROTOTIPO TÁCTICO</p>
                <img src="https://image.pollinations.ai/prompt/{prompt_url}%20futuristic%20blueprint%20cyberpunk%20stark%20tech" width="100%" style="border-radius: 5px;">
            </div>
            """
    elif "hola" in prompt_lower or "despierta" in prompt_lower:
      response = (
          "🟣 **N.O.V.A.:** En línea, discreta y operativa a su entera"
          " disposición, Jefa."
      )
    else:
      response = f"🟣 **N.O.V.A.:** Directiva '{prompt}' procesada con precisión táctica."

    msg_dict = {"role": "assistant", "content": response}
    if widget_html:
      msg_dict["widget_custom"] = widget_html

    st.session_state.messages_nova.append(msg_dict)

    with st.chat_message("assistant"):
      st.markdown(response)
      if widget_html:
        with st.expander("📂 Ver Proyección Táctica / Oculto"):
          st.markdown(widget_html, unsafe_allow_html=True)

    reproducir_voz(response)
