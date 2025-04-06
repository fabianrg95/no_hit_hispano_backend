class Juego:
    TABLE_NAME = "juegos"

    def __init__(self, id, nombre, subtitulo, nombres_juego, **kwargs):
        self.id = id
        self.nombre = nombre
        self.subtitulo = subtitulo
        self.nombres_juego = nombres_juego

    def __repr__(self):
        return f"Juego(id={self.id}, nombre={self.nombre}, subtitulo={self.subtitulo}, nombres_juego={self.nombres_juego})"