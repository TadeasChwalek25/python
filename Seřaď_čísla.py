class Sorting:
    def __init__(self, numbers):
        self.numbers = numbers

    def serad(self, ascending=True):
        """Seřadí čísla vzestupně nebo sestupně podle parametru ascending."""
        self.numbers.sort(reverse=not ascending)

    def __str__(self):
        """Vrátí čísla jako řetězec oddělený čárkami."""
        return ', '.join(map(str, self.numbers))

numbers = list(map(int, input("Zadej čísla oddělená mezerou: ").split()))
order = input("Chceš čísla seřadit vzestupně (v) nebo sestupně (s)? ").lower()

sorting_instance = Sorting(numbers)

if order == 'v':
    sorting_instance.serad(ascending=True)
elif order == 's':
    sorting_instance.serad(ascending=False)
else:
    print("Neplatná volba, výchozí řazení bude vzestupné.")
    sorting_instance.serad(ascending=True)

print("Seřazená čísla:", sorting_instance)
