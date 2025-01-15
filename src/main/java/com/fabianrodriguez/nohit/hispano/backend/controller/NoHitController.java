package com.fabianrodriguez.nohit.hispano.backend.controller;

import com.fabianrodriguez.nohit.hispano.backend.services.defs.IContinenteService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class NoHitController {

	private final IContinenteService continenteService;

	@GetMapping("/continentes")
	public void obtenerContinentes() {
		continenteService.obtenerContinentes();
	}
}
