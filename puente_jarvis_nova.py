import json
import os
import time

ARCHIVO_MEMORIA = "memoria_compartida.json"


def inicializar_memoria():
    if not os.path.exists(ARCHIVO_MEMORIA):
        datos_iniciales = {
            "ultima_directiva": "Sin directivas recientes",
            "origen": "N.O.V.A.",
            "estado_jarvis": "STANDBY",
            "respuestas_jarvis": [
                "J.A.R.V.I.S. vinculado y a la espera de comandos, Jefa."
            ],
        }
        with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as f:
            json.dump(datos_iniciales, f, ensure_ascii=False, indent=4)


def guardar_directiva(mensaje):
    inicializar_memoria()
    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as f:
        datos = json.load(f)

    datos["ultima_directiva"] = mensaje
    datos["origen"] = "N.O.V.A. Mobile"

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def leer_memoria():
    inicializar_memoria()
    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as f:
        return json.load(f)