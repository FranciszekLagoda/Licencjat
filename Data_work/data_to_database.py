import os
import psycopg2

# Ustawienia połączenia z bazą danych
conn = psycopg2.connect(
    dbname='licencjat',
    user='postgres',
    password='321Kenarfsql?',
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
                # Zastosowanie replace do konwersji przecinków na kropki
                content = f.read().replace(',', '.')
                cur.copy_expert("COPY trade_raw FROM STDIN WITH CSV HEADER DELIMITER ';'", f)  # Użyj 'f', zamiast 'content'
                # Informowanie o udanym imporcie
                print(f"Zaimportowano plik: {filename}")
        except Exception as e:
            # Informowanie o błędzie podczas importu
            print(f"Błąd przy imporcie pliku {filename}: {e}")

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
cur.close()
conn.close()