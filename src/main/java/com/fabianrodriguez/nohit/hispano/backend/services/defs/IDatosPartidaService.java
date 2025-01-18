package com.fabianrodriguez.nohit.hispano.backend.services.defs;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import java.util.List;

public interface IDatosPartidaService {
	List<InformacionPartidaExcelDto> obtenerDatosExcel(final String hoja);
}
