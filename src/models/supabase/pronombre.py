class Pronombre:
    TABLE_NAME = "pronombre"

    def __init__(self, id, pronombre, genero, fecha_insert, **kwargs):
        self.id = id
        self.pronombre = pronombre
        self.genero = genero
        self.fecha_insert = fecha_insert

    def __repr__(self):
        return f"Pronombre(id={self.id}, pronombre={self.pronombre}, genero={self.genero}, fecha_insert={self.fecha_insert})"