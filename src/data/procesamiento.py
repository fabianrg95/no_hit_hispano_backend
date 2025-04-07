from datetime import datetime

from src.data import supabase
from src.models.dto.partida_dto import PartidaDTO
from src.models.excel.partida import Partida
from src.models.supabase.run import Run
from src.utils import utilidades
from src.utils.data_store import DataStore
import re
import unicodedata

data_store = DataStore()

def process_data():

    for partida in data_store.obtener_partidas_a_procesar():
        partida_dto = mapear_informacion_partida_para_validacion(partida)

        if validar_registro_correcto(partida, partida_dto) is False:
            guardar_partida_database(partida_dto, partida)

def guardar_partida_database(partida_dto: PartidaDTO, partida_excel: Partida):
    run: Run = mapear_partida_database(partida_dto)
    if supabase.registrar_partida(run) is True:
        utilidades.notificar_exito_discord(utilidades.construir_mensaje_exito(partida_excel))

def validar_registro_correcto(partida, partida_dto)-> bool:
    mensaje_fecha = None
    mensaje_runner = None
    mensaje_juego = None

    registro_con_error = False
    fecha_partida = utilidades.obtener_fecha_partida_normalizada(partida_dto.fecha)

    if fecha_partida is None or fecha_partida > datetime.now():
        mensaje_fecha = {"name": "• Fecha", "value": "La fecha de la run '"+partida.fecha+"' posee un error."}
        registro_con_error = True

    if partida_dto.id_juego == 0:
        mensaje_runner = {"name": "• Juego", "value": "El juego '"+partida.juego+"' de la run  no se encuentra en la base."}
        registro_con_error = True

    if partida_dto.id_runner == 0:
        mensaje_juego = {"name": "• Runner", "value": "El runner '"+partida.runner+"' no se encuentra en la base."}
        registro_con_error = True

    if registro_con_error:
        utilidades.notificar_error_discord(utilidades.construir_mensaje_error(partida.__repr__(), [mensaje_fecha, mensaje_juego, mensaje_runner]))

    return registro_con_error

def mapear_informacion_partida_para_validacion(partida):
    nombre_juego_normalizado = limpiar_texto_sin_tildes(partida.juego)
    partida_dto = PartidaDTO()
    partida_dto.update(fecha=partida.fecha)
    partida_dto.update(id_juego=obtener_juego(nombre_juego_normalizado))
    partida_dto.update(nombre_partida=partida.run)
    partida_dto.update(id_runner=obtener_jugador(partida.runner))
    partida_dto.update(video_clips=unificar_links_videos(partida))
    partida_dto.update(primera_personal=partida.personal_1st)
    partida_dto.update(primera_hispano=partida.hispano_1st)
    partida_dto.update(primera_mundial=partida.world_1st)
    partida_dto.update(pronombre=partida.pronombre)
    partida_dto.update(año_de_nacimiento=partida.año_de_nacimiento)
    partida_dto.update(nacionalidad=partida.nacionalidad)
    return partida_dto

def mapear_partida_database(partida_dto: PartidaDTO) -> Run:
    return Run(fecha_partida=utilidades.obtener_fecha_partida_normalizada(partida_dto.fecha).strftime("%Y-%m-%d"),
              juego_id=partida_dto.id_juego,
              nombre_partida=partida_dto.nombre_partida,
              jugador_id=partida_dto.id_runner,
              primera_partida_personal=partida_dto.primera_personal,
              primera_partida_hispano=partida_dto.primera_hispano,
              primera_partida_mundial=partida_dto.primera_mundial,
              videos_clips=partida_dto.video_clips)

def obtener_juego(nombre_juego_normalizado):
    juegos = data_store.obtener_juegos()

    for juego in juegos:
        lista_nombres_juego = [nombre.strip() for nombre in juego.nombres_juego.split(',')]
        if nombre_juego_normalizado in lista_nombres_juego:
            return juego.id
    return 0

def obtener_jugador(nombre_jugador):
    jugadores = data_store.obtener_jugadores()

    for jugador in jugadores:
        lista_nombres_jugador = [nombre.strip().lower() for nombre in jugador.nombres_jugador.split(',')]
        if nombre_jugador.strip().lower() in lista_nombres_jugador:
            return jugador.id
    return 0

def limpiar_texto_sin_tildes(texto: str) -> str:
    # 1. Normaliza el texto (NFD separa letras y tildes)
    texto_normalizado = unicodedata.normalize('NFD', texto)

    # 2. Elimina los signos diacríticos (tildes, diéresis, etc.)
    texto_sin_tildes = ''.join(
        c for c in texto_normalizado
        if unicodedata.category(c) != 'Mn'
    )

    # 3. Elimina caracteres especiales (deja letras, números y espacios)
    texto_limpio = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sin_tildes)

    return texto_limpio.strip().lower()

def unificar_links_videos(partida) -> str:
    links_youtube = partida.run_youtube
    links_twitch = partida.run_twitch if partida.run_twitch != 'NO HAY CLIP' else ""

    return ",".join([links_youtube,links_twitch])


