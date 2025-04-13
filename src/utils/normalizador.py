import re
import unicodedata
from datetime import datetime
from src.utils.constantes import formatos_fecha
from src.utils.data_store import DataStore

data_store = DataStore()

def normalizar_fecha_partida(fecha) -> datetime | None:
    for formato in formatos_fecha:
        try:
            return datetime.strptime(fecha, formato)
        except ValueError:
            continue

def normalizar_texto(texto: str) -> str:
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

def normalizar_links_videos(partida) -> str:
    links_youtube = partida.run_youtube
    links_twitch = partida.run_twitch if partida.run_twitch != 'NO HAY CLIP' else ""

    return ",".join([links_youtube,links_twitch])

def buscar_juego_por_nombre(nombre_juego_normalizado):
    juegos = data_store.obtener_juegos()

    for juego in juegos:
        lista_nombres_juego = [nombre.strip() for nombre in juego.nombres_juego.split(',')]
        if nombre_juego_normalizado in lista_nombres_juego:
            return juego.id
    return 0

def buscar_jugador_por_nombre(nombre_jugador):
    jugadores = data_store.obtener_jugadores()

    for jugador in jugadores:
        lista_nombres_jugador = [nombre.strip().lower() for nombre in jugador.nombres_jugador.split(',')]
        if nombre_jugador.strip().lower() in lista_nombres_jugador:
            return jugador.id
    return 0
