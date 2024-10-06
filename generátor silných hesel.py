import random
import string

def generate_strong_password(length=12):
    if length < 8:  # Zajišťuje minimální délku hesla pro silnou ochranu
        raise ValueError("Password length should be at least 8 characters.")
    
    # Definice možných znaků pro heslo
    letters = string.ascii_letters  # malá a velká písmena (a-z, A-Z)
    digits = string.digits  # číslice (0-9)
    special_chars = string.punctuation  # speciální znaky (@, #, atd.)
    
    # Zajištění, že heslo bude obsahovat aspoň jeden znak z každé kategorie
    password = [
        random.choice(letters),  # alespoň jedno písmeno
        random.choice(digits),   # alespoň jedno číslo
        random.choice(special_chars)  # alespoň jeden speciální znak
    ]
    
    # Zbytek hesla se naplní náhodnými znaky
    remaining_length = length - 3
    password += random.choices(letters + digits + special_chars, k=remaining_length)
    
    # Zamíchání hesla pro zajištění náhodnosti
    random.shuffle(password)
    
    return ''.join(password)

# Příklad: Generování silného hesla o délce 12 znaků
print(generate_strong_password(12))
