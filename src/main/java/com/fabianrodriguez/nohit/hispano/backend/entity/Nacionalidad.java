package com.fabianrodriguez.nohit.hispano.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.io.Serializable;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity
@Table(schema = "public", name = "nacionalidad")
@AllArgsConstructor
@NoArgsConstructor
@Data
@ToString
public class Nacionalidad implements Serializable {

    @Id
    private Long id;

    @Column(name = "pais")
    private String pais;

    @Column(name = "gentilicio_femenino")
    private String gentilicioFemenino;

}
