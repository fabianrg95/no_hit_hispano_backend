package com.fabianrodriguez.nohit.hispano.backend.controller;

import com.fabianrodriguez.nohit.hispano.backend.dto.excel.InformacionPartidaExcelDto;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IDatosPartidaService;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Locale;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class NoHitController {

	private final IDatosPartidaService datosPartidasService;

	@GetMapping("/obtener-datos-excel-mes-actual")
	public ResponseEntity<List<InformacionPartidaExcelDto>> obtenerDatosExcel(){

		final LocalDate fechaActual = LocalDate.now();
		final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM", Locale.forLanguageTag("es"));
		final String mes = fechaActual.format(formatter);

		return ResponseEntity.ok()
				.header(HttpHeaders.CONTENT_TYPE, "application/json; charset=UTF-8")
				.body(datosPartidasService.obtenerDatosExcel(mes.substring(0, 1).toUpperCase() + mes.substring(1)));
	}
}
