from enum import Enum

class MensajeNotificacion(Enum):
    NUEVA_RUN = (
        "⭐ **Nueva run registrada** ⭐",
        "**{runner}** logró el reto **{run}** en **{juego}** el {fecha}",
        8912681,
        "No Hit Hispano"
    )
    ERROR = (
        "🚨 **Registro de run con inconvenientes** 🚨",
        "Se detectaron los siguientes inconvenientes durante el registro de la run: \n\n",
        16711680,
        "Sistema de Monitoreo"
    )

    def __init__(self, titulo, descripcion, color, pie_pagina):
        self.titulo = titulo
        self.descripcion = descripcion
        self.color = color
        self.pie_pagina = pie_pagina

    def contruir_embeds(self, mensaje, fields):
        return {
            "title": self.titulo,
            "description": mensaje if mensaje is not None else self.descripcion,
            "color": self.color,
            "fields": fields,
            "footer": {
                "text": self.pie_pagina
            }
        }
