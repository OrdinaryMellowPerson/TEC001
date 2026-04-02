def caesar_cipher(filename, shift_positions, direction):
    if direction.lower() == "right":
        n = shift_positions
    elif direction.lower() == "left":
        n = -shift_positions
    else:
        print("Error: Direction must be 'left' or 'right'.")
        return

    output_filename = "cipher_" + filename

    try:
        with open(filename, 'r', encoding='utf-8') as infile, \
                open(output_filename, 'w', encoding='utf-8') as outfile:

            for line in infile:
                cipher_line = ""
                for char in line:
                    if char.isalpha():
                        x = ord(char)
                        if char.isupper():
                            y = (x - 65 + n) % 26 + 65
                            cipher_line += chr(y)
                        elif char.islower():
                            y = (x - 97 + n) % 26 + 97
                            cipher_line += chr(y)
                    else:
                        cipher_line += char
                outfile.write(cipher_line)
        print(f"Success! Ciphertext saved to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == "__main__":
    caesar_cipher('task4_test.txt', 3, 'right')