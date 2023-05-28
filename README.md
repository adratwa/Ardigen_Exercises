# Python Recruitment Exercises

This repository contains solutions to two Python exercises that are part of a recruitment process:

1. FizzBuzz
2. Valuation Service
## Exercise 1 - FizzBuzz

This exercise involves writing a script that takes two integers as input, n and m, and prints the numbers from n to m (inclusive). However, for multiples of three, it prints "Fizz" instead of the number, for multiples of five, it prints "Buzz", and for multiples of both three and five, it prints "FizzBuzz".

The solution can be found in the script: Exercise_1.py.

## Exercise 2 - Valuation Service

This exercise is to build a valuation service. The service reads the input data from three CSV files, selects products with a particular matching_id that have the highest total price (price * quantity), limits the dataset by top_priced_count and aggregates the prices.

The solution can be found in the script: Exercise_2.py.

The script reads data from three CSV files stored in the data/ directory:

1. data.csv - product representation with price, currency, quantity, matching_id.
2. currencies.csv - currency code and ratio to PLN.
3. matchings.csv - matching data matching_id, top_priced_count.

## Unit Tests of Exercise_2

Test_Exercise_2.py contains a set of unittests for Exercise_2.py. It checks the functions in Exercise_2.py to make sure they are returning the correct outputs.

To run the tests, call:

```bash
python Test_Exercise_2.py
```

## Requirements

To run these scripts, you need Python 3 and the following Python libraries: pandas, unittest.

You can install the libraries with pip:

```bash
pip install pandas
pip install unittest
```



## Execution

The main.py script can be run to execute both exercises sequentially.

```bash
python main.py
```


