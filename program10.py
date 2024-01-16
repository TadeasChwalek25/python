#Pomocí prompt() zadáte křestní jméno podezřelého a do konzole se vypíší všechny jeho údaje. Každý údaj přehledně na jeden řádek. Např.:
#Jméno: Jana
#Příjmení: Růžová
#atd.

#Budete tedy muset najít podle jména daný objekt a ten pak vypíšete. K nalezení objektu použijete findIndex

# Zde je seznam podezřelých:


criminals = [
    {
        "firstName": "Martin",
        "secondName": "Zelený",
        "birth": 1985,
        "address": "U sloupů 16",
        "city": "České Budějovice"
    },
    {
        "firstName": "Jana",
        "secondName": "Růžová",
        "birth": 1996,
        "address": "Malská 29",
        "city": "České Budějovice"
    },
    {
        "firstName": "Filip",
        "secondName": "Modrý",
        "birth": 1989,
        "address": "Stevardská 38",
        "city": "České Budějovice"
    }
]

suspect = input("Zadejte křestní jméno podezřelého: ")

for one_suspect in criminals:
    if one_suspect["firstName"] == suspect:
        our_suspect = one_suspect
        break
else:
    print("Podezřelý nenalezen.")
    exit()

print(f"Jméno: {our_suspect['firstName']}")
print(f"Příjmení: {our_suspect['secondName']}")
print(f"Rok narození: {our_suspect['birth']}")
print(f"Adresa: {our_suspect['address']}")
print(f"Město: {our_suspect['city']}")
