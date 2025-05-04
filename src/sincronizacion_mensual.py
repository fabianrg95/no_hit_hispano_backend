from datetime import datetime

from data.google import obtener_informacion_excel_por_hoja
from src.models.excel.partida_excel import PartidaExcel
from src.notificador.notificador import notificar_error_discord, notificar_exito_discord
from src.services.procesamiento import procesar_registro_partida
from src.data.supabase import obtener_informacion_tabla
from src.models.supabase.juego import Juego
from src.models.supabase.jugador import Jugador
from src.utils.data_store import DataStore
from src.utils.constantes import meses_es


def main():
    print("Inicializando memoria")
    data_store = DataStore()

    cargar_informacion_base_memoria(data_store)
    datos_excel = obtener_informacion_excel()
    procesar_registro_partida(datos_excel)
    notificar_error_discord()
    notificar_exito_discord()


def cargar_informacion_base_memoria(data_store):
    print("""-----------------------------------------------------------------------------
Realizando el cargue inicial de informacion con base en excel y base de datos
-----------------------------------------------------------------------------""")
    ##print("Cargando los continentes en memoria")
    ##data_store.cargar_continentes(get_data(Continente))

    print("Cargando los juegos en memoria")
    data_store.cargar_juegos(obtener_informacion_tabla(Juego))

    print("Cargando los jugadores en memoria")
    data_store.cargar_jugadores(obtener_informacion_tabla(Jugador))

    ##print("Cargando las nacionalidades en memoria")
    ##data_store.cargar_nacionalidades(get_data(Nacionalidad))

    ##print("Cargando los pronombres en memoria")
    ##data_store.cargar_pronombres(get_data(Pronombre))

def obtener_informacion_excel()-> [PartidaExcel]:
    mes_actual = meses_es[datetime.now().month - 1]
    print("Obteniendo del ("+mes_actual+") desde el excel.")

    return obtener_informacion_excel_por_hoja(mes_actual)


if __name__ == "__main__":
    main()