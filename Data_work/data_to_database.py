import os
import csv
import psycopg2

def upload_files_to_database(folder_path):
    try:
        # Połącz z bazą danych PostgreSQL
        conn = psycopg2.connect(
            dbname="licencjat",
            user="postgres",
            password="321Kenarfsql?",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Iteruj przez wszystkie pliki w folderze
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Sprawdź, czy to plik CSV (pomijanie folderów)
            if os.path.isfile(file_path) and filename.endswith('.csv'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=';')  # Użyj delimitera ';'
                    header = next(reader)  # Odczytaj nagłówki
                    
                    # Zmiana float na integer w każdej linii i zapisanie do bazy
                    for row in reader:
                        # Ignoruj puste wiersze
                        if not row:
                            continue
                        
                        modified_row = []
                        try:
                            # Zbieraj i konwertuj dane do zmiennej modified_row
                            id_zmienna = int(row[1])  # id_zmienna
                            id_kraj = int(row[5])      # id_pozycja_2 -> id_kraj
                            id_kategoria = int(row[6])  # id_pozycja_3 -> id_kategoria
                            id_miesiac = int(row[21])   # id_okres
                            rok = int(row[22])          # id_daty
                            wartosc = round(float(row[25].replace(',', '.')))  # wartosc, zamień przecinek na kropkę i zaokrąglij

                            modified_row = (id_zmienna, id_kraj, id_kategoria, id_miesiac, rok, wartosc)

                            # Insert do bazy danych
                            cursor.execute("""
                                INSERT INTO trade (id_zmienna, id_kraj, id_kategoria, id_miesiac, rok, wartosc)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, modified_row)
                            
                        except (ValueError, IndexError) as e:
                            print(f"Błąd przy przetwarzaniu wiersza {row} w pliku '{filename}': {e}")
                            continue

                # Informuj o załadowanym pliku
                print(f"Plik '{filename}' został pomyślnie załadowany do bazy danych.")

        # Zatwierdź transakcje
        conn.commit()

    except Exception as e:
        # W przypadku błędu wypisz go i wyjdź z programu
        print(f"Wystąpił błąd: {e}")
    finally:
        # Zamknij połączenie przy zakończeniu operacji
        cursor.close()
        conn.close()

# Ścieżka do folderu z plikami
folder_path = r'C:\Dokumenty\Licencjat\Data_raw'

upload_files_to_database(folder_path)