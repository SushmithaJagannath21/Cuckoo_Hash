# Cuckoo Hashing Implementation in Python

## Project Overview

This project implements Cuckoo Hashing, a collision resolution technique used in hash tables, using Python. The project contains two main classes: `CuckooHash` and `CuckooHash24`, which implement different variations of Cuckoo Hashing.

- **CuckooHash**: Implements the standard Cuckoo Hashing algorithm with two hash tables and single-slot buckets.
- **CuckooHash24**: Implements a more advanced version called "2,4-cuckoo" hashing, where each bucket can hold multiple items (4 slots per bucket).

## Files Included

- **`cuckoo_hash.py`**: Contains the `CuckooHash` class implementation.
- **`cuckoo_hash_24.py`**: Contains the `CuckooHash24` class implementation.
- **`project1_tests.py`**: Provides test cases for the `CuckooHash` class.
- **`project1_tests_24.py`**: Provides test cases for the `CuckooHash24` class.
- **`requirements.txt`**: Specifies the required Python packages for the project (if any).

## Getting Started

### Prerequisites

- Python 3.6 or higher
- A Linux environment (recommended for testing)

### Installation
Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/cuckoo-hash-python.git
   cd cuckoo-hash-python

Usage
CuckooHash Class (cuckoo_hash.py)
__init__(): Initializes the Cuckoo Hash tables with specified dimensions and fills both tables with None entries.
insert(key): Inserts a key into the hash table. If a cycle is detected during insertion, the method returns False; otherwise, it returns True.
lookup(key): Returns True if the key exists in the hash table, False otherwise.
delete(key): Removes the key from the hash table.
rehash(new_table_size): Rehashes all elements into new tables of the specified size.

CuckooHash24 Class (cuckoo_hash_24.py)
Implements a "2,4-cuckoo" hash table where each bucket has 4 slots.
__init__(): Initializes the 2,4-cuckoo hash table.
insert(key): Inserts a key into the hash table with multi-slot bucket handling.
lookup(key): Looks up a key in the hash table across the 4 slots in each relevant bucket.
delete(key): Deletes a key from the hash table.
rehash(new_table_size): Rehashes all elements into new tables with adjusted bucket sizes.
Project Structure
cuckoo_hash.py: Implementation of the standard Cuckoo Hashing algorithm.
cuckoo_hash_24.py: Implementation of the "2,4-cuckoo" hashing algorithm.
project1_tests.py: Test cases for the CuckooHash class.
project1_tests_24.py: Test cases for the CuckooHash24 class.
