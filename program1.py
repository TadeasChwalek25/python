# Vytvořte program, kde budou vypsány čísla od 1 do 100, pokud:
# číslo dělitelné 3 = Fizz
# číslo dělitelné 5 = Buzz
# číslo dělitelné 3 a 5 = FizzBuzz
# jinak vypsat běžné číslo


for one_number in range(1, 101):
    if one_number % 3 == 0 and one_number % 5 == 0:
        print("FizzBuzz")
    elif one_number % 3 == 0:
        print("Fizz")
    elif one_number % 5 == 0:
        print("Buzz")
    else:
        print(one_number)