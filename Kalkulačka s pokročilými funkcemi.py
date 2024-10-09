import math

def calculator():
    print("Pokročilá kalkulačka")
    print("Dostupné operace:")
    print("1. Sčítání (+)")
    print("2. Odčítání (-)")
    print("3. Násobení (*)")
    print("4. Dělení (/)")
    print("5. Mocnina (**)")
    print("6. Sinus (sin)")
    print("7. Kosinus (cos)")
    print("8. Tangens (tan)")
    print("9. Faktoriál (factorial)")
    print("10. Konec")

    while True:
        choice = input("\nZadejte operaci (1-10): ")

        if choice == '10':
            print("Konec programu.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Zadejte první číslo: "))
            num2 = float(input("Zadejte druhé číslo: "))

            if choice == '1':
                print(f"Výsledek: {num1 + num2}")
            elif choice == '2':
                print(f"Výsledek: {num1 - num2}")
            elif choice == '3':
                print(f"Výsledek: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Výsledek: {num1 / num2}")
                else:
                    print("Chyba: Dělení nulou!")
            elif choice == '5':
                print(f"Výsledek: {num1 ** num2}")

        elif choice in ['6', '7', '8']:
            num = float(input("Zadejte úhel ve stupních: "))
            radians = math.radians(num)

            if choice == '6':
                print(f"sin({num}) = {math.sin(radians)}")
            elif choice == '7':
                print(f"cos({num}) = {math.cos(radians)}")
            elif choice == '8':
                print(f"tan({num}) = {math.tan(radians)}")

        elif choice == '9':
            num = int(input("Zadejte číslo pro faktoriál: "))
            if num >= 0:
                print(f"{num}! = {math.factorial(num)}")
            else:
                print("Chyba: Faktoriál není definován pro záporná čísla.")

        else:
            print("Neplatná volba, zkuste to znovu.")

calculator()
