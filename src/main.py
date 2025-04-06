import locale
from datetime import datetime

from data.google import obtener_informacion_excel
from data.procesamiento import process_data
from src.data.supabase import get_data
from src.models.supabase.continente import Continente
from src.models.supabase.juego import Juego
from src.models.supabase.jugador import Jugador
from src.models.supabase.nacionalidad import Nacionalidad
from src.models.supabase.pronombre import Pronombre
from src.utils.data_store import DataStore


def main():
    print("Inicializando memoria")
    data_store = DataStore()

    cargar_informacion_base_memoria(data_store)
    cargar_informacion_excel_memoria(data_store)
    process_data()


def cargar_informacion_base_memoria(data_store):
    print("""-----------------------------------------------------------------------------
Realizando el cargue inicial de informacion con base en excel y base de datos
-----------------------------------------------------------------------------""")
    ##print("Cargando los continentes en memoria")
    ##data_store.cargar_continentes(get_data(Continente))

    print("Cargando los juegos en memoria")
    data_store.cargar_juegos(get_data(Juego))

    print("Cargando los jugadores en memoria")
    data_store.cargar_jugadores(get_data(Jugador))

    ##print("Cargando las nacionalidades en memoria")
    ##data_store.cargar_nacionalidades(get_data(Nacionalidad))

    ##print("Cargando los pronombres en memoria")
    ##data_store.cargar_pronombres(get_data(Pronombre))

def cargar_informacion_excel_memoria(data_store):
    mes_actual = data_store.obtener_meses_es()[datetime.now().month - 1]
    print("Cargando la informacion del mes actual ("+mes_actual+") en memoria")

    data_store.cargar_partidas_a_procesar(obtener_informacion_excel(mes_actual))


if __name__ == "__main__":
    main()