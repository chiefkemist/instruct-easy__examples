(defun Y (f)
  ((lambda (x) (funcall x x))
   (lambda (x)
     (funcall f (lambda (&rest args)
                  (apply (funcall x x) args))))))

;; Example usage:
(defun factorial (f)
  (lambda (n)
    (if (<= n 1)
        1
        (* n (funcall f (- n 1))))))

(defparameter *factorial* (Y #'factorial))

;; Test the factorial function
(format t "Factorial of 5: ~A~%" (funcall *factorial* 5))
(format t "Factorial of 10: ~A~%" (funcall *factorial* 10))