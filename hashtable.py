import pytest
from typing import NamedTuple, Any
from collections import deque
DELETED = object()

class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    

    def __init__(self, capacity=8, load_factor_thereshold = 0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_thereshold <= 1):
            raise ValueError("Load factor must be a number beetwen (0, 1]")
        self._kets = []
        self._buckets = [deque() for _ in range()]
        self._load_factor_thereshold = load_factor_thereshold


    def __len__(self):
        return len(self._pairs)
    
    
    def _index(self, key):
        return hash(key) % len(self._pairs)
    
    
    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" +", ".join(pairs) + "}"

    
    def __iter__(self):
            yield from self.keys
    

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)
    

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)


    def __delitem__(self, key): #Usuwanie rzeczy z hash listy
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __setitem__(self, key, value): #Kod na dodanie wartości
        if self.load_factor >= self._load_factor_thereshold:
            self._resize_and_rehash
        
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
            else :
                bucket.append(Pair(key, value))
                self._keys.append(key) 
            

    def __getitem__(self, key): #Napisanie kodu który będzie przydzielał wartości oraz rozpozna czy jest wartość pusta i pokaże KeyError
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)
    
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
        return [self[key] for key in self.keys]
    
    @property
    def keys(self):
       return self._keys.copy()
    
    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]
    
    @property
    def load_factor(self):
        occupied_or_deleted = [slot for slot in self.slots if slot]
        return len(occupied_or_deleted) / self.capacity
    
    @property
    def load_factor(self):
        return len(self) / self.capacity
    
    @property
    def capacity(self):
        return len(self._buckets)
    
    @classmethod
    def from_dict(cls, dictionary, capacity = None):
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def _probe(self, key):
        index = self.index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index +1) % self.capacity

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

