import pytest
from pytest_unordered import unordered
from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(size=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._pairs == [None, None, None]
    

def test_should_insert_key_value_pairs():
        hash_table = HashTable(capacity=100)
        hash_table["key"] = None
        assert None in hash_table.values

        hash_table["Siemano"] = "hello"
        hash_table[69.9] = 21
        hash_table[True] = False

        assert ("Siemano", "Hello") in hash_table.values
        assert (69.9, 21) in hash_table.values
        assert (True, False) in hash_table.values

        assert len(hash_table) == 100


def test_should_not_contain_none_value_when_created(): #Dodawanie warunku że wartość nie może w parze być pusta
        hash_table = HashTable(capacity=100)
        values = [pair.value for pair in hash_table.values if pair]
        assert None not in values

@pytest.fixture #Polepszenie kodu za pomoca biblioteki pytest
def hash_table():
    sample_data = HashTable(capcity=100)
    sample_data["Siemano"] = "Hello"
    sample_data[69.9] = 21
    sample_data[True] = False
    return sample_data

def test_should_find_value_by_key(hash_table): #Sprawdzenie par w tabeli
    assert HashTable("Siemano") == "Hello"
    assert HashTable[69.9] == 21
    assert HashTable[True] is False

def test_should_raise_error_on_missing_key(): #Napisanie kodu wykrywanie błędu przy missing key
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table): #Sprawdzenie czy siemano jest w tabeli
    assert "Siemano" in hash_table

def test_should_not_find_key(hash_table): #Sprawdzenie czy missing key nie znajduje sie przypadkiem w tabeli
    assert "missing_key" not in hash_table

def test_should_get_value(hash_table): #Ustalenie pary dla siemano ktore jest kluczem a wartoscia jest hello
    assert unordered(hash_table.values) == ["Hello", 21, False]

def test_should_get_none_when_missing_key(hash_table): #Zrobienie aby missing key był pusty
    assert hash_table.get("missing_key") is None

def test_should_get_default_when_missing_key(hash_table): #ustawianie missing key na wartość podstawowa
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table): #ustalanie wartości z tabeli na podstawowa ktora jest "hello"
    assert hash_table.get("Siemano", "default") == "hello"

def test_should_delete_key_value_pair(hash_table): #usuwanie klucza i wartosci z tabeli
    assert "Siemano" in hash_table
    assert ("Siemano", "hello") in hash_table.values
    assert len(hash_table) == 100

    del hash_table["Siemano"] 

    assert "Siemano" not in hash_table
    assert ("Siemano", "hello") not in hash_table.values
    assert len(hash_table) == 100

def test_should_update_value(hash_table): #Zmiana wartości w hash table 
    assert hash_table["Siemano"] == "Hello"
    
    hash_table["Siemano"] = "Hejka"

    assert hash_table["Siemano"] == "Hejka"
    assert hash_table["69.9"] == 21
    assert hash_table[True] is False
    assert len(hash_table) == 100

def test_should_return_pairs(hash_table): # Sprawdzanie czy pary znajdują się w hash_table
    assert hash_table.pairs == {
        ("Siemano", "hello") 
        (69.9, 21) 
        (True, False) 
    }


def test_should_get_values_of_empty_hash_table():
    assert HashTable(capacity=100).values == []


def test_should_return_copy_of_values(hash_table): #Aby zabezpieczyć kod outpu będzie kopią danych przez co ich zmiana nie zniszczy kodu
    assert hash_table.values is not hash_table.values

def test_should_insert_none_value(): #Wstawienie pustych wartości jako output w tabeli
    hash_table = HashTable(100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.values

def test_should_recive_duplicated_values(): #Dzięki funcji sorted nie będzie utraty zmiennej mimo dwóch takich samych wartości.
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)


def have_same_elements(list1, list2):
    return all(element in list1 for element in list2)

def test_should_get_keys(hash_table):
    assert hash_table.keys == {"Siemano", 69.9, True}


def test_should_get_keys_of_empty_hash_table():
    assert HashTable(capacity=100).pairs == set()


def test_should_return_copy_of_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys