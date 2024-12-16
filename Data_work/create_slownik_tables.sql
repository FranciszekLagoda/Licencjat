-- Stworzenie tabel slownika

CREATE TABLE slownik_kraj (
    id_kraj int,
    kraj varchar,
    czy_kraj BOOLEAN,
    kontynent VARCHAR,
    czy_UE BOOLEAN
);

CREATE TABLE slownik_kategoria (
    id_kategoria bigint,
    towar_nr VARCHAR,
    towar VARCHAR,
    towar_lista VARCHAR
);

CREATE TABLE  slownik_zmienna (
    id_zmienna INT,
    zmienna VARCHAR
);


-- Załadowanie danych ze slownika do odpowiednich tabel

COPY slownik_kraj
FROM 'Data_work\Slowniki\slownik_kraje.csv'
WITH (Format csv, Delimiter ',', encoding 'UTF8', Header);



