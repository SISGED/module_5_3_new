class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.n_floors = number_of_floors

    def go_to(self, n_floor):
        if n_floor > self.n_floors or n_floor < 1:
            print("Такого этажа не существует")
        for i in range(n_floor):
            j = i + 1
            if n_floor < self.n_floors:
                print(j)

    def __len__(self):
        return self.n_floors

    def __str__(self):
        return (f'Название {self.name}, количество этажей: {self.n_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.n_floors == other.n_floors
        elif isinstance(other, int):
            return self.n_floors == other

    def __add__(self, value):
        if isinstance(value, int):
            self.n_floors += value
        elif isinstance(value, House):
            self.n_floors += value.n_floors
        return self

    def __lt__(self, other):
        return self.n_floors < other.n_floors

    def __le__(self, other):
        return self.n_floors <= other.n_floors

    def __gt__(self, other):
        return self.n_floors > other.n_floors

    def __ge__(self, other):
        return self.n_floors >= other.n_floors

    def __ne__(self, other):
        return self.n_floors != other.n_floors

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other


# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)

# h1.go_to(11)
# h1.go_to(0)
# h1.go_to(-2)

# h2.go_to(10)

# print(h1)
# print(h2)

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

# __len__
print(len(h3))
print(len(h4))

# __str__
print(h3)
print(h4)

# __eq__
print(h3 == h4)

# __add__
h3 = h3 + 10
print(h3)
print(h3 == h4)

# __iadd__
h3 += 10
print(h3)

# __radd__
h4 = 10 + h4
print(h4)

print(h3 > h4)
print(h3 >= h4)
print(h3 < h4)
print(h3 <= h4)
print(h3 != h4)