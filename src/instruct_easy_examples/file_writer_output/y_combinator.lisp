; Y Combinator implementation in Lisp

(defun Y (f)
  ((lambda (x) (funcall f (lambda (&rest args) (apply (funcall x x) args))))
   (lambda (x) (funcall f (lambda (&rest args) (apply (funcall x x) args))))))

; Example usage: Factorial function using Y combinator
(defun factorial (f)
  (lambda (n)
    (if (<= n 1)
        1
        (* n (funcall f (- n 1))))))

(defparameter *fact* (Y #'factorial))

; Test the factorial function
(format t "Factorial of 5: ~A~%" (funcall *fact* 5))
(format t "Factorial of 10: ~A~%" (funcall *fact* 10))
