import os

def encrypt_message(data_file, text_file, output_file):
    try:
        # Read the numbers from data.txt
        with open(data_file, 'r', encoding='utf-8') as df:
            number_lines = [line.strip().split() for line in df.readlines()]
        
        # Flatten the numbers into a single list
        numbers = [int(num) for sublist in number_lines for num in sublist]

        # Read the message from T.txt
        with open(text_file, 'r', encoding='utf-8') as tf:
            message = tf.read()

        # Encrypt the message
        encrypted_message = []
        for i, char in enumerate(message):
            shift = numbers[i % len(numbers)]  # Use the numbers cyclically as an offset
            encrypted_char = chr((ord(char) + shift) % 256)  # Shift the character
            encrypted_message.append(encrypted_char)

        # Write the encrypted message to a new file
        with open(output_file, 'w', encoding='utf-8') as of:
            of.write(''.join(encrypted_message))

        print(f"Encrypted message saved to: {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
# Correct file paths for Windows
data_file_path = r'C:\Users\Fabio\Desktop\crypto\data.txt'
text_file_path = r'C:\Users\Fabio\Desktop\crypto\T.txt'
output_file_path = r'C:\Users\Fabio\Desktop\crypto\cripted\cripted_message.txt'

# Execute the function
encrypt_message(data_file_path, text_file_path, output_file_path)
