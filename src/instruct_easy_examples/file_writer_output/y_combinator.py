def Y(f):
    def g(h):
        return lambda *args: f(h(h))(*args)
    return g(g)

# Example usage:
def factorial(f):
    return lambda n: 1 if n == 0 else n * f(n - 1)

factorial_func = Y(factorial)

# Test the Y combinator implementation
if __name__ == '__main__':
    print(factorial_func(5))  # Should print 120
    print(factorial_func(0))  # Should print 1
    print(factorial_func(10))  # Should print 3628800
