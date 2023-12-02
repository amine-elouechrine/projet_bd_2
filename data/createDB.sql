create table IF NOT EXISTS Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT,
    constraint pk_departements primary key (code_departement),
    constraint fk_region foreign key (code_region) references Regions(code_region) ON DELETE CASCADE ON UPDATE CASCADE
);

create table IF NOT EXISTS Regions (
    code_region INTEGER,
    nom_region TEXT,
    constraint pk_regions primary key (code_region)
);

create table IF NOT EXISTS Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    constraint pk_mesures primary key (code_departement, date_mesure) ,
    constraint fk_mesures foreign key (code_departement) references Departements(code_departement)ON DELETE CASCADE ON UPDATE CASCADE
);

create table IF NOT EXISTS Communes(
    code_commune Integer,
    code_departement TEXT,
    nom_commune TEXT,
    statue TEXT,
    altitude_moyenne FLOAT,
    population FLOAT,
    superffecie FLOAT,
    code_canton INTEGER,
    code_arrondissement INTEGER,
    CONSTRAINT PK_code_commune_code_departement_Communes PRIMARY KEY (code_commune,code_departement),
    CONSTRAINT FK_code_departement_Communes FOREIGN KEY (code_departement) REFERENCES Departements (code_departement) ON DELETE CASCADE ON UPDATE CASCADE
);

create table IF NOT EXISTS Traveaux (
    id_traveaux INTEGER  PRIMARY KEY AUTOINCREMENT,
    cout_taotal_ht FLOAT,
    cout_induit_ht  FLOAT,
    type_logement TEXT,
    annee_traveaux DATE,
    annee_construction_logement DATE,
    code_departement TEXT,
    code_region INTEGER,

    CONSTRAINT FK_code_departement_Traveaux FOREIGN KEY (code_departement) REFERENCES Departements (code_departement) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_code_region_Traveaux FOREIGN KEY (code_region) REFERENCES Regions (code_region) ON DELETE CASCADE ON UPDATE CASCADE
    );

create table IF NOT EXISTS Isolation (
    id_traveaux INTEGER,
    poste TEXT,
    isolant TEXT,
    epaisseur INTEGER,
    surface FLOAT,
    CONSTRAINT PK_id_Traveaux_Isolation PRIMARY KEY (id_traveaux),
    CONSTRAINT FK_id_traveaux_Isolation FOREIGN KEY (id_traveaux) REFERENCES Traveaux (id_traveaux) ON DELETE CASCADE ON update CASCADE
);

create table IF NOT EXISTS Chauffage (
    id_traveaux INTEGER,
    energie_avant_traveaux TEXT,
    energie_installe TEXT,
    generateur TEXT,
    type_chaudiere TEXT,
    CONSTRAINT PK_id_id_traveaux_Chauffage PRIMARY KEY (id_traveaux),
    CONSTRAINT FK_id_traveaux_Chauffage FOREIGN KEY (id_traveaux) REFERENCES Traveaux (id_traveaux) ON DELETE CASCADE ON UPDATE CASCADE
);

create table IF NOT EXISTS Photovoltaique(
    id_traveaux INTEGER,
    puissance_installe INTEGER,
    type_panneau TEXT,
    CONSTRAINT PK_id_traveaux_Photovoltaique PRIMARY KEY (id_traveaux),
    CONSTRAINT FK_id_traveaux_Photovoltaique FOREIGN KEY (id_traveaux) REFERENCES Traveaux (id_traveaux) ON DELETE CASCADE ON UPDATE CASCADE
);



