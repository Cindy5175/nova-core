if prompt := st.chat_input("Ingrese consulta o directiva táctica..."):
        st.session_state.msgs_n.append({"role": "user", "content": prompt})
        
        texto_lower = prompt.lower().strip()
        
        if any(w in texto_lower for w in ["hola", "buenos dias", "buenas tardes", "buenas noches", "saludos"]):
            resp_n = "INFORME: Saludo recibido. N.O.V.A. en línea y pertrechado. ¿Qué directiva ejecutamos, Jefa?"
            
        elif any(w in texto_lower for w in ["cómo estás", "como estas", "estado", "reporte"]):
            resp_n = "ESTADO TÁCTICO: Todos los perímetros están seguros, encriptación activa al 100% y latencia mínima."
            
        elif any(w in texto_lower for w in ["quién eres", "quien eres"]):
            resp_n = "Soy N.O.V.A. (C.I.T.), su protocolo de Inteligencia Táctica y Blindaje de Seguridad."
            
        elif any(w in texto_lower for w in ["gracias"]):
            resp_n = "CONFIRMACIÓN: De nada, Jefa. Manteniendo guardia activa."
            
        else:
            resp_n = f"DIRECTIVA RECIBIDA: '{prompt}'. Registrada en auditoría sin anomalías en el sector."

        st.session_state.msgs_n.append({"role": "assistant", "content": resp_n})
        
        nuevo_evento = {"Hora": datetime.now().strftime("%H:%M:%S"), "Evento": f"Comando: {prompt[:12]}...", "Estado": "VERIFICADO"}
        memoria_nova["auditoria"].append(nuevo_evento)
        guardar_memoria_nova(memoria_nova)
        
        emitir_voz_nova(resp_n)
        st.rerun()
