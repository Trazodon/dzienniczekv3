from hashtable import HashTable
hash_table = HashTable(capacity=1)

for i in range(20):
    num_pairs = len(hash_table)
    num_empty = hash_table.capacity - num_pairs
    print(
        f"{num_pairs:>2}/{hash_table.capacity:>2}",
        ("X" * num_pairs) + ("." * num_empty)
    )
    hash_table[i] = i