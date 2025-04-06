class Continente:
    TABLE_NAME = "continente"

    def __init__(self, id, nombre, fecha_insert):
        self.id = id
        self.nombre = nombre
        self.fecha_insert = fecha_insert

    def __repr__(self):
        return f"Continente(id={self.id}, nombre={self.nombre}, fecha_insert={self.fecha_insert})"