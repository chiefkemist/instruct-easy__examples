def Y(f):
    return (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

# Example usage:
def factorial(f):
    return lambda n: 1 if n == 0 else n * f(n - 1)

factorial_func = Y(factorial)

# Test the factorial function
if __name__ == '__main__':
    for i in range(6):
        print(f'{i}! = {factorial_func(i)}')
