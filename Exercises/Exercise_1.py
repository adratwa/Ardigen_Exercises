"""
This Python script takes two integers as input, n and m, and prints the numbers from n to m (inclusive).
However, for multiples of three, it prints "Fizz" instead of the number,
for multiples of five, it prints "Buzz", and for multiples of both three and five, it prints "FizzBuzz".
The input numbers should satisfy the condition 1 <= n < m <= 10000.
"""


def validate_input(n, m):
    try:
        n = int(n)
        m = int(m)

        if n < 1 or m <= n or m > 10000:
            raise ValueError("Invalid input! Please provide numbers within the range 1 <= n < m <= 10000.")
        return n, m
    except ValueError:
        raise ValueError("Invalid input! Please provide valid integers.")


def fizz_buzz(n, m):
    for i in range(n, m + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def run_fizz_buzz():
    n = input("Please provide the n number within the range 1 <= n < 10000: ")
    m = input("Please provide the m number within the range 1 <= n < m <= 10000: ")

    try:
        # validate the input numbers
        n, m = validate_input(n, m)
        # FizzBuzz logic
        fizz_buzz(n, m)
    except ValueError as e:
        print(str(e))


