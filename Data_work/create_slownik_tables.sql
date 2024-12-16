-- Stworzenie tabel slownika

CREATE TABLE slownik_kraj (
    id_kraj int,
    kraj varchar
);

CREATE TABLE slownik_kategoria (
    id_kategoria bigint,
    towar_nr INT,
    towar VARCHAR,
    towar_full VARCHAR
);

CREATE TABLE  slownik_zmienna (
    id_zmienna INT,
    zmienna VARCHAR
);


-- Załadowanie danych ze slownika do odpowiednich tabel



