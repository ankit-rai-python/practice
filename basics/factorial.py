
# Python code​​​​​​‌‌​​​‌​‌‌​​​‌​​‌​​‌‌​​‌​​ below factoria

def factorial_recursive(num):
    # Your code goes here.
    if(type(num)) != int:
        return None
    if(num < 0):
        return None
    
    if num == 0:
        return 1
    
    return num * factorial(num - 1)
    

def factorial(num):
    # Your code goes here.
    factorial = 1
    
    if not isinstance(num, int) or num < 0:
        return None

    if num == 0:
        return 1
        
    while num > 0:
        factorial = factorial * num
        num = num - 1

    return factorial


print("Factorial of 5 : ",factorial(5))
print("Factorial of string : ", factorial("ankit"))
print("Factorial of -5 : ", factorial(-5))
print("Factorial of 0 : ", factorial(0))

      
