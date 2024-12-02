import os
import csv
import psycopg2

def upload_files_to_database(folder_path, columns_to_remove):
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
                    
                    # Zbuduj nowy nagłówek usuwając wybrane kolumny
                    included_columns = [i for i in range(len(header)) if i not in columns_to_remove]
                    
                    # Zmiana float na integer w każdej linii i zapisanie do bazy
                    for row in reader:
                        # Ignoruj puste wiersze
                        if not row:
                            continue

                        modified_row = []
                        for i, col in enumerate(row):
                            if i in included_columns:
                                if i == 25:  # Index kolumny 'wartosc'
                                    try:
                                        # Konwersja na float, zaokrąglenie do najbliższej liczby całkowitej
                                        int_value = round(float(col.replace(',', '.')))  # Zamień przecinek na kropkę
                                        modified_row.append(int_value)
                                    except ValueError:
                                        print(f"Błąd konwersji wartości '{col}' w pliku '{filename}' wiersz '{row}'")
                                        modified_row.append(None)  # lub inną wartość, jeśli nie chcesz None
                                else:
                                    modified_row.append(col)  # Dodaj inne wartości bez zmian
                            else:
                                modified_row.append(None)  # Dodaj None do kolumn usuniętych

                        # Insert do bazy danych (zakładając, że tabela ma odpowiednią strukturę)
                        cursor.execute("""
                            INSERT INTO trade (id_zmienna, id_przekroj, wartosc)  -- Dodaj inne kolumny, które chcesz
                            VALUES (%s, %s, %s)
                        """, (modified_row[1], modified_row[2], modified_row[25]))  # Dopasuj kolejność

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

# Indeksy kolumn do usunięcia (np. jakie kolumny chcesz wyłączyć)
columns_to_remove = [0,2,3,4,5,7,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,26,28,29]  # Na przykład usuwamy rowNumber; szereg innych indeksów w zależności od potrzeb

upload_files_to_database(folder_path, columns_to_remove)