import os
from datetime import datetime
from typing import Any

import requests


def obtener_fecha_partida_normalizada(partida_dto) -> datetime | None:
    formatos = ["%d/%m/%Y", "%d/%m/%y"]
    for formato in formatos:
        try:
            return datetime.strptime(partida_dto.fecha, formato)
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

def construir_mensaje_error(partida, errores):
    mensaje = []
    for error in errores:
        if error is not None:
            mensaje.append(error)

    return {
        "title": "🚨 Registro de run con inconvenientes",
        "description": "Se detectaron los siguientes inconvenientes durante el registro de la siguiente run: \n\n"
                       "",
        "color": 16711680,  # rojo
        "fields": mensaje,
        "footer": {
            "text": "No Hit Hispano - Backend"
        }
    }