class Partida:

    def __init__(self, fecha, juego, run, runner, run_youtube, clip_twitch, pronombre, año_de_nacimiento, nacionalidad,
                 personal_1st:bool, hispano_1st:bool,world_1st:bool, **kwargs):
        self.fecha = fecha
        self.juego = juego
        self.run = run
        self.runner = runner
        self.run_youtube = run_youtube
        self.run_twitch = clip_twitch
        self.pronombre = pronombre
        self.año_de_nacimiento = año_de_nacimiento
        self.nacionalidad = nacionalidad
        self.personal_1st = personal_1st == "TRUE"
        self.hispano_1st = hispano_1st == "TRUE"
        self.world_1st = world_1st == "TRUE"

    def __repr__(self):
        return (f"Partida(fecha={self.fecha}, juego={self.juego}, run={self.run}, runner={self.runner}, "
                f"run_youtube=<{self.run_youtube}>, run_twitch=<{self.run_twitch}>, pronombre={self.pronombre}, "
                f"fecha_nacimiento={self.año_de_nacimiento}, nacionalidad={self.nacionalidad}, "
                f", personal_1st={self.personal_1st}, , hispano_1st={self.hispano_1st}, , world_1st={self.world_1st})")