# --- ÁREA DE CHAT CON HORA Y FECHA LOCAL EXACTA ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message and message["audio"]:
            st.audio(message["audio"], format="audio/mp3")

prompt = st.chat_input("Ingrese comando, consulta o instrucción táctica para N.O.V.A...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    puente.registrar_transmision("NOVA", prompt)

    with st.chat_message("assistant"):
        # Se obtiene la hora y fecha local actual
        ahora = datetime.now()
        hora_num = ahora.hour
        hora_actual_str = ahora.strftime("%H:%M:%S")
        fecha_actual_str = ahora.strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        # Determinación dinámica del saludo según la hora local exacta
        if 5 <= hora_num < 12:
            saludo = "Buenos días"
        elif 12 <= hora_num < 20:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"
        
        if "hola" in p_lower:
            reply = f"{saludo}, Jefa. Son exactamente las {hora_actual_str} del {fecha_actual_str}. El reloj táctico y el núcleo de plasma están operando en perfecta sincronía. ¿Qué orden ejecutamos hoy?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Confirmado, Jefa: hoy es {fecha_actual_str} y la hora exacta en su ubicación es {hora_actual_str}."
        elif "bitcoin" in p_lower or "btc" in p_lower or "mercado" in p_lower:
            reply = "Accediendo a las métricas del mercado en tiempo real. Los paneles secundarios están disponibles a su izquierda."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "Enlace con J.A.R.V.I.S. activo. Reportan telemetría estable."
        elif "purga" in p_lower or "limpiar" in p_lower:
            reply = "Módulo de purga preparado. Puede ejecutar la limpieza desde el panel lateral."
        else:
            reply = f"Comando '{prompt}' recibido y en procesamiento, Jefa. Sistemas en alerta constante."
        
        st.markdown(reply)
        
        try:
            from gtts import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
