if prompt := st.chat_input(tn["input"]):
        st.session_state.msgs_n.append({"role": "user", "content": prompt})
        
        texto_lower = prompt.lower().strip()
        
        # Palabras de saludo para detectar aunque traigan más texto (ej: "hola nova", "hola jarvis")
        saludos = ["hola", "hello", "bonjour", "olá", "saludos", "buenas", "buenos dias", "buenas tardes", "buenas noches"]
        preguntas_estado = ["cómo estás", "como estas", "cómo andas", "que tal", "how are you", "comment vas-tu", "como vai", "estado", "reporte"]
        
        # 1. Si incluye algún saludo
        if any(s in texto_lower for s in saludos):
            if idioma_n == "English 🇺🇸":
                resp_n = "REPORT: Greeting acknowledged. N.O.V.A. online and armed via Starlink. What is our directive, Boss?"
            elif idioma_n == "Français 🇫🇷":
                resp_n = "RAPPORT : Salutations reçues. N.O.V.A. en ligne et parée via Starlink. Quelle est notre directive, Chef ?"
            elif idioma_n == "Português 🇧🇷":
                resp_n = "RELATÓRIO: Saudação recebida. N.O.V.A. online via Starlink. Qual é a nossa diretriz, Chefe?"
            else:
                resp_n = "INFORME: Saludo recibido. N.O.V.A. en línea y pertrechada vía Starlink. ¿Qué directiva ejecutamos, Jefa?"
                
        # 2. Si pregunta por su estado
        elif any(p in texto_lower for p in preguntas_estado):
            resp_n = "ESTADO TÁCTICO: Perímetros seguros, latencia Starlink en 18ms y encriptación cuántica activa al 100%."
            
        # 3. Respuesta por defecto para directivas o comandos más complejos
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
