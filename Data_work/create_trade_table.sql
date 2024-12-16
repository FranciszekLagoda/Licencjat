CREATE TABLE trade(
    id_zmienna INT,  
    id_kraj INT, --id_pozycja_2
    id_kategoria bigint, --id_pozycja_3
    id_miesiac INT, --id_okres
    rok INT, --id_daty
    wartosc NUMERIC
);
-- Dodawanie wartości z trade_raw
INSERT INTO trade (id_zmienna, id_kraj, id_kategoria, id_miesiac, rok, wartosc)
SELECT 
    id_zmienna, 
    id_pozycja_2 AS id_kraj, 
    id_pozycja_3 AS id_kategoria, 
    id_okres AS id_miesiac, 
    id_daty AS rok, 
    wartosc
FROM 
    trade_raw;

-- Zmiana wartosc z numeric na integer(big)
ALTER TABLE trade
ALTER COLUMN wartosc type bigint
using wartosc::bigint;

--Zmiana id_miesiąc na czytelny format
ALTER TABLE trade
ADD COLUMN miesiac INT;

UPDATE trade
SET miesiac = id_miesiac - 246;

ALTER TABLE trade
drop COLUMN id_miesiac;

ALTER TABLE trade
add column data DATE;

UPDATE trade
SET data = TO_DATE(rok::TEXT || '-' || miesiac::TEXT || '-01', 'YYYY-MM-DD');

ALTER TABLE trade
DROP COLUMN rok,
DROP COLUMN miesiac;

--Dodanie indeksów aby przyspieszyć działanie zapytań
CREATE index idx_kraj on trade (id_kraj);
CREATE index idx_kategoria on trade (id_kategoria);
CREATE index id_kraj_kategoria on trade(id_kraj,id_kategoria);
