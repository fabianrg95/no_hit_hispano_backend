import os
import time

import requests
from src.models.enums.mensaje_notificacion_discord import MensajeNotificacion
from src.models.excel.partida_excel import PartidaExcel
from src.utils.data_store import DataStore

data_store = DataStore()

def notificar_error_discord():
    fallos = data_store.obtener_notificaciones_fallos()
    if len(fallos) > 0:
        print("Iniciando las notificaciones de errores....")
        for notificacion in fallos:
            print("Notificando sobre un error en la sincronizacion de una partida por discord.")
            __notificar_discord(notificacion, "WEBHOOK_NOTIFICACIONES_ERRORES")
            time.sleep(2)
        print("Finalizando las notificaciones de errores....")
    else:
        print("No se detectaron fallos para notificar")

def notificar_exito_discord():
    exitos = data_store.obtener_notificaciones_exitos()
    if len(exitos) > 0:
        print("Iniciando las notificaciones de registros exitosos....")
        for notificacion in data_store.obtener_notificaciones_exitos():
            print("Notificando exito en la sincronizacion de una partida por discord.")
            __notificar_discord(notificacion, "WEBHOOK_NOTIFICACIONES_EXITOSAS")
            time.sleep(2)
        print("Finalizando las notificaciones de registros exitosos....")
    else:
        print("No se detectaron exitos para notificar")


def __notificar_discord(mensaje: str, webhook: str):
    webhook_url = os.getenv(webhook)
    if not webhook_url:
        raise ValueError("No se encontró la variable de entorno "+ webhook)

    payload = {
        "embeds": [mensaje]
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        raise Exception(f"Error al enviar mensaje a Discord: {response.status_code} - {response.text}")

def construir_mensaje_error(errores):
    return MensajeNotificacion.ERROR.contruir_embeds(None, errores)

def construir_mensaje_exito(partida_excel : PartidaExcel):
    descripcion = MensajeNotificacion.NUEVA_RUN.descripcion.format(runner=partida_excel.runner, run=partida_excel.run, juego=partida_excel.juego, fecha=partida_excel.fecha)

    mensajes = []
    if partida_excel.personal_1st is True:
        mensajes.append("• Es su primera run.")
    if partida_excel.hispano_1st is True:
        mensajes.append("• Es el primer hispano en lograrlo.")
    if partida_excel.world_1st is True:
        mensajes.append("• Es la primera persona a nivel mundial que lo logra.")

    fields = []
    if mensajes:
        fields.append({
            "name": "WOW 😲",
            "value": "\n".join(mensajes)
        })

    return MensajeNotificacion.NUEVA_RUN.contruir_embeds(descripcion, fields)


