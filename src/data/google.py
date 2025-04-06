import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

from src.models.excel.partida import Partida


def obtener_informacion_excel(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(os.getenv("GOOGLE_KEY")).worksheet(sheet_name)
    data = sheet.get_all_records()
    data_lower = [{k.lower().strip().replace(" ", "_"): v for k, v in row.items()} for row in data]
    return [Partida(**row) for row in data_lower if row.get('fecha') and row.get('juego') and row.get('runner')]
