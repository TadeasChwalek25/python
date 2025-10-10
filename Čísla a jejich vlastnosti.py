def is_even(number):

    # Vrací True, pokud je číslo uděleno, jinak False.
    
    return number % 2 == 0

def is_odd(number):
    
    #  Vrací True, pokud je číslo liché, jinak False.
    
    return number % 2 == 1

def is_prime(number):
    
    #  Vrací True, pokud je číslo prvočíslo, jinak False.
    
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# hlavní program
n = int(input("Zadejte celé číslo n (větší než nula 0): "))

even_count = 0
odd_count = 0
prime_count = 0

for i in range(1, n + 1):
    print(f"Číslo {i}:")
    print(f"  - Sudé: {is_even(i)}")
    print(f"  - Děl se 3: {i % 3 == 0}")
    print(f"  - Prvočíslo: {is_prime(i)}")
    print()

    if is_even(i):
        even_count += 1
    if is_odd(i):
        odd_count += 1
    if is_prime(i):
        prime_count += 1

print(f"Součet sudých čísel: {even_count}")
print(f"Součet lichých čísel: {odd_count}")
print(f"Součet prvočísel: {prime_count}")
