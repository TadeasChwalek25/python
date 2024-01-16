# Sečtěte všechna sudá čísla od 1 do 100 a vypište do centrálu:
sum = 0


for one_number in range(1, 101):
    if one_number % 2 == 0:
        sum += one_number


print(sum)
