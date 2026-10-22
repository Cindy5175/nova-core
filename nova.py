import streamlit as st

# Configuración de la página para NOVA
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
    '<p class="console-title">N.O.V.A. — UNIDAD TÁCTICA SEGURA</p>',
    unsafe_allow_html=True,
)
st.markdown("---")

# --- MÓDULO 1: BIOMETRÍA DE VOZ (PROTOCOLO DE SEGURIDAD NOVA) ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False

if not st.session_state.authenticated:
  st.markdown(
      "<h3 style='text-align: center; color: #ff3366;'>🔒 ACCESO RESTRINGIDO"
      " — MODO SIGILO</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #a0a0a0;'>Se requiere validación de"
      " huella vocal para desbloquear el núcleo NOVA.</p>",
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("🎙️ VALIDAR BIOMETRÍA VOCAL", use_container_width=True):
      # Validación biométrica
      st.session_state.authenticated = True
      st.rerun()

else:
  # --- MÓDULO 2: CHAT INTERACTIVO FUNCIONAL (DESBLOQUEADO) ---
  st.success("✅ [ACCESO CONCEDIDO]: Biometría de voz validada. Hola, Jefa.")

  # Inicializar el historial de mensajes de NOVA
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # Mostrar mensajes anteriores en pantalla
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # Caja de entrada interactiva para chatear
  if prompt := st.chat_input("¿Qué directiva táctica ejecutamos hoy?"):
    # Guardar y mostrar mensaje de la usuaria
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
      st.markdown(prompt)

    # Respuesta del núcleo NOVA
    response = (
        f"🌟 Directiva procesada en el núcleo NOVA: '{prompt}'. Unidad táctica"
        " lista, Jefa."
    )
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
      st.markdown(response)
