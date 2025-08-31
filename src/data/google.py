import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

from src.models.excel.partida_excel import PartidaExcel

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credenciales = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
cliente = gspread.authorize(credenciales).open_by_key(os.getenv("GOOGLE_KEY"))

def obtener_informacion_excel_por_hoja(nombre_hoja: str) -> [PartidaExcel]:
    try:
        datos = cliente.worksheet(nombre_hoja).get_all_records()
        return [
            PartidaExcel(**row)
            for row in __normalizar_datos_excel(datos)
            if __registro_valido(row)
        ]
    except gspread.exceptions.WorksheetNotFound:
        # Si la hoja no existe, retorna lista vacía
        return []

##valida si un registro es valido cuando posee valor en fecha, juego y jugador (runner)
def __registro_valido(row):
    return row.get('fecha') and row.get('juego') and row.get('runner')

##normaliza el nombre de cada propiedad dejandolo en minustula y los espacios se remplazan por _
##el valor de cada celda se daja tal cual viene, solo se normaliza la cabecera de los registros
def __normalizar_datos_excel(data):
    return [{columna.lower().strip().replace(" ", "_"): valor_celda for columna, valor_celda in registro.items()} for registro in data]
