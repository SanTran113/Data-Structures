from typing import Any, Tuple, List

class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        hash_value = key % self.table_size
        # print(f"hash value key: {self.hash_table[hash_value]}")
        if key < 0:
            raise ValueError
        else:

            if self.hash_table[hash_value] != []:   # if not empty
                for pair in self.hash_table[hash_value]:    # check each element that is in the hash_value

                    # print(f"hash table: {self.hash_table}")
                    # print(f"    adding: [{key}, {value}]")
                    # print(f"    hash_value: {self.hash_table[hash_value]}")
                    # print(f"    checking pair: {pair}")

                    self.num_collisions += 1
                    if pair[0] == key:
                        # print(pair[0])
                        # print(f"key: {key}")
                        # print(self.hash_table[hash_value].index(pair))
                        # print(f"length: {len(self.hash_table[hash_value])}")
                        # self.hash_table[hash_value][1] = self.hash_table[hash_value].index(pair)
                        # del (self.hash_table[hash_value][1])
                        self.num_collisions -= len(self.hash_table[hash_value])
                        self.num_items -= 1
                        self.hash_table[hash_value].pop(self.hash_table[hash_value].index(pair))
                        # print(f"new: {self.hash_table}")

                self.hash_table[hash_value].append([key, value])
                self.num_items += 1

            else:   # is empty append straight in
                self.hash_table[hash_value].append([key, value])
                self.num_items += 1

            if self.load_factor() > 1.5:
                # print('run rehash')
                self.rehash()
        # print(f"final List: {self.hash_table}")


    def rehash(self):
        prev = self.hash_table
        # print(prev)
        self.table_size = 2 * self.table_size + 1
        # print(f"new table size: {self.table_size}")
        self.hash_table = [[] for _ in range(self.table_size)]
        # print(prev)
        for list in prev:
            # print(f"list: {list}")
            if list != []:
                for pair in list:
                    key = pair[0]
                    value = pair[1]
                    hash_value = key % self.table_size
                    if self.hash_table[hash_value] == []:
                        self.hash_table[hash_value].append([key, value])
        # print(self.hash_table)


    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        hash_value = key % self.table_size
        check = hash_value
        return self.get_item_helper(key, hash_value, check)

    def get_item_helper(self, key, hash_value, check):
        # print(self.hash_table[hash_value])
        # print(self.hash_table[check])
        # print(hash_value)
        if self.hash_table[hash_value] == self.hash_table[check]:
            for item in self.hash_table[hash_value]:
                # print(item[0])
                # print(key)
                if item[0] == key:
                    return item[1]
            else:
                raise LookupError


    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        hash_value = key % self.table_size
        for list in self.hash_table:
            print(f"item: {list}")
            if list != []:
                for pair in list:
                    if pair[0] == key:
                        value = self.hash_table[hash_value]
                        self.hash_table[hash_value] = []
                        self.num_items -= 1
                        return tuple(pair)
        raise LookupError


    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        factor = float(self.num_items / self.table_size)
        # print(type(factor))
        # comps = 0.5*(1 + (1 / ((1 - factor)**2)))
        # print(self.hash_table)
        # print(f"num items: {self.num_items}")
        # print(f"table size {self.table_size}")
        return factor

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions
