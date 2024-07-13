// Y Combinator implementation in JavaScript

const Y = f => (
  (x => f(y => x(x)(y)))
  (x => f(y => x(x)(y)))
);

// Example usage:
// Let's define a factorial function using Y combinator
const factorial = Y(fac => n =>
  n <= 1 ? 1 : n * fac(n - 1)
);

// Test the factorial function
console.log(factorial(5)); // Output: 120
console.log(factorial(0)); // Output: 1
console.log(factorial(10)); // Output: 3628800

// Another example: Fibonacci sequence
const fibonacci = Y(fib => n =>
  n <= 1 ? n : fib(n - 1) + fib(n - 2)
);

// Test the fibonacci function
console.log(fibonacci(0)); // Output: 0
console.log(fibonacci(1)); // Output: 1
console.log(fibonacci(10)); // Output: 55
