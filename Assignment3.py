
# Task 1
def factorial(n):
    if n < 2:
        return 1
    else: return n * (factorial(n-1))

result = factorial(5)
print(result)

# Task 2
import math
number = int(input("Enter the number: "))

sqrt_value = math.sqrt(number)
log_value = math.log(number)
sine_value = math.sin(number)


print(f"Square root of {number} = {sqrt_value}")
print(f"Natural log of {number} = {log_value}")
print(f"Sine of {number} (in radians) = {sine_value}")
