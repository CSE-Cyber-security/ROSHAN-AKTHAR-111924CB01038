def get_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
number = 5
print(f"The factorial of {number} is {get_factorial(number)}")