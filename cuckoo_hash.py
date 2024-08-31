# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional


class CuckooHash:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.CYCLE_THRESHOLD = 10
        self.number_of_evictions = 0
        self.table_size = init_size
        self.tables = [[None] * init_size for _ in range(2)]

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size - 1)

    def get_table_contents(self) -> List[List[Optional[int]]]:
        return self.tables

    def is_full_list(self, my_list) -> bool:
        if my_list is not None and not my_list:
            return True
        return False
    
    def insert(self, key: int) -> bool:
        table_id = 0
        self.number_of_evictions = 0
        while self.number_of_evictions<=self.CYCLE_THRESHOLD:
            index = self.hash_func(key, table_id)
            if self.tables[table_id][index] is None:
                self.tables[table_id][index] = key
                return True
            else:
                self.number_of_evictions += 1
                h1_evicted_key = self.tables[table_id][index]
                self.tables[table_id][index]= key
                table_id = 1 - table_id
                key = h1_evicted_key
        return False
        

    def lookup(self, key: int) -> bool:
        for row in range(len(self.tables)):
            for col in range(len(self.tables[row])):
                if self.tables[row][col] == key:
                    return True
        return False

    def delete(self, key: int) -> None:
        for row in range(len(self.tables)):
            for col in range(len(self.tables[row])):
                if self.tables[row][col] == key:
                    self.tables[row][col] = None

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define

    def rehash(self, new_table_size: int) -> None:
        self.number_of_evictions = 0
        self.__num_rehashes += 1  # Increment the rehash counter
        self.table_size = new_table_size  # Set the new table size (do not modify this line)
        self.tables_temp = self.tables
        self.tables = [[None] * new_table_size for _ in range(2)]
        for i in range(len(self.tables_temp)):
            for j in range(len(self.tables_temp[i])):
                if self.tables_temp[i][j] is not None:
                    key = self.tables_temp[i][j]
                    self.insert(key)  
        #self.tables = self.tables_temp