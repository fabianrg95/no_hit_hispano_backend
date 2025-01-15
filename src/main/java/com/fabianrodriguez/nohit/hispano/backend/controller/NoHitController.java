package com.fabianrodriguez.nohit.hispano.backend.controller;

import com.fabianrodriguez.nohit.hispano.backend.services.ContinenteService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class NoHitController {

    private final ContinenteService continenteService;

    @GetMapping("/continentes")
    private void obtenerContinentes() {
        continenteService.obtenerContinentes();
    }
}
