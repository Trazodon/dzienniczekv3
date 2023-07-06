import pytest
from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:

    def __init__(self, capacity):
        self.values = capacity * [None]

    def __len__(self):
        return len(self._pairs)
    
    
    def __delitem__(self, key): #Usuwanie rzeczy z hash listy
        if key in self:
            self.values[self._index(key)] = None
        else:
            raise KeyError(key)
        

    def __setitem__(self, key, value): #Kod na dodanie wartości
        self._pairs[self._index(key)] = Pair(key, value)
    

    def __getitem__(self, key): #Napisanie kodu który będzie przydzielał wartości oraz rozpozna czy jest wartość pusta i pokaże KeyError
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return Pair.value
    
    def __contains__(self, key): #Sprawdzenie czy wystepuje KeyError
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    
    def get(self, key, default = None): # kod dla ustanowienia KeyErrora jako wartosc domyslna
        try:
            return self[key]
        except KeyError:
            return default
    @property #Zdefiniowanie czym jest value oraz jak działa
    def values(self):
        return [pair.value for pair in self.pairs]
    
    @property
    def keys(self):
        return{pair.key for pair in self.pairs}
    
    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}
    

    def test_should_raise_key_error_when_deleting(hash_table): #Usuwanie wartości missing_key z hash_table
        with pytest.raises(KeyError) as expection_info:
            del hash_table["missing_key"]
        assert expection_info.values.args[0] == "missing_key"

    