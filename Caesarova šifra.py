def caesar_cipher(text, shift, mode='encrypt'):
    """
    Caesarova šifra
    :param text: Text k zašifrování nebo dešifrování
    :param shift: Posun o daný počet míst
    :param mode: 'encrypt' pro šifrování, 'decrypt' pro dešifrování
    :return: Výsledný text
    """
    if mode == 'decrypt':
        shift = -shift 
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


# Příklad použití
text = "Hello world!"
shift = 3

# Šifrování
encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print("Zašifrovaný text:", encrypted_text)

# Dešifrování
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print("Dešifrovaný text:", decrypted_text)
