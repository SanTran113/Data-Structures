from typing import List, Any, Optional


class HashTable:

    def __init__(self, table_size: int):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table: List = [None] * table_size  # hash table
        self.num_items = 0  # empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        hash_value = self.horner_hash(key)
        # print('ran')
        # print(f"hash_value: {hash_value}")
        if self.hash_table[hash_value] is None:     # is empty append straight in
            self.hash_table[hash_value] = [key, value]
            self.num_items += 1
        else:  # if not empty
            # print(f"hash_ value: {self.hash_table[hash_value][0]}")
            # print(f"key: {key}")
            # print(f"value: {value}\n")
            if self.hash_table[hash_value][0] == key:  # if same key
                # print('same key ran')
                for num in value:
                    if num not in self.hash_table[hash_value][1]:   # checks
                        self.hash_table[hash_value][1].append(num)
            else:  # collision so quadratic probing
                # print('collision')
                # print(f"inital value: {hash_value}")
                n = 1
                # print(self.get_load_factor())
                # print(f"num items: {self.num_items}")
                self.quadratic_probing(key, value, n)

        if self.get_load_factor() > 0.5:
            self.rehash()
        # print(self.hash_table)

    def quadratic_probing(self, key, value, n):
        hash_value = self.horner_hash(key)
        temp = (n ** 2)
        hash_value = (hash_value + temp) % self.table_size
        # print(f"temp: {temp}")
        # print(f"current key: {self.hash_table[hash_value]}")
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = [key, value]
            self.num_items += 1
        elif self.hash_table[hash_value][0] == key:  # if same key
            for num in value:
                if num not in self.hash_table[hash_value][1]:  # checks
                    self.hash_table[hash_value][1].append(num)
        else:
            self.quadratic_probing(key, value, n + 1)


    def rehash(self):
        # print(f"before Hash: {self.hash_table}")
        # print(f"table size: {self.table_size}")
        # print(f"num_items: {self.num_items}")
        prev = self.hash_table
        self.table_size = 2 * self.table_size + 1
        self.hash_table = [None] * self.table_size
        for item in prev:
            # print(f"item: {item}")
            if item is not None:
                # print(f"item is not None")
                key = item[0]
                value = item[1]
                hash_value = self.horner_hash(key)
                # print(f"hash_value: {hash_value}")
                if self.hash_table[hash_value] is None:
                    # print('ran')
                    self.hash_table[hash_value] = [key, value]
                else:
                    self.quadratic_probing(item[0], item[1], n=1)
                    self.num_items -= 1

        # print(f"final rehash: {self.hash_table}")


    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        h = 0
        # print(len(key))
        n = min(8, len(key))
        for i in range(n):
            h = (31 * h) + ord(key[i])
        return h % self.table_size

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        hash_value = self.horner_hash(key)
        n = 1
        return self.in_table_helper(key, hash_value, n)

    def in_table_helper(self, key, hash_value, n) -> bool:
        if self.hash_table[hash_value] is None:
            return False
        else:
            # print(hash_value)
            # print(list(self.hash_table[hash_value])[0])
            # print(f" key: {key}")
            # print(list(self.hash_table[hash_value])[0] == key)
            if list(self.hash_table[hash_value])[0] is key:
                return True
            else:
                hash_value += n ** 2
                return self.in_table_helper(key, hash_value, n + 1)

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        hash_value = self.horner_hash(key)
        n = 1
        return self.get_index_helper(key, hash_value, n)

    def get_index_helper(self, key, hash_value, n):
        if self.hash_table[hash_value] is None:
            # print("no index ran")
            return None
        else:
            # print(hash_value)
            # print(list(self.hash_table[hash_value])[0])
            if list(self.hash_table[hash_value])[0] == key:
                return self.hash_table.index(self.hash_table[hash_value])
            else:
                hash_value += n ** 2
                return self.get_index_helper(key, hash_value % self.table_size, n + 1)

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        final = []
        if self.hash_table.count(None) == len(self.hash_table):
            return []
        for item in self.hash_table:
            if item is not None:
                final.append(item[0])
        return final


    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        hash_value = self.horner_hash(key)
        n = 1
        return self.get_value_helper(key, hash_value, n)

    def get_value_helper(self, key, hash_value, n):
        if self.hash_table[hash_value] is None:
            return None
        else:
            if list(self.hash_table[hash_value])[0] == key:
                return list(self.hash_table[hash_value])[1]
            else:
                hash_value += n ** 2
                return self.get_value_helper(key, hash_value % self.table_size, n + 1)

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return float(self.num_items / self.table_size)
