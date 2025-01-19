package com.fabianrodriguez.nohit.hispano.backend.entity;

import jakarta.persistence.*;
import java.io.Serializable;
import java.util.Date;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity
@Table(schema = "public", name = "juegos")
@AllArgsConstructor
@NoArgsConstructor
@Data
@ToString
public class Juegos implements Serializable {

    @Id
    private Long id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "url_imagen")
    private String urlImagen;

    @Column(name = "oficial_team_hitless")
    private Boolean oficialTeamHitless;

    @Column(name = "fecha_insert")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaInsert;

    @Column(name = "fecha_update")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaUpdate;

    @Column(name = "subtitulo")
    private String subtitulo;

    @Column(name = "nombres_juego")
    private String nombresJuego;

}
