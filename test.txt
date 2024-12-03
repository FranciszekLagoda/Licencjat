SELECT
    count(*),
    id_daty
from trade_raw
WHERE 
    id_pozycja_2 = 6649664
    AND
    id_pozycja_3 = 7438267
GROUP BY id_daty;


SELECT *
FROM trade
limit 5;