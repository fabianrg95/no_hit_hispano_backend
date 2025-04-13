from postgrest import APIError
from supabase import create_client, Client
from src.models.supabase.run import Run
import os


# Inicializar conexión con Supabase una sola vez
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def obtener_informacion_tabla(entidad):

    response = (supabase.table(entidad.TABLE_NAME).select("*").order("id").execute())

    return [entidad(**item) for item in response.data]


def registrar_partida(partida: Run):
    ##se elimina la propiedad id del diccionario de datos para que la base de datos la cree automaticamente
    del partida.__dict__['id']
    try:
        response = (
        supabase.table(Run.TABLE_NAME)
        .upsert(partida.__dict__)
        .execute()
    )
        print("Partida registrada de forma exitosa...")
        return True
    except APIError as e:
        if e.code == "23505":
            print("Partida ya existente, se ignora.")
            return False
        else:
            raise e
