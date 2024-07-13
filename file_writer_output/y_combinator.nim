proc Y[T, R](f: proc(f: proc(T): R): proc(T): R): proc(T): R =
  proc g(x: T): R =
    f(Y(f))(x)
  g

# Example usage:
proc factorial(f: proc(int): int): proc(int): int =
  proc innerFact(n: int): int =
    if n <= 1: 1
    else: n * f(n - 1)
  innerFact

let fact = Y(factorial)
echo fact(5)  # Outputs: 120
echo fact(10) # Outputs: 3628800