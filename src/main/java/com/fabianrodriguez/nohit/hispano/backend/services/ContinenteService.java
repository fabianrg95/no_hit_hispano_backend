package com.fabianrodriguez.nohit.hispano.backend.services;

import com.fabianrodriguez.nohit.hispano.backend.repositories.ContinenteRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class ContinenteService {

    @Autowired
    private ContinenteRepository continenteRepository;

    public void obtenerContinentes() {
        log.info("Obteniendo todas las continentes");
        continenteRepository.findAll().forEach(continente -> {log.info(continente.toString());});
    }
}
