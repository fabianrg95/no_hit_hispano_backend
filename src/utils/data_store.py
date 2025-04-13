class DataStore:
    _instance = None  # Variable estática para la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
            cls._instance.continentes = []
            cls._instance.juegos = []
            cls._instance.jugadores = []
            cls._instance.nacionalidades = []
            cls._instance.pronombres = []
            cls._instance.partidas_procesar = []
        return cls._instance

    def cargar_continentes(self, continentes):
        self.continentes = continentes

    def cargar_juegos(self, juegos):
        self.juegos = juegos

    def cargar_jugadores(self, jugadores):
        self.jugadores = jugadores

    def cargar_nacionalidades(self, nacionalidades):
        self.nacionalidades = nacionalidades

    def cargar_pronombres(self, pronombres):
        self.pronombres = pronombres

    def cargar_partidas_a_procesar(self, partidas):
        self.partidas_procesar = partidas

    def obtener_continentes(self):
        return self.continentes

    def obtener_juegos(self):
        return self.juegos

    def obtener_jugadores(self):
        return self.jugadores

    def obtener_nacionalidades(self):
        return self.nacionalidades

    def obtener_pronombres(self):
        return self.pronombres

    def obtener_partidas_a_procesar(self):
        return self.partidas_procesar