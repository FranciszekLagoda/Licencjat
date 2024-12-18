# Przegląd Projektu
Zapraszam do zapoznania się z moją analizą dotyczącą tego jak polski eksport i import reaguje na kryzysy gospodarcze w kraju trzecim. Projekt realizowany jest jako moja praca licencjacka na kierunku ekonomia na Uniwersytecie Ekonomicznym we Wrocławiu.

## Etapy analizy
Analiza została podzielona według metodologii analizy danych stosowanej w Google czyli:
1. Zapytaj
2. Przygotuj
3. Przetwórz
4. Analizuj
5. Podziel się
6. Działaj

# 1. Zapytaj
Pierwszy punkt analizy polega na identyfikacji kluczowych pytań, które są niezbędne do zbadania określonego zjawiska. W kontekście metodologii badań naukowych jest to zadanie pytań i hipotez badawczych.

## Główne pytanie badawcze
Jak polski eksport i import reagują na kryzysy gospodarcze w wybranych krajach trzecich, a jakie czynniki determinują różnice w tych reakcjach?

## Dopełniające pytania badawcze
* Jakie państwa prowadzą z Polską wystarczająco intensywną wymianę handlową aby nadawała się do skutecznej analizy?
* Co oznacza, i jak zidentyfikować pojawienie się w danym państwie kryzysu gospodarczego?
* Jakie były państwa spełniająca kryterium wielkości wymiany handlowej i zaistnienia kryzysu?
* Jaki był ogólny trend w różnicach między reakcją importu a eksportu na kryzys?
* Czy występowały prawidłowości pod względem zmiany w strukturze eksportu i importu?
* Czy informacja o zmianie wielkości eksportu do importu może być prognostykiem kryzysu gospodarczego?

## Hipotezy badawcze
* Kryzysy gospodarcze w krajach trzecich mają bezpośredni wpływ na zmiany w wartości polskiego eksportu do tych krajów, gdzie obserwuje się spadek eksportu w odpowiedzi na kryzys.
* Reakcja importu polskiego na kryzys gospodarczy w kraju trzecim jest mniej wrażliwa niż reakcja eksportu, co prowadzi do rozwoju deficytu handlowego w czasie kryzysów.
* Istnieje istotna różnica w strukturze towarowej eksportu i importu Polski w odpowiedzi na kryzysy gospodarcze w krajach trzecich, co może prowadzić do zmian w dominujących sektorach gospodarki.
* Zmiany w poziomie eksportu i importu mogą działać jako wczesne sygnały ostrzegawcze dla potencjalnych kryzysów gospodarczych w Polsce, umożliwiając wcześniejsze podjęcie działań prewencyjnych.

# 2. Przygotuj

## Dane dotyczące polskiej wymiany handlowej
### Dane
1. Pobrano do folderu 'Data_raw' dane z bazy danych o wysokiej wartości [GUS](https://dbw.stat.gov.pl/katalog/hvd) o Polskim eksporcie i imporcie towarami z lat 2012-2023.
2. Za pomocą [skryptu python](2_Przygotuj/Python_scripts/data_to_database.py) zaimportowano dane do [lokalnej bazy danych](2_Przygotuj/SQL_queries/create_trade_raw_table.sql) utworzonej w PostgreSQL i wstępnie je oczyszczono.
3. [Skrypt w SLQ](2_Przygotuj/SQL_queries/create_trade_table.sql) oczyścił dane, dodał do docelowej tabeli w bazie danych o nazwie "trade" oraz utworzył indeksy dla szybszego działania zapytań.
### Słownik
1. Pobrano odpowiednie słowniki GUS do danych oraz połączono je w [pliku Excela](Data_work/slownik.xlsx) oraz rozdzielono słownik na kategorie.
2. Korzystając z Chat GPT dodano kolumnę kontynent do do słownika.
3. Korzystając z formuł Excel i z edytora PowerQuery sformatowano słowniki.
4. Każdy słownik został zapisany oddzielnie jako plik csv w folderze [słowniki](2_Przygotuj/Slowniki).
5. [Skrypt w SQL](Data_work/create_slownik_tables.sql) utworzył odpowiednie tabele słowników i zapisał w nich dane.


## Jakie państwa prowadzą z Polską wystarczająco intensywną wymianę handlową aby nadawała się do skutecznej analizy
### Analiza teoretyczna

###
[link]()
