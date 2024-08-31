# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional


class CuckooHash24:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.bucket_size = 4
        self.CYCLE_THRESHOLD = 10
        self.table_size = init_size
        self.number_of_evictions = 0
        self.tables = [[None] * init_size for _ in range(2)]
        self.table_id = 0

    def get_rand_idx_from_bucket(self, bucket_idx: int, table_id: int) -> int:
        # you must use this function when you need to displace a random key from a bucket during insertion (see the description in requirements.py).
        # this function randomly chooses an index from a given bucket for a given table. this ensures that the random
        # index chosen by your code and our test script match.
        #
        # for example, if you are inserting some key x into table 0, and hash_func(x, 0) returns 5, and the bucket in index 5 of table 0 already has 4 elements,
        # you will call get_rand_bucket_index(5, 0) to determine which key from that bucket to displace, i.e. if get_random_bucket_index(5, 0) returns 2, you
        # will displace the key at index 2 in that bucket.
        rand.seed(int(str(bucket_idx) + str(table_id)))
        return rand.randint(0, self.bucket_size - 1)

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size - 1)

    def get_table_contents(self) -> List[List[Optional[List[int]]]]:
        # the buckets should be implemented as lists. Table cells with no elements should still have None entries.
        return self.tables

    # you should *NOT* change any of the existing code above this line
    # you may however define additional instance variables inside the __init__ method.
    def reset_numberOfEvictions(self):
        self.number_of_evictions = 0        

    def insert(self, key: int) -> bool:
        table_id = 0
        self.number_of_evictions = 0
        while self.number_of_evictions<=self.CYCLE_THRESHOLD:
            index = self.hash_func(key, table_id)
            if self.tables[table_id][index] is None:
                res = []
                res.append(key)
                self.tables[table_id][index] = res
                return True
            else:
                if len(self.tables[table_id][index]) < self.bucket_size:
                    self.tables[table_id][index].append(key)
                    return True
                else:
                    self.number_of_evictions += 1
                    h1_randIndex_replace = self.get_rand_idx_from_bucket(index, table_id)
                    h1_evicted_key = self.tables[table_id][index][h1_randIndex_replace]
                    self.tables[table_id][index][h1_randIndex_replace]= key
                    table_id = 1 - table_id
                    key = h1_evicted_key
        return False
        

    def lookup(self, key: int) -> bool:
        for table_id in range(2):
            index = self.hash_func(key, table_id)
            if self.tables[table_id][index] is not None and key in self.tables[table_id][index]:
                return True
        return False

    def delete(self, key: int) -> None:
        # TODO
        if self.lookup(key):
            index = self.hash_func(key, 0)
            h1_List = self.tables[0][index]
            if key in h1_List:
                #List_index = h1_List.index(key)
                h1_List.remove(key)
                if len(h1_List)<1:
                        self.tables[0][index] = None
                else:
                        self.tables[0][index] = h1_List
            else:
                index = self.hash_func(key,1)
                h2_List = self.tables[1][index]
                if key in h2_List:
                    #List_index = h2_List.index(key)
                    h2_List.remove(key)
                    if len(h2_List)<1:
                        self.tables[1][index] = None
                    else:
                        self.tables[1][index] = h2_List
                
            
        

    def rehash(self, new_table_size: int) -> None:
        self.__num_rehashes += 1
        self.table_size = new_table_size  # do not modify this line
        self.number_of_evictions = 0
        self.tables_temp = self.tables
        self.tables = [[None] * new_table_size for _ in range(2)]
        for i in range(len(self.tables_temp)):
            for j in range(len(self.tables_temp[i])):
                if self.tables_temp[i][j] is not None:
                    keysList = self.tables_temp[i][j]
                    for key in keysList:
                        self.insert(key)
        

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
