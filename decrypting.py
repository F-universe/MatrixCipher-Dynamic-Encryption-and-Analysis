import os

def decrypt_message(data_file, encrypted_file, output_file):
    try:
        # Leggi i numeri da data.txt
        with open(data_file, 'r', encoding='utf-8') as df:
            number_lines = [line.strip().split() for line in df.readlines()]
        
        # Appiattisci i numeri in una lista
        numbers = [int(num) for sublist in number_lines for num in sublist]

        # Leggi il messaggio crittografato
        with open(encrypted_file, 'r', encoding='utf-8') as ef:
            encrypted_message = ef.read()

        # Decrittazione del messaggio
        decrypted_message = []
        for i, char in enumerate(encrypted_message):
            shift = numbers[i % len(numbers)]  # Usa i numeri come offset ciclicamente
            decrypted_char = chr((ord(char) - shift) % 256)  # Sposta indietro il carattere
            decrypted_message.append(decrypted_char)

        # Scrivi il messaggio decrittografato in un nuovo file
        with open(output_file, 'w', encoding='utf-8') as of:
            of.write(''.join(decrypted_message))

        print(f"Messaggio decrittografato salvato in: {output_file}")

    except FileNotFoundError as e:
        print(f"Errore: {e}")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Percorsi dei file
data_file_path = r'C:\Users\Fabio\Desktop\crypto\data.txt'
encrypted_file_path = r'C:\Users\Fabio\Desktop\crypto\cripted\cripted_message.txt'
output_file_path = r'C:\Users\Fabio\Desktop\crypto\decrypted_message.txt'

# Esegui la funzione
decrypt_message(data_file_path, encrypted_file_path, output_file_path)
