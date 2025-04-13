from src.models.dto.partida_dto import PartidaDTO
from src.models.excel.partida_excel import PartidaExcel
from src.models.supabase.run import Run
from src.utils.data_store import DataStore
from src.utils.normalizador import normalizar_texto, buscar_juego_por_nombre, buscar_jugador_por_nombre, \
    normalizar_links_videos, normalizar_fecha_partida

data_store = DataStore()

def partida_excel_a_partida_dto(partida: PartidaExcel):
    nombre_juego_normalizado = normalizar_texto(partida.juego)
    partida_dto = PartidaDTO()
    partida_dto.update(fecha=partida.fecha)
    partida_dto.update(id_juego=buscar_juego_por_nombre(nombre_juego_normalizado))
    partida_dto.update(nombre_partida=partida.run)
    partida_dto.update(id_runner=buscar_jugador_por_nombre(partida.runner))
    partida_dto.update(video_clips=normalizar_links_videos(partida))
    partida_dto.update(primera_personal=partida.personal_1st)
    partida_dto.update(primera_hispano=partida.hispano_1st)
    partida_dto.update(primera_mundial=partida.world_1st)
    partida_dto.update(pronombre=partida.pronombre)
    partida_dto.update(año_de_nacimiento=partida.año_de_nacimiento)
    partida_dto.update(nacionalidad=partida.nacionalidad)
    return partida_dto

def partida_dto_a_partida_db(partida_dto: PartidaDTO) -> Run:
    return Run(fecha_partida=normalizar_fecha_partida(partida_dto.fecha).strftime("%Y-%m-%d"),
              juego_id=partida_dto.id_juego,
              nombre_partida=partida_dto.nombre_partida,
              jugador_id=partida_dto.id_runner,
              primera_partida_personal=partida_dto.primera_personal,
              primera_partida_hispano=partida_dto.primera_hispano,
              primera_partida_mundial=partida_dto.primera_mundial,
              videos_clips=partida_dto.video_clips)
