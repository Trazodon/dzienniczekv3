from hashtable import HashTable
def test_should_create_hashtable():
    assert HashTable(size=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    excepted_values = [None, None, None]
    hash_table = HashTable(capacity=3)
    
    actual_values = hash_table.values

    assert actual_values == excepted_values

    def test_should_insert_key_value_pairs():
        hash_table = HashTable(capacity=100)

        hash_table["Siemano"] = "hello"
        hash_table["69.9"] = 21
        hash_table["True"] = False

        assert "Siemano" in hash_table.values
        assert 69.9 in hash_table.values
        assert True in hash_table.values

        assert len(hash_table) == 100

