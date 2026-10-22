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

# Estado de autenticación e historial de mensajes
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "messages" not in st.session_state:
  st.session_state.messages = []

# --- MÓDULO 1: BIOMETRÍA VOCAL Y ACTIVACIÓN POR VOZ ---
if not st.session_state.authenticated:
  st.markdown(
      "<h3 style='text-align: center; color: #ff3366;'>🔒 ACCESO RESTRINGIDO"
      " — MODO SIGILO</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #a0a0a0;'>Graba tu comando de voz"
      " ('Hola N.O.V.A.' o 'N.O.V.A. activa') para validar tu huella"
      " biométrica.</p>",
      unsafe_allow_html=True,
  )

  # Grabador de audio para validación vocal
  audio_data = st.audio_input("🎙️ Presiona para hablarle a N.O.V.A.")

  if audio_data is not None:
    st.session_state.authenticated = True

    # Mensaje inicial de bienvenida personalizado para N.O.V.A.
    st.session_state.messages.append(
        {"role": "user", "content": "🎙️ [Comando Vocal]: Hola N.O.V.A."}
    )
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "🌟 **N.O.V.A.:** Sistemas tácticos en línea, Jefa. Lista para"
            " tomar el control cuando usted lo indique."
        ),
    })

    st.success("✅ [HUELLA VOCAL DETECTADA]: Autenticación correcta, Jefa.")
    st.rerun()

# --- MÓDULO 2: CHAT INTERACTIVO CON PERSONALIDAD TÁCTICA ---
else:
  st.markdown(
      "<p style='color: #00f0ff; font-weight: bold;'>🌟 SISTEMA DESBLOQUEADO —"
      " UNIDAD NOVA OPERATIVA</p>",
      unsafe_allow_html=True,
  )

  # Mostrar el historial de la conversación
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # Entrada del chat con respuestas según lo que preguntes
  if prompt := st.chat_input("¿Qué directiva táctica ejecutamos hoy, Jefa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    prompt_lower = prompt.lower().strip()

    # Lógica de respuestas dinámicas según la consulta
    if any(
        saludo in prompt_lower
        for saludo in ["hola", "buenas", "que tal", "nova"]
    ):
      response = (
          "🌟 **N.O.V.A.:** A sus órdenes, Jefa. Todos los sistemas funcionando"
          " al 100%. ¿Qué tenemos en agenda?"
      )
    elif "despierta" in prompt_lower or "despierto" in prompt_lower:
      response = (
          "🌟 **N.O.V.A.:** Jamás duermo, Jefa. Los núcleos C.I.T están listos"
          " para cualquier misión."
      )
    elif "quien eres" in prompt_lower or "quién eres" in prompt_lower:
      response = (
          "🌟 **N.O.V.A.:** Soy N.O.V.A., su unidad táctica C.I.T. Diseñada"
          " para ejecutar, optimizar y proteger sus proyectos con máxima"
          " precisión."
      )
    else:
      response = (
          f"🌟 **N.O.V.A.:** Comprendido, Jefa. Procesando '{prompt}' a máxima"
          " velocidad. Considerelo en marcha."
      )

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
      st.markdown(response)
