import os
from datetime import datetime
import requests
from src.models.excel.partida import Partida


def obtener_fecha_partida_normalizada(fecha) -> datetime | None:
    formatos = ["%d/%m/%Y", "%d/%m/%y"]
    for formato in formatos:
        try:
            return datetime.strptime(fecha, formato)
        except ValueError:
            continue

def notificar_error_discord(mensaje: str):
    print("Notificando sobre un error en la sincronizacion de una partida por discord.")
    webhook_url = os.getenv("WEBHOOK_NOTIFICACIONES_ERRORES")
    if not webhook_url:
        raise ValueError("No se encontró la variable de entorno DISCORD_WEBHOOK_URL")

    payload = {
        "embeds": [mensaje]
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code != 204:
        raise Exception(f"Error al enviar mensaje a Discord: {response.status_code} - {response.text}")

def notificar_exito_discord(mensaje):
    print("Notificando exito en la sincronizacion de una partida por discord.")
    webhook_url = os.getenv("WEBHOOK_NOTIFICACIONES_EXITOSAS")
    if not webhook_url:
        raise ValueError("No se encontró la variable de entorno DISCORD_WEBHOOK_URL")

    payload = {
        "embeds": [mensaje]
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code != 204:
        raise Exception(f"Error al enviar mensaje a Discord: {response.status_code} - {response.text}")

    return None

def construir_mensaje_error(partida, errores):
    mensaje = []
    for error in errores:
        if error is not None:
            mensaje.append(error)

    return {
        "title": "🚨 **Registro de run con inconvenientes** 🚨",
        "description": "Se detectaron los siguientes inconvenientes durante el registro de la siguiente run: \n\n"
                       "",
        "color": 16711680,  # rojo
        "fields": mensaje,
        "footer": {
            "text": "No Hit Hispano"
        }
    }

def construir_mensaje_exito(partida_excel : Partida):

    embeds = {
        "title": "⭐ **Nueva run registrada** ⭐",
        "description": "**"+ partida_excel.runner +"** logro el reto **"+ partida_excel.run +"** en **"+ partida_excel.juego +"** el "+ partida_excel.fecha,
        "color": 8912681,
        "fields": [],
        "footer": {
            "text": "No Hit Hispano"
        }
    }

    mensaje = ""
    if partida_excel.personal_1st is True:
        mensaje += "• Es su primera run. \n "
    if partida_excel.hispano_1st is True:
        mensaje += "• Es el primer hispano en lograrlo. \n "
    if partida_excel.world_1st is True:
        mensaje += "• Es la primera persona a nivel mundial que lo logra. \n "

    if mensaje != "":
        embeds["fields"].append({"name": "WOW 😲", "value" : mensaje})

    return embeds


