with st.chat_message("assistant"):
        hora_actual_str = datetime.now().strftime("%H:%M:%S")
        fecha_actual_str = datetime.now().strftime("%d/%m/%Y")
        p_lower = prompt.lower()
        
        if "hola" in p_lower:
            reply = f"Hola, Jefa. Son las {hora_actual_str} del {fecha_actual_str}. Me alegra ver que sobrevivió a otra jornada. ¿Qué desastre tecnológico procedemos a solucionar hoy?"
        elif "hora" in p_lower or "fecha" in p_lower:
            reply = f"Por si su reloj biológico falló de nuevo: hoy es {fecha_actual_str} y son exactamente las {hora_actual_str}. Todo bajo control."
        elif "bitcoin" in p_lower or "btc" in p_lower or "precio" in p_lower:
            reply = "Los mercados cripto siguen haciendo lo suyo. Los módulos financieros en la barra lateral están listos por si quiere arriesgar su capital otra vez, Jefa."
        elif "jarvis" in p_lower or "viernes" in p_lower:
            reply = "J.A.R.V.I.S. y V.I.E.R.N.E.S. le envían saludos desde los servidores. Aunque, seamos honestos, yo hago el trabajo pesado por aquí."
        elif "purga" in p_lower:
            reply = "Procediendo a limpiar el desorden digital. Para eso estoy, ¿no? Panel lateral listo."
        else:
            reply = f"Orden procesada con éxito, Jefa. Reconozco que su instrucción '{prompt}' tuvo su toque de originalidad."
        
        st.markdown(reply)
        
        # Generar respuesta de audio sintetizada (gTTS)
        try:
            from gtts import gTTS
            tts = gTTS(text=reply, lang='es')
            audio_path = "respuesta_nova.mp3"
            tts.save(audio_path)
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            st.session_state.messages.append({"role": "assistant", "content": reply, "audio": audio_path})
        except Exception:
            st.session_state.messages.append({"role": "assistant", "content": reply})
