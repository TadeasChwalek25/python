def bin_to_dec(bin_cislo):
    return int(bin_cislo, 2)

def dec_to_bin(desitkove):
    return bin(desitkove)[2:]

def dec_to_hex(desitkove):
    return hex(desitkove)[2:].upper()

def hex_to_dec(hex_cislo):
    return int(hex_cislo, 16)

def bin_to_hex(bin_cislo):
    return dec_to_hex(bin_to_dec(bin_cislo))

def hex_to_bin(hex_cislo):
    return dec_to_bin(hex_to_dec(hex_cislo))

# Hlavní menu
print("Možnosti převodu:")
print("1: Binární → Desítková")
print("2: Desítková → Binární")
print("3: Desítková → Hexadecimální")
print("4: Hexadecimální → Desítková")
print("5: Binární → Hexadecimální")
print("6: Hexadecimální → Binární")

volba = input("Vyber možnost (1-6): ")

if volba == "1":
    bin_cislo = input("Zadej binární číslo: ")
    print(f"Desítkově: {bin_to_dec(bin_cislo)}")

elif volba == "2":
    desitkove = int(input("Zadej desítkové číslo: "))
    print(f"Binárně: {dec_to_bin(desitkove)}")

elif volba == "3":
    desitkove = int(input("Zadej desítkové číslo: "))
    print(f"Hexadecimálně: {dec_to_hex(desitkove)}")

elif volba == "4":
    hex_cislo = input("Zadej hexadecimální číslo: ")
    print(f"Desítkově: {hex_to_dec(hex_cislo)}")

elif volba == "5":
    bin_cislo = input("Zadej binární číslo: ")
    print(f"Hexadecimálně: {bin_to_hex(bin_cislo)}")

elif volba == "6":
    hex_cislo = input("Zadej hexadecimální číslo: ")
    print(f"Binárně: {hex_to_bin(hex_cislo)}")

else:
    print("Neplatná volba")
