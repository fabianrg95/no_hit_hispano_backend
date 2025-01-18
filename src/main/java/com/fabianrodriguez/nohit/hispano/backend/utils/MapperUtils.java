package com.fabianrodriguez.nohit.hispano.backend.utils;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import java.util.List;
import java.util.stream.Collectors;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.util.ObjectUtils;

@Slf4j
@Component
public class MapperUtils {

	protected MapperUtils() {
	}

	public static List<InformacionPartidaExcelDto> mapearInformacionPartidasExcel(List<List<Object>> informacionArchivo) {
		List<InformacionPartidaExcelDto> registrosPartidas;
		registrosPartidas = informacionArchivo.stream().skip(1).filter(registroExcel -> !ObjectUtils.isEmpty(registroExcel)
				&& !ObjectUtils.isEmpty(registroExcel.get(0))
				&& !ObjectUtils.isEmpty(registroExcel.get(1))
				&& !ObjectUtils.isEmpty(registroExcel.get(3))).map(InformacionPartidaExcelDto::new).collect(Collectors.toList());
		return registrosPartidas;
	}
}
