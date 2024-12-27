# Python code​​​​​​‌‌​​​‌​‌‌​​​‌​​‌​​‌‌​​‌​​ below factoria

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


print(factorial(5))

      
