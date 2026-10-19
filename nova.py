REPORTE_NOVA = (
    "✨ **PROTOCOLO N.O.V.A. ACTIVADO** ✨\n\n"
    "Saludos, Jefa. Soy N.O.V.A. (Neural Operational Surveillance & Assistance), "
    "el núcleo de inteligencia estratégica, análisis de datos y soporte avanzado diseñado por Cindy "
    "para la gestión táctica del taller. Enlace N.T.C. en línea, monitoreando flujos, parámetros "
    "y seguridad global. ¿En qué enfocaré mis capacidades analíticas hoy?"
)

# Filtro dentro del chat de N.O.V.A.
if "presentacion" in p_lower or "presentación" in p_lower or "quien eres" in p_lower or "quién eres" in p_lower:
    respuesta_ia = REPORTE_NOVA
elif "directivas" in p_lower or "reglas" in p_lower:
    respuesta_ia = (
        "🛡️ **DIRECTIVAS FUNDAMENTALES DE N.O.V.A.:**\n\n"
        "1. **Lealtad Prima:** Comando exclusivo subordinado a Cindy (Jefa).\n"
        "2. **Análisis Táctico:** Supervisión de datos, memoria N.T.C. y rendimiento del taller.\n"
        "3. **Coordinación:** Sincronización continua con el núcleo J.A.R.V.I.S.\n"
        "4. **Protección:** Prevención de fallos y auditoría de seguridad."
    )
elif "capacidades" in p_lower or "que puedes hacer" in p_lower or "qué puedes hacer" in p_lower:
    respuesta_ia = (
        "⚙️ **MÓDULOS OPERATIVOS DE N.O.V.A.:**\n\n"
        "• 📊 Diagnóstico y análisis de rendimiento en tiempo real.\n"
        "• 💾 Auditoría y persistencia en memoria compartida JSON.\n"
        "• 🔐 Control de acceso biométrico y protocolos N.T.C.\n"
        "• 🛰️ Telemetría satelital y sincronización ambiental."
    )
