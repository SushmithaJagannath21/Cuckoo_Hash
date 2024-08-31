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

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/cuckoo-hash-python.git
   cd cuckoo-hash-python
