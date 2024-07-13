#lang racket

;; Y Combinator implementation in Scheme (Racket)
(define Y
  (lambda (f)
    ((lambda (x) (x x))
     (lambda (x)
       (f (lambda (y) ((x x) y)))))))

;; Example usage: Factorial function using Y Combinator
(define factorial
  (Y (lambda (f)
       (lambda (n)
         (if (zero? n)
             1
             (* n (f (- n 1))))))))

;; Test the factorial function
(displayln "Factorial of 5:")
(displayln (factorial 5))

(displayln "Factorial of 10:")
(displayln (factorial 10))
