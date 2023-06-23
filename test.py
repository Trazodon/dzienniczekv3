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

"""
class LinkedList:
    def __init__(self, head = None):
       self.head = head
       def append(self, new_node):
           current = self.head
           if current:
                while current.next:
                    current = current.next
                current.next = new_node
           else:
               self.head = new_node
        
"""

"""
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
        def delete(self, value):
            current = self.head
            if current.value == value:
                self.head = current.next
            else:
                while current:
                    if current.value == value:
                        break
                if current == None:
                    return
"""

"""
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
        def delete(self, value):
            current = self.head
            if current.value == value:
                self.head = current.next
            else:
                while current:
                    if current.value == value:
                        break
                if current == None:
                    return
        def insert(self, new_element, position):
            count = 1
            current = self.head
            if position == 1:
                new_element.next = self.head
                self.head = new_element
            while current:
                if count + 1 == position:
                    new_element.next = current.next
                    current.next = new_element
                    return
                else:
                    count += 1
                    current = current.next
                    break
            pass

"""

class Node:
	
	def __init__(self):
		self.data = 0
		self.next = None

head = None
e1 = None
e2 = None
e3 = None
e4 = None

# Nadanie przynależności wartościom do node'ów
e1 = Node()
e2 = Node()
e3 = Node()
e4 = Node()
# Dodawanie wartości
e1.data = "136642"
e2.data = "22626236"
e3.data = "32673727"
e4.data = "462677627"

# Połączenie node'ów
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = None

# wyświetlenie listy 
head = e1

while (head != None):
	print(head.data)
	head = head.next


