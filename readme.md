# Praca licencjacka

* Temat: Analiza zmienności handlu Polski w kontekście kryzysów gospodarczych
* Data rozpoczęcia: 02.12.2024
* Autor: Franciszek Łagoda

# Etap przygotowań
## Przygotowanie danych
1. Pobrano dane z bazdy danych o wysokiej wartości [GUS] (https://dbw.stat.gov.pl/katalog/hvd) o Polskim eksporcie i imporcie towarami z lat 2012-2023 oraz słownik, który został ręcznie uzupełniony o brakujące terminy.
2. Za pomocą [skryptu python](https://github.com/FranciszekLagoda/Licencjat/blob/4d8cf82a1277c711b99a1f90d7a03a33810ecea9/Data_work/data_to_database.py) zaimportowano dane do bazy danych i wstępnie je oczyszczono.
3. [Skrypt w SLQ](https://github.com/FranciszekLagoda/Licencjat/blob/4d8cf82a1277c711b99a1f90d7a03a33810ecea9/Data_work/create_trade_table.sql) dodał oczyszczone dane do docelowej tabeli "trade".

## Przygotowanie teorytyczne
1. Identyfikacja państw, z którymi Polska prowadziła wymianę handlową i napotkały kryzys.
