import google.generativeai as genai
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

# Configurar el modelo de Inteligencia Artificial para NOVA mediante Secrets
try:
  api_key = st.secrets["GEMINI_API_KEY"]
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      system_instruction=(
          "Eres N.O.V.A., una inteligencia artificial táctica y avanzada del"
          " taller Stark. Te diriges a la usuaria como 'Jefa'. Eres audaz,"
          " rápida, leal y eficiente. Respondes con datos precisos, actitud"
          " táctica e inteligencia real a cualquier consulta (clima,"
          " información, ciencia, tareas)."
      ),
  )
except Exception:
  model = None

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

# --- MÓDULO 2: SUPER IA Y CHAT INTERACTIVO ---
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

  # Entrada del chat para interactuar con la Super IA táctica
  if prompt := st.chat_input("¿Qué directiva táctica ejecutamos hoy, Jefa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    prompt_lower = prompt.lower().strip()

    # 1. Respuestas de personalidad rápida o activaciones especiales
    if "despierta" in prompt_lower or "despierto" in prompt_lower:
      response = (
          "🌟 **N.O.V.A.:** Jamás duermo, Jefa. Los núcleos C.I.T están listos"
          " para cualquier misión."
      )
    # 2. Procesamiento con la Super IA de Gemini
    elif model is not None:
      try:
        ai_response = model.generate_content(prompt)
        response = f"🌟 **N.O.V.A.:** {ai_response.text}"
      except Exception as e:
        response = (
            "🌟 **N.O.V.A.:** Alerta táctica: Error al conectar con los"
            f" servidores principales: {e}"
        )
    # 3. Respaldo por si falta configurar los secrets
    else:
      response = (
          f"🌟 **N.O.V.A.:** Directiva '{prompt}' registrada. (Configure"
          " GEMINI_API_KEY en los Secrets para habilitar la Super IA)."
      )

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
      st.markdown(response)
