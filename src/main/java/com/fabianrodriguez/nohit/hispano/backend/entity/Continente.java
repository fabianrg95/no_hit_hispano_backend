package com.fabianrodriguez.nohit.hispano.backend.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.io.Serializable;
import java.util.Date;

@Entity
@Table(schema = "public", name = "continente")
@AllArgsConstructor
@NoArgsConstructor
@Data
@ToString
public class Continente implements Serializable {

    @Id
    private Long id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "fecha_insert")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaInsert;

}
