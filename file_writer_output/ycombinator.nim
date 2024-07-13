# Y Combinator implementation in Nim

proc Y[T, R](f: proc(f: proc(x: T): R): proc(x: T): R): proc(x: T): R =
  proc g(x: T): R =
    f(Y(f))(x)
  return g

# Example usage:
proc factorial(f: proc(n: int): int): proc(n: int): int =
  return proc(n: int): int =
    if n <= 1: 1
    else: n * f(n - 1)

let fact = Y(factorial)
echo fact(5)  # Output: 120
echo fact(10) # Output: 3628800
