// Y Combinator implementation in JavaScript

const Y = f => (x => x(x))(x => f(y => x(x)(y)));

// Example usage:

// Factorial function using Y combinator
const factorialGen = f => n => (n === 0 ? 1 : n * f(n - 1));
const factorial = Y(factorialGen);

console.log(factorial(5)); // Output: 120

// Fibonacci function using Y combinator
const fibonacciGen = f => n => (n <= 1 ? n : f(n - 1) + f(n - 2));
const fibonacci = Y(fibonacciGen);

console.log(fibonacci(10)); // Output: 55
