package com.fabianrodriguez.nohit.hispano.backend.commons;

import com.fabianrodriguez.nohit.hispano.backend.entity.*;
import java.util.List;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@Data
@NoArgsConstructor
public class InformacionDataBase {

	private List<Jugadores> jugadores;
	private List<Juegos> juegos;
	private List<Nacionalidad> nacionalidades;
	private List<Pronombre> pronombres;
}
