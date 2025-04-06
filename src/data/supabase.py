from src.models.supabase.continente import Continente
from src.models.supabase.juego import Juego
from supabase import create_client, Client
import os

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
