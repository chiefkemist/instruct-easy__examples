# Y Combinator implementation in Ruby

# Define the Y Combinator function
Y = -> f {
  -> x { f.call(x.call(x)) }.call(-> x { f.call(-> y { x.call(x).call(y) }) })
}

# Example usage: Factorial function using Y Combinator
factorial = Y.call(-> f {
  -> n { n.zero? ? 1 : n * f.call(n - 1) }
})

# Test the factorial function
puts "Factorial of 5: #{factorial.call(5)}"
puts "Factorial of 10: #{factorial.call(10)}"

# Another example: Fibonacci sequence using Y Combinator
fibonacci = Y.call(-> f {
  -> n { n < 2 ? n : f.call(n - 1) + f.call(n - 2) }
})

# Test the fibonacci function
puts "\nFibonacci sequence:"
10.times { |i| print "#{fibonacci.call(i)} " }
puts "\n"
