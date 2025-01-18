package com.fabianrodriguez.nohit.hispano.backend.controller;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IDatosPartidaService;
import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.List;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class NoHitController {

	private final IDatosPartidaService datosPartidasService;

	@GetMapping("/obtener-datos-excel")
	public List<InformacionPartidaExcelDto> obtenerDatosExcel() throws GeneralSecurityException, IOException {
		return datosPartidasService.obtenerDatosExcel();
	}
}
