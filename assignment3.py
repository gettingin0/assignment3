#task1

n = int(input('Enter the no.: '))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(n)
print(f"Factorial of {n} : {result}")


#task2

import math

a = float(input("Enter a No.: "))

if a >= 0:
    sqrt_result = math.sqrt(a)
    log_result = math.log(a)
    sine_result = math.sin(a)

else:
    sqrt_result = "square root not defined for zero"
    log_result =  "not defined for zero or negative numbers "
    sine_result = "not defined for zero or negative numbers "

print('Square root of', a, 'is :', sqrt_result)
print('Natural logarithm (log base e) of', a, 'is :', log_result)
print('Sine of' , a, '(in radians) is :',sine_result)