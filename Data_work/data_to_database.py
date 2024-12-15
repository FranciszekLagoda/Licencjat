import os
import psycopg2
from config import DATABASE_PASSWORD

# Ustawienia połączenia z bazą danych
conn = psycopg2.connect(
    dbname='licencjat',
    user='postgres',
    password=DATABASE_PASSWORD,
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Ścieżka do folderu z plikami CSV
folder_path = r'C:\Dokumenty\Licencjat\Data_raw'

# Iterowanie przez pliki w folderze
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r') as f:
                # Odczyt danych i zamiana przecinków na kropki
                content = f.read().replace(',', '.')
                
                # Tworzymy tymczasowy plik do przechowywania zmodyfikowanych danych
                temp_file_path = file_path.replace('.csv', '_temp.csv')
                with open(temp_file_path, 'w') as temp_file:
                    temp_file.write(content)

                # Import danych do tabeli trade_raw z tymczasowego pliku
                with open(temp_file_path, 'r') as temp_file:
                    cur.copy_expert("COPY trade_raw FROM STDIN WITH CSV HEADER DELIMITER ';'", temp_file)

                # Informowanie o udanym imporcie
                print(f"Zaimportowano plik: {filename}")

                # Usuwamy tymczasowy plik
                os.remove(temp_file_path)
        except Exception as e:
            # Informowanie o błędzie podczas importu
            print(f"Błąd przy imporcie pliku {filename}: {e}")

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
cur.close()
conn.close()