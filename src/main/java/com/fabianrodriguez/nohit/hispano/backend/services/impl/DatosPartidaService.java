package com.fabianrodriguez.nohit.hispano.backend.services.impl;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IDatosPartidaService;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IGoogleService;
import com.fabianrodriguez.nohit.hispano.backend.utils.MapperUtils;
import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
@AllArgsConstructor
public class DatosPartidaService implements IDatosPartidaService {

	private final IGoogleService googleService;
	private final MapperUtils mapperUtils;

	@Override
	public List<InformacionPartidaExcelDto> obtenerDatosExcel(final String Hoja) {
		log.info("Obteniendo todas las partidas de la hoja de excel");
		List<InformacionPartidaExcelDto> registrosPartidas = new ArrayList<>();
		try {
			List<List<Object>> informacionArchivo = googleService.leerExcel(Hoja);
			if (Objects.nonNull(informacionArchivo) && informacionArchivo.size() > 0) {
				registrosPartidas = mapperUtils.mapearInformacionPartidasExcel(informacionArchivo);
			}


		} catch (IOException | GeneralSecurityException e) {
			log.error("Error al momento de intentar obtener la informacion del archivo de google", e);
		}
		return registrosPartidas;
	}


}
