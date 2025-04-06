class Jugador:
    TABLE_NAME = "jugadores"

    def __init__(self, id, nombre_usuario, pronombre_id, anio_nacimiento, nombres_jugador, **kwargs):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.pronombre_id = pronombre_id
        self.anio_nacimiento = anio_nacimiento
        self.nombres_jugador = nombres_jugador

    def __repr__(self):
        return f"Jugador(id={self.id}, nombre={self.nombre_usuario}, pronombre_id={self.pronombre_id}, anio_nacimiento={self.anio_nacimiento}, nombres_jugador={self.nombres_jugador})"