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
@Table(schema = "public", name = "pronombre")
@AllArgsConstructor
@NoArgsConstructor
@Data
@ToString
public class Pronombre implements Serializable {

    @Id
    private Long id;

    @Column(name = "pronombre")
    private String pronombre;

    @Column(name = "genero")
    private String genero;

}
