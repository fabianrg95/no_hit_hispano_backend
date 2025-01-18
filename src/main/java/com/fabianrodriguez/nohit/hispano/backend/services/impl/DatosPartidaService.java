package com.fabianrodriguez.nohit.hispano.backend.services.impl;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IDatosPartidaService;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IGoogleService;
import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;

@Service
@Slf4j
@AllArgsConstructor
public class DatosPartidaService implements IDatosPartidaService {

	private final IGoogleService googleService;

	@Override
	public List<InformacionPartidaExcelDto> obtenerDatosExcel() {
		log.info("Obteniendo todas las partidas de la hoja de excel");
		List<InformacionPartidaExcelDto> registrosPartidas = new ArrayList<>();
		try {
			List<List<Object>> informacionArchivo = googleService.leerExcel();
			if (Objects.nonNull(informacionArchivo) && informacionArchivo.size() > 0) {
				registrosPartidas = informacionArchivo.stream().skip(1).filter(registroExcel -> !ObjectUtils.isEmpty(registroExcel)
						&& !ObjectUtils.isEmpty(registroExcel.get(0))
						&& !ObjectUtils.isEmpty(registroExcel.get(1))
						&& !ObjectUtils.isEmpty(registroExcel.get(3))).map(InformacionPartidaExcelDto::new).collect(Collectors.toList());
			}


		} catch (IOException | GeneralSecurityException e) {
			log.error("Error al momento de intentar obtener la informacion del archivo de google", e);
		}
		return registrosPartidas;
	}
}
