# EDI Parser Stups

[![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/keironstoddart/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser)](https://pepy.tech/project/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser/month)](https://pepy.tech/project/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser/week)](https://pepy.tech/project/edi-835-parser)

### edi-parser: a lightweight EDI file parser

This package provides a simple-to-use Python interface to EDI 835 Health Care Claim Payment and Remittance Advice files.

### Installation
Binary installers for the latest released version are at the Python Package Index. Please note that you need to run Python 3.9 or higher to install the edi-835-parser.
```
pip install edi-parser2-stups==1.0.0
```

### Usage
To parse an EDI file simply execute the `parse` function or `parsestream` function when passing a file stream object.
```python
from ediparser import parse

path = '~/Desktop/my_edi_file.txt'
transaction_set = parse(path)
```
The `parse` function also works on a directory path.
```python
from ediparser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)
```
In both cases, `parse` returns an instance of the `TransactionSets` class. 
This is the class you manipulate depending on your needs. 
For example, say you want to work with the transaction sets data as a `pd.DataFrame`.
```python
from ediparser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)

data = transaction_sets.to_dataframe()
```
And then save that `pd.DataFrame` as a `.csv` file.
```python
data.to_csv('~/Desktop/my_edi_file.csv')
```
The complete set of `TransactionSets` functionality can be found by inspecting the `TransactionSets` 
class found at `edi_parser/transaction_set/transaction_sets.py`

### Tests
Example EDI 835 files can be found in `tests/test_edi_835/files`. To run the tests use `pytest`.
```
python -m pytest
```
