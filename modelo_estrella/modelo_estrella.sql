CREATE TABLE Dim_Tiempo (
    id_tiempo SERIAL PRIMARY KEY,
    anio INT UNIQUE
);

CREATE TABLE Dim_Indicador (
    id_indicador SERIAL PRIMARY KEY,
    codigo_indicador VARCHAR(20) UNIQUE,
    nombre_indicador TEXT,
    unidad VARCHAR(20),
    fuente TEXT
);

CREATE TABLE Dim_Region (
    id_region SERIAL PRIMARY KEY,
    codigo_region VARCHAR(10) UNIQUE,
    nombre_region TEXT
);

CREATE TABLE Hechos_Economicos (
    id_hechos_economicos SERIAL PRIMARY KEY,
    id_tiempo INT NOT NULL,
    id_indicador INT NOT NULL,
    id_region INT NOT NULL,
    valor NUMERIC,
    FOREIGN KEY (id_tiempo) REFERENCES Dim_Tiempo(id_tiempo),
    FOREIGN KEY (id_indicador) REFERENCES Dim_Indicador(id_indicador),
    FOREIGN KEY (id_region) REFERENCES Dim_Region(id_region)
);