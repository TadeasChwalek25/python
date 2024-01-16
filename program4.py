#Vytvořte program, kde zadáte výšku osob a program vám vypíše průměrnou výšku:


heights = input("Vložte výšky lidí oddělené čárkou a mezerou\n")
heights_list = heights.split(", ")
suma = 0


for one_height in heights_list:
    suma = suma + int(one_height)


average = suma / len(heights_list)
print(f"Průměrná výška je: {average}.")