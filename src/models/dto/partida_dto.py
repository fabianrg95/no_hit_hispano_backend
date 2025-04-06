class PartidaDTO:
    def __init__(self, fecha=None, id_juego=None, id_runner=None, video_clips=None, primera_personal=False,
                 primera_hispano=False, primera_mundial=False, pronombre=None, año_de_nacimiento=None, nacionalidad=None):
        self.fecha = fecha
        self.id_juego = id_juego
        self.id_runner = id_runner
        self.video_clips = video_clips
        self.primera_personal = primera_personal
        self.primera_hispano = primera_hispano
        self.primera_mundial = primera_mundial
        self.pronombre = pronombre
        self.año_de_nacimiento = año_de_nacimiento
        self.nacionalidad = nacionalidad

    def update(self, **kwargs):
        """Permite actualizar los atributos del objeto de manera progresiva"""
        for key, value in kwargs.items():
            if hasattr(self, key):  # Evita agregar atributos no definidos en la clase
                setattr(self, key, value)

    def __repr__(self):
        """Representación en string para depuración"""
        return f"PartidaDTO({self.__dict__})"