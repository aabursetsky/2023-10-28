class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        i = 1
        if 0 < new_floor <= self.number_of_floors:
            while i <= new_floor:
                print(i)
                i += 1
                continue
        else:
            print("Такого этажа не существует")

# Возвращает кол-во этажей здания
    def __len__(self):
        return self.number_of_floors

# Возвращает строку "Название: <название>, кол-во этажей: <этажи>"
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# __eq__ (==)
    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

# __lt__ (<)
    def __lt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

# __le__ (<=)
    def __le__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

# __gt__ (>)
    def __gt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

# __ge__ (>=)
    def __ge__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

# __ne__ (!=)
    def __ne__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __iadd__(self, other):
        return self + other        # __add__(+)

    def __radd__(self, other):
        return self + other        # __add__(+)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10     # __add__
print(h1)
print(h1 == h2)

h1 += 10         # __iadd__
print(h1)

h2 = 10 + h2     # __radd__
print(h2)

print(h1 > h2)   # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)   # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

'''
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
'''
