import pytest
from pytest_unordered import unordered
from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(size=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_pairs_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]
    

def test_should_insert_key_value_pairs():
        hash_table = HashTable(capacity=100)
        hash_table["key"] = None
        assert None in hash_table.values

        hash_table["Siemano"] = "hello"
        hash_table[69.9] = 21
        hash_table[True] = False

        assert ("Siemano", "Hello") in hash_table.pairs
        assert (69.9, 21) in hash_table.pairs
        assert (True, False) in hash_table.pairs

        assert len(hash_table) == 3


#Dodawanie warunku że wartość nie może w parze być pusta

def test_should_not_contain_none_value_when_created():
        hash_table = HashTable(capacity=100)
        values = [pair.value for pair in hash_table.values if pair]
        assert None not in values


#Polepszenie kodu za pomoca biblioteki pytest

@pytest.fixture 
def hash_table():
    sample_data = HashTable(capcity=100)
    sample_data["Siemano"] = "Hello"
    sample_data[69.9] = 21
    sample_data[True] = False
    return sample_data


#Sprawdzenie par w tabeli

def test_should_find_value_by_key(hash_table): 
    assert HashTable("Siemano") == "Hello"
    assert HashTable[69.9] == 21
    assert HashTable[True] is False


#Napisanie kodu wykrywanie błędu przy missing key

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


#Sprawdzenie czy siemano jest w tabeli

def test_should_find_key(hash_table): 
    assert "Siemano" in hash_table


#Sprawdzenie czy missing key nie znajduje sie przypadkiem w tabeli

def test_should_not_find_key(hash_table): 
    assert "missing_key" not in hash_table


#Ustalenie pary dla siemano ktore jest kluczem a wartoscia jest hello

def test_should_get_value(hash_table): 
    assert unordered(hash_table.values) == ["Hello", 21, False]


#Zrobienie aby missing key był pusty

def test_should_get_none_when_missing_key(hash_table): 
    assert hash_table.get("missing_key") is None


#ustawianie missing key na wartość podstawowa

def test_should_get_default_when_missing_key(hash_table): 
    assert hash_table.get("missing_key", "default") == "default"


#ustalanie wartości z tabeli na podstawowa ktora jest "hello"

def test_should_get_value_with_default(hash_table): 
    assert hash_table.get("Siemano", "default") == "hello"


#usuwanie klucza i wartosci z tabeli

def test_should_delete_key_value_pairs(hash_table): 
    assert "Siemano" in hash_table
    assert ("Siemano", "hello") in hash_table.values
    assert len(hash_table) == 3

    del hash_table["Siemano"] 

    assert "Siemano" not in hash_table
    assert ("Siemano", "hello") not in hash_table.values
    assert len(hash_table) == 2


#Zmiana wartości w hash table 

def test_should_update_value(hash_table): 
    assert hash_table["Siemano"] == "Hello"
    
    hash_table["Siemano"] = "Hejka"

    assert hash_table["Siemano"] == "Hejka"
    assert hash_table["69.9"] == 21
    assert hash_table[True] is False
    assert len(hash_table) == 3


# Sprawdzanie czy pary znajdują się w hash_table

def test_should_return_pairs(hash_table): 
    assert hash_table.pairs == {
        ("Siemano", "hello") 
        (69.9, 21) 
        (True, False) 
    }


def test_should_get_values_of_empty_hash_table():
    assert len(HashTable(capacity=100)) == 0


#Aby zabezpieczyć kod outpu będzie kopią danych przez co ich zmiana nie zniszczy kodu

def test_should_return_copy_of_values(hash_table): 
    assert hash_table.values is not hash_table.values


#Wstawienie pustych wartości jako output w tabeli

def test_should_insert_none_value(): 
    hash_table = HashTable(100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.values


#Dzięki funcji sorted nie będzie utraty zmiennej mimo dwóch takich samych wartości.

def test_should_recive_duplicated_values(): 
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)


#Stworzenie list aby móc porównać czy nie ma błędu w zapisie zmiennych

def have_same_elements(list1, list2): 
    return all(element in list1 for element in list2)


#Dodanie key dla wartości aby dana wartość mogła byc przypisana do klucza.

def test_should_get_keys(hash_table): 
    assert hash_table.keys == {"Siemano", 69.9, True}

#Stworzenie możliwosci nadania kluczó mimo pustej hash table

def test_should_get_keys_of_empty_hash_table(): 
    assert HashTable(capacity=100).pairs == set()

#Pokazanie kopii kluczów, aby niepowołane osoby nie uszkodziły kodu
def test_should_return_copy_of_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys


#Przekonwertowanie hash_table jako dictionary,a by móc brać wartości z różnych miejsc

def test_should_convert_to_dict(hash_table): 
        dictionary = dict(hash_table.pairs)
        assert set(dictionary.keys()) == hash_table.keys
        assert set(dictionary.items()) == hash_table.pairs
        assert list(dictionary.values()) == unordered(hash_table.values)


#Stworzenie hash_table z zerową pojemnością

def test_should_not_create_hashtable_with_zero_capacity(): 
    with pytest.raises(ValueError):
        HashTable(capacity=0)


#Stworzenie hash_table z ujemną pojemnością (nie może tak być przez co w drugim pliku jest to ustalone jako error bo nie może być ujemną liczbą.)

def test_should_not_create_hashtable_with_negative_capacity(): 
    with pytest.raises(ValueError):
        HashTable(capacity=-100)


#Ustalenie długości dla hash_table

def test_should_report_length(hash_table):
    assert len(hash_table) == 3


#Ustaelenie capacity(pojemności) dla pustej tabeli

def test_should_report_capacity_of_empty_hash_table(hash_table):
    assert HashTable(capacity=100).capacity == 100


#Ukazanie capacity dla hash_table

def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100


#Nadanie kluczy w hash_table

def test_should_iterate_over_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("Siemano", 69.9, True)


#Nadanie wartości dla kluczy w hash_table (trzeba zapisać je w kolejności takiej samej jak ich klucze )

def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in hash_table ("Hello", 21, False)


#Połączenie kluczy z wartościami 

def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values


#Zapisanie randomizera dla tych wartości w pętli

def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ("Siemano", 69.9, True)


#Stworzenie dictionary który odczytuje wartości w ,wybranej kolejności. Zmienne są zapisane jednym apostrofem, bo cudzysłów jest dla całego ciągu zmiennych. Aby to działało trzeba było zapisać __str__ w drugim pliku.

def test_should_use_dict_literal_for_sth(hash_table):
        assert str(hash_table) in {
        "{'Siemano': 'hello', 69.9: 21, True: False}",
        "{'Siemano': 'hello', True: False, 69.9: 21}",
        "{69.9: 21, 'Siemano': 'hello', True: False}",
        "{69.9: 21, True: False, 'Siemano': 'hello'}",
        "{True: False, 'Siemano': 'hello', 69.9: 21}",
        "{True: False, 69.9: 21, 'Siemano': 'hello'}",
        }


def test_should_create_hashtable_from_dict():
    dictionary = {"Siemano": "Hello", 69.9: 21, True: False}

    hash_table = HashTable.from_dict(dictionary)

    assert hash_table.capacity == len(dictionary) * 10
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_create_hashtable_from_dict_with_custom_capacity():
    dictionary = {"Siemano": "hello", 69.9: 21, True: False}

    hash_table = HashTable.from_dict(dictionary, capacity=100)
    
    assert hash_table.capacity == 100
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())


def test_should_have_canonical_string_representation(hash_table):
        assert repr(hash_table) in {
        "HashTable.from_dict{'Siemano': 'hello', 69.9: 21, True: False}",
        "HashTable.from_dict{'Siemano': 'hello', True: False, 69.9: 21}",
        "HashTable.from_dict{69.9: 21, 'Siemano': 'hello', True: False}",
        "HashTable.from_dict{69.9: 21, True: False, 'Siemano': 'hello'}",
        "HashTable.from_dict{True: False, 'Siemano': 'hello', 69.9: 21}",
        "HashTable.from_dict{True: False, 69.9: 21, 'Siemano': 'hello'}",
        }


def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table


def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()


def test_should_compare_equal_diffrent_key_value_order(hash_table):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    assert h1 == h2


def test_should_compare_unequal(hash_table):
    other = hash_table.from_dict({"diffrent": "value"})
    assert hash_table != other

def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 42


def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.pairs) == set(copy.pairs)
    assert hash_table.capacity == copy.capacity

def test_should_comapare_equal_diffrent_capacity():
    data = {"a": 1, "b": 2, "c": 3}
    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity= 50)
    assert h1 == h2


