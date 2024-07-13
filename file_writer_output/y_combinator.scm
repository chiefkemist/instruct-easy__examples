; Y Combinator implementation in Scheme

(define Y
  (lambda (f)
    ((lambda (x) (x x))
     (lambda (g)
       (f (lambda args
            (apply (g g) args)))))))

; Example usage:
; Factorial function using Y combinator
(define factorial
  (Y (lambda (f)
       (lambda (n)
         (if (zero? n)
             1
             (* n (f (- n 1))))))))

; Test the factorial function
(display (factorial 5))
(newline)
(display (factorial 10))
(newline)