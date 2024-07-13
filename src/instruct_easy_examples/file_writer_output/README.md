# Y Combinator in Python

This project implements the Y Combinator in Python using the standard library.

## What is the Y Combinator?

The Y Combinator is a concept in functional programming that allows for the implementation of recursion without naming the recursive function. It's a fixed-point combinator that can be used to implement recursive functions in a language that doesn't have built-in support for recursion.

## Implementation

The Y Combinator is implemented in the `y_combinator.py` file. The main function `Y` takes a function as an argument and returns a recursive version of that function.

## Usage

To use the Y Combinator, import it from the package and apply it to a function that takes itself as the first argument:

```python
from y_combinator import Y

def factorial(f):
    return lambda n: 1 if n == 0 else n * f(n - 1)

factorial_func = Y(factorial)

print(factorial_func(5))  # Outputs: 120
```

## Running the Example

The `y_combinator.py` file includes an example implementation of the factorial function using the Y Combinator. To run it, simply execute the script:

```
python y_combinator.py
```

This will output the factorial of 5, 0, and 10 as a demonstration.

## Note

This implementation is primarily for educational purposes. In practice, Python supports recursion natively, so you wouldn't typically need to use the Y Combinator for recursive functions in Python.
