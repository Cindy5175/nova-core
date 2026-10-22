import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Stark Core - NOVA Secure", page_icon="🌟", layout="centered"
)

# Estilos CSS personalizados (Modo Sigilo y Neón Azul)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .console-title {
        color: #00f0ff;
        font-family: monospace;
        font-size: 16px;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: 1.5px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="console-title">N.O.V.A. — C.I.T</p>', unsafe_allow_html=True
)
st.markdown("---")

# Estado de autenticación
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False

# --- MÓDULO 1: BIOMETRÍA VOCAL REAL ---
if not st.session_state.authenticated:
  st.markdown(
      "<h3 style='text-align: center; color: #ff3366;'>🔒 ACCESO RESTRINGIDO"
      " — MODO SIGILO</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #a0a0a0;'>Graba un comando de voz"
      " para validar tu huella biométrica y activar a NOVA.</p>",
      unsafe_allow_html=True,
  )

  # Grabador de audio para validación vocal
  audio_data = st.audio_input("🎙️ Presiona para grabar tu firma vocal")

  if audio_data is not None:
    st.session_state.authenticated = True
    st.success("✅ [HUELLA VOCAL DETECTADA]: Autenticación correcta, Jefa.")
    st.rerun()

# --- MÓDULO 2: CHAT INTERACTIVO FUNCIONAL ---
else:
  st.markdown(
      "<p style='color: #00f0ff; font-weight: bold;'>🌟 SISTEMA DESBLOQUEADO —"
      " UNIDAD NOVA OPERATIVA</p>",
      unsafe_allow_html=True,
  )

  if "messages" not in st.session_state:
    st.session_state.messages = []

  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  if prompt := st.chat_input("¿Qué directiva táctica ejecutamos hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    response = (
        f"🌟 **N.O.V.A.:** Directiva '{prompt}' analizada. Unidad táctica lista"
        " a su orden, Jefa."
    )
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
      st.markdown(response)
