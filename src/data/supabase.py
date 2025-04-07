from dataclasses import asdict

from postgrest import APIError
from supabase import create_client, Client
import os

from src.models.supabase.run import Run

# Inicializar conexión con Supabase una sola vez
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

"""def insert_data_to_supabase(df):
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)
    data = df.to_dict(orient="records")
    response = supabase.table("tu_tabla").insert(data).execute()
    return response"""


def get_data(model_class):

    response = (supabase.table(model_class.TABLE_NAME).select("*").order("id").execute())

    return [model_class(**item) for item in response.data]


def registrar_partida(partida: Run):
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

    return response
