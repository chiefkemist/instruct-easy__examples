// Y Combinator implementation in JavaScript

const Y = f => (x => x(x))(x => f(y => x(x)(y)));

// Example usage:

// Factorial function using Y Combinator
const factorial = Y(fac => n => n <= 1 ? 1 : n * fac(n - 1));

console.log(factorial(5)); // Output: 120

// Fibonacci function using Y Combinator
const fibonacci = Y(fib => n => n <= 1 ? n : fib(n - 1) + fib(n - 2));

console.log(fibonacci(10)); // Output: 55