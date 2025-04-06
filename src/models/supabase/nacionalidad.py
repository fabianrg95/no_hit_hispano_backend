class Nacionalidad:
    TABLE_NAME = "nacionalidad"

    def __init__(self, id, pais, continente_id, gentilicio_femenino, **kwargs):
        self.id = id
        self.pais = pais
        self.continente_id = continente_id
        self.gentilicio_femenino = gentilicio_femenino

    def __repr__(self):
        return f"Nacionalidad(id={self.id}, pais={self.pais}, continente_id={self.continente_id}, gentilicio_femenino={self.gentilicio_femenino})"