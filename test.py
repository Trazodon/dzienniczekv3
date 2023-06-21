""" LISTA
list1 = ["Pizza", "Sushi", "Steak", "Hamburger", 69, 42.0]
list1[3] = "Carbonara"
print(list1)
"""

""" TUPLA 
tuple1 = ("Computer", "Screen", "TV", "Laptop", 11, 12.1)
tuple1[2] = "Keyboard" #nie zadziała ze względu na to że tupla tego nie obsługuje
print(tuple1
"""
""""  SET
set1 = set(["Michał", "Maja", "Martyna", "Tata", "Mama", "Michał"])
print(set1) 
"""

""" DICTIONARY (dziennik)
dict1 = {
    1:  "Mama",
    2:  "Tata",
    3:  "Martyna",
    4:  "Michał",
    5:  "Maja"
}
print(dict1)"""

""" Dodawanie rzeczy do listy poprzez komende append
list1 = ["Pizza", "Sushi", "Steak", "Hamburger", 69, 42.0]
list1.append(5)
print(list1)
"""


""" Usuniecie objektu z listy poprzez komende pop
list1 = ["Pizza", "Sushi", "Steak", "Hamburger", 69, 42.0]
list1.pop(2)
print(list1) 
"""

""" Dodawanie rzeczy do seta poprzez add
set1 = set(["Michał", "Maja", "Martyna", "Tata", "Mama", "Michał"])
set1.add(2137)
print(set1) 
"""
""" Usuniecie objektu z seta poprzez komende remove
set1 = set(["Michał", "Maja", "Martyna", "Tata", "Mama", "Michał"])
set1.remove("Maja")
print(set1)
"""

""" Dodawanie nowego klucza ze zmienną 
dict1 = {
    1:  "Mama",
    2:  "Tata",
    3:  "Martyna",
    4:  "Michał",
    5:  "Maja"
}
dict1[7] = "Faron" # Klucze nie muszą iść numerami po sobie. Aby dodać nowy klucz trzeba podać nazwe słownika obok w kwadratowym nawiasie numer klucza, a na końcu nazwę zmiennej.
print(dict1) 
"""

""" Usuwanie elementu ze słownika
dict1 = {
    1:  "Mama",
    2:  "Tata",
    3:  "Martyna",
    4:  "Michał",
    5:  "Maja"
}
del dict1[5] # Trzeba podać dokładny klucz który chcemy usunąć, ale przed kluczem nazwe słownika 
print(dict1)
"""

"""
class Node:

    def __init__(self):
        self.value = 0
        self.next = None

head = None
one = None
two = None
three = None

one = Node()
two = Node()
three = Node()

one.value = 1
two.value = 2
three.value = 3

one.next = two
two.next = three
three.next = None 

head = one

while (head !=None):
    print(head.value)
    head = head.next

"""
#Budowa bardzo prostego arraya
#arr = [ 2, 1, 3, 3, 7]
#print(arr)