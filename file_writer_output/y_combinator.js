// Y Combinator function in JavaScript

const Y = f => (x => x(x))(x => f(y => x(x)(y)));

// Example usage:
const factorial = Y(fac => n => n <= 1 ? 1 : n * fac(n - 1));

console.log(factorial(5));  // Output: 120
console.log(factorial(10)); // Output: 3628800