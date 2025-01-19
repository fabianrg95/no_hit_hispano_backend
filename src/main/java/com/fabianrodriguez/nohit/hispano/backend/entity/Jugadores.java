package com.fabianrodriguez.nohit.hispano.backend.entity;

import jakarta.persistence.*;
import java.io.Serializable;
import java.util.Date;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity
@Table(schema = "public", name = "jugadores")
@AllArgsConstructor
@NoArgsConstructor
@Data
@ToString
public class Jugadores implements Serializable {

    @Id
    private Long id;

    @Column(name = "nombre_usuario")
    private String nombreUsuario;

    @Column(name = "pronombre_id")
    private Long pronombreId;

    @Column(name = "anio_nacimiento")
    private String anioNacimiento;

    @Column(name = "nacionalidad_id")
    private Long nacionalidadId;

    @Column(name = "url_canal_youtube")
    private String urlCanalYoutube;

    @Column(name = "url_canal_twitch")
    private String urlCanalTwitch;

    @Column(name = "fecha_creacion")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaCreacion;

    @Column(name = "fecha_update")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaUpdate;

}
