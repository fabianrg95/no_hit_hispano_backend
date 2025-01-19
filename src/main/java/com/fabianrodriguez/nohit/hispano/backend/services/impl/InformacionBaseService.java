package com.fabianrodriguez.nohit.hispano.backend.services.impl;

import com.fabianrodriguez.nohit.hispano.backend.commons.InformacionDataBase;
import com.fabianrodriguez.nohit.hispano.backend.entity.Juegos;
import com.fabianrodriguez.nohit.hispano.backend.entity.Jugadores;
import com.fabianrodriguez.nohit.hispano.backend.entity.Nacionalidad;
import com.fabianrodriguez.nohit.hispano.backend.entity.Pronombre;
import com.fabianrodriguez.nohit.hispano.backend.repositories.JuegosRepository;
import com.fabianrodriguez.nohit.hispano.backend.repositories.JugadoresRepository;
import com.fabianrodriguez.nohit.hispano.backend.repositories.NacionalidadRepository;
import com.fabianrodriguez.nohit.hispano.backend.repositories.PronombreRepository;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Slf4j
@AllArgsConstructor
public class InformacionBaseService implements CommandLineRunner {

	private final InformacionDataBase informacionDataBase;
	private final JuegosRepository juegosRepository;
	private final JugadoresRepository jungadoresRepository;
	private final NacionalidadRepository nacionalidadRepository;
	private final PronombreRepository pronombreRepository;

	@Override
	public void run(String... args) throws Exception {
		log.info("Cargando en memoria todos los juegos registrados");
		informacionDataBase.setJuegos(obtenerTodosJuegos());
		log.info("Se cargaron {} juegos en memoria", informacionDataBase.getJuegos().size());

		log.info("Cargando en memoria todos los jugadores registrados");
		informacionDataBase.setJugadores(obtenerTodosJugadores());
		log.info("Se cargaron {} jugadores en memoria", informacionDataBase.getJugadores().size());

		log.info("Cargando en memoria todas las nacionalidades registradas");
		informacionDataBase.setNacionalidades(obtenerTodasNacionalidades());
		log.info("Se cargaron {} nacionalidades en memoria", informacionDataBase.getNacionalidades().size());

		log.info("Cargando en memoria todos los pronombres registrados");
		informacionDataBase.setPronombres(obtenerTodosPronombres());
		log.info("Se cargaron {} pronombres en memoria", informacionDataBase.getPronombres().size());
	}

	@Transactional(readOnly = true)
	public List<Juegos> obtenerTodosJuegos() {
		return juegosRepository.findAll();
	}

	@Transactional(readOnly = true)
	public List<Jugadores> obtenerTodosJugadores() {
		return jungadoresRepository.findAll();
	}

	@Transactional(readOnly = true)
	public List<Nacionalidad> obtenerTodasNacionalidades() {
		return nacionalidadRepository.findAll();
	}

	@Transactional(readOnly = true)
	public List<Pronombre> obtenerTodosPronombres() {
		return pronombreRepository.findAll();
	}


}
