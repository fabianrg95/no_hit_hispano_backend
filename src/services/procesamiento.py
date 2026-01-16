from datetime import datetime
from src.convertidor.convertidor_partida import partida_excel_a_partida_dto, partida_dto_a_partida_db
from src.data import supabase
from src.models.dto.partida_dto import PartidaDTO
from src.models.excel.partida_excel import PartidaExcel
from src.notificador.notificador import construir_mensaje_error, construir_mensaje_exito
from src.utils.data_store import DataStore
from src.utils.normalizador import normalizar_fecha_partida

data_store = DataStore()

def procesar_registro_partida(datos_excel : [PartidaExcel]):

    for index, partida in enumerate(datos_excel):
        print(f"Procesando item #{index + 1} de {len(datos_excel)}: {partida.fecha}")
        partida_dto = partida_excel_a_partida_dto(partida)

        errores = validar_registro_correcto(partida, partida_dto)

        if len(errores) > 0:
            data_store.cargar_notificacion_fallos(construir_mensaje_error(errores))
        else:
            guardar_partida_database(partida_dto, partida)


def validar_registro_correcto(partida, partida_dto)-> []:
    errores = []
    fecha_partida = normalizar_fecha_partida(partida_dto.fecha)

    if fecha_partida is None or fecha_partida > datetime.now():
        errores.append({"name": "• Fecha", "value": "'"+partida.fecha+"' posee un error."})

    if partida_dto.id_juego == 0:
        errores.append({"name": "• Juego", "value": "'"+partida.juego+"' no se encuentra registrado."})

    if partida_dto.id_runner == 0:
        errores.append({"name": "• Runner", "value": "'"+partida.runner+"' no se encuentra registrado."})

    return errores

def guardar_partida_database(partida_dto: PartidaDTO, partida_excel: PartidaExcel):
    if supabase.registrar_partida(partida_dto_a_partida_db(partida_dto)) is True:
        data_store.cargar_notificacion_exitos(construir_mensaje_exito(partida_excel))
