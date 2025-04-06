from datetime import datetime


def obtener_fecha_partida_normalizada(partida_dto) -> datetime | None:
    formatos = ["%d/%m/%Y", "%d/%m/%y"]
    for formato in formatos:
        try:
            return datetime.strptime(partida_dto.fecha, formato)
        except ValueError:
            continue
