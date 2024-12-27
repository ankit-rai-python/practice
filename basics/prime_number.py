# Python code​​​​​​‌‌​​​‌​‌‌​​​‌​‌​​​‌‌​‌‌​‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    prime = []
    # Your code goes here.
    for number in range(2, num):
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor ==0:
                break
        else:
            prime.append(number)
    return prime

print("Prime number betwween 2 and 100 are: ", allPrimesUpTo(100))
