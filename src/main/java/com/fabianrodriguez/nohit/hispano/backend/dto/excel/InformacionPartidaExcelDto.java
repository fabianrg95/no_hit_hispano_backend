package com.fabianrodriguez.nohit.hispano.backend.dto.excel;

import java.io.Serial;
import java.io.Serializable;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class InformacionPartidaExcelDto implements Serializable {

	@Serial
	private static final long serialVersionUID = -7041764680892447579L;

	private String fecha;
	private String juego;
	private String nombrePartida;
	private String jugador;
	private String primeroPersonal;
	private String primeroHispano;
	private String primeroMundial;
	private String urlYoutube;
	private String urlTwitch;
	private String pronombreJugador;
	private String anioNacimientoJugador;
	private String NacionalidadJugador;

	public InformacionPartidaExcelDto(final List<Object> registroExcel) {
		this.fecha = (String) registroExcel.get(0);
		this.juego = (String) registroExcel.get(1);
		this.nombrePartida = (String) registroExcel.get(2);
		this.jugador = (String) registroExcel.get(3);
		this.primeroPersonal = (String) registroExcel.get(4);
		this.primeroHispano = (String) registroExcel.get(5);
		this.primeroMundial = (String) registroExcel.get(6);
		this.urlYoutube = obtenerValorOpcional(registroExcel, 7);
		this.urlTwitch = obtenerValorOpcional(registroExcel, 8);
		this.pronombreJugador = obtenerValorOpcional(registroExcel, 9);
		this.anioNacimientoJugador = obtenerValorOpcional(registroExcel, 10);
		this.NacionalidadJugador = obtenerValorOpcional(registroExcel, 11);
	}

	private static String obtenerValorOpcional(final List<Object> list, final int index) {
		return (index < list.size() && list.get(index) != null) ? list.get(index).toString() : "";
	}
}
