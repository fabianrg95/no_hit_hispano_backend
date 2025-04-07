import datetime


class Run:
    TABLE_NAME = "partidas"

    def __init__(self, id = None, fecha_partida: datetime = None, juego_id = None, nombre_partida = None,
                 jugador_id = None,primera_partida_personal = None, primera_partida_hispano = None,
                 primera_partida_mundial = None,videos_clips = None, **kwargs):
        self.id = id
        self.fecha_partida = fecha_partida
        self.juego_id = juego_id
        self.nombre_partida = nombre_partida
        self.jugador_id = jugador_id
        self.primera_partida_personal = primera_partida_personal
        self.primera_partida_hispano = primera_partida_hispano
        self.primera_partida_mundial = primera_partida_mundial
        self.videos_clips = videos_clips

    def __repr__(self):
        return f"Run({self.__dict__})"