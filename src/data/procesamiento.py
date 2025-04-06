from src.models.dto.partida_dto import PartidaDTO
from src.utils.data_store import DataStore
import re
import unicodedata

data_store = DataStore()


def process_data():

    for partida in data_store.obtener_partidas_a_procesar():
        nombre_juego_normalizado = limpiar_texto_sin_tildes(partida.juego)
        partida_dto = PartidaDTO()
        partida_dto.update(fecha = partida.fecha)
        partida_dto.update(id_juego = obtener_juego(nombre_juego_normalizado))
        partida_dto.update(id_runner = obtener_jugador(partida.runner))
        partida_dto.update(video_clips = unificar_links_videos(partida))
        partida_dto.update(primera_personal = partida.personal_1st)
        partida_dto.update(primera_hispano = partida.hispano_1st)
        partida_dto.update(primera_mundial = partida.world_1st)

        if partida_dto.id_runner == 0:
            print("No se encontro el jugador con nombre "+ partida.runner)
            print(partida_dto)

        print(partida_dto)


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


