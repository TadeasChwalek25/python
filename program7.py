#Do proměnné password uložte libovolné heslo.
#Pokud bude mít heslo více jak 13 znaků, tak vypište "Velmi silné heslo". Pokud bude mít mezi 8 až 13 (včetně), tak vypište "Silné heslo". Pokud méně než 8, tak vypište "Slabé heslo".
#Zjistěte, zda heslo obsahuje znaky 1234 v tomto pořadí. Pokud ano, tak se vypíše do konzole "Heslo nesmí obsahovat 1234". Jinak se vypíše "Heslo je v pořádku".


password = "admin1234"

if len(password) > 13:
    print("Velmi silné heslo")
elif 8 <= len(password) <= 13:
    print("Silné heslo")
else:
    print("Slabé heslo")


if "1234" in password:
    print("Heslo nesmí obsahovat 1234")
else:
    print("Heslo je v pořádku")
