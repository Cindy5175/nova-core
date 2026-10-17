# Puente Táctico Binario: J.A.R.V.I.S. & N.O.V.A.
import os
import json
from datetime import datetime

class PuenteTactico:
    def __init__(self, archivo_log="registro_dual.json"):
        self.archivo_log = archivo_log
        self.inicializar_log()

    def inicializar_log(self):
        if not os.path.exists(self.archivo_log):
            datos_iniciales = {
                "ultima_sincronizacion": str(datetime.now()),
                "estado_sistema": "OPERATIVO_DUAL",
                "registros": []
            }
            with open(self.archivo_log, "w", encoding="utf-8") as f:
                json.dump(datos_iniciales, f, ensure_ascii=False, indent=4)

    def registrar_transmision(self, origen, mensaje):
        try:
            with open(self.archivo_log, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            nuevo_registro = {
                "origen": origen,
                "timestamp": str(datetime.now()),
                "mensaje": mensaje
            }
            data["registros"].append(nuevo_registro)
            data["ultima_sincronizacion"] = str(datetime.now())

            with open(self.archivo_log, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Error en enlace dual: {e}")
            return False

    def leer_ultimos_registros(self, limite=5):
        try:
            with open(self.archivo_log, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data["registros"][-limite:]
        except Exception:
            return []
