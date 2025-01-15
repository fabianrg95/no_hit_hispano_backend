package com.fabianrodriguez.nohit.hispano.backend.services.impl;

import com.fabianrodriguez.nohit.hispano.backend.repositories.ContinenteRepository;
import com.fabianrodriguez.nohit.hispano.backend.services.defs.IContinenteService;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
@AllArgsConstructor
public class ContinenteService implements IContinenteService {

	private final ContinenteRepository continenteRepository;

	@Override
	public void obtenerContinentes() {
		log.info("Obteniendo todas las continentes");
		continenteRepository.findAll().forEach(continente -> {
			log.info(continente.toString());
		});
	}
}
