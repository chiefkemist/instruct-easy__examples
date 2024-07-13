# Y Combinator implementation in Ruby

# The Y Combinator function
Y = lambda do |f|
  lambda do |x|
    lambda do |*args|
      f[x[x]].call(*args)
    end
  end.call(lambda do |x|
    lambda do |*args|
      f[x[x]].call(*args)
    end
  end)
end

# Example usage: Factorial function using Y Combinator
factorial = Y.call(lambda do |f|
  lambda do |n|
    n <= 1 ? 1 : n * f.call(n - 1)
  end
end)

# Test the factorial function
puts "Factorial of 5: #{factorial.call(5)}"
puts "Factorial of 10: #{factorial.call(10)}"

# Example usage: Fibonacci function using Y Combinator
fibonacci = Y.call(lambda do |f|
  lambda do |n|
    n <= 1 ? n : f.call(n - 1) + f.call(n - 2)
  end
end)

# Test the fibonacci function
puts "10th Fibonacci number: #{fibonacci.call(10)}"
puts "20th Fibonacci number: #{fibonacci.call(20)}"
