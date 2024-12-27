# Python code​​​​​​‌‌​​​‌​‌‌​​​‌​​‌​‌‌​‌‌​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    if len(hexNum) > 3:
        return None
    
    lengthOfHexNum = len(hexNum)

    if(lengthOfHexNum == 1):
        return hexNumbers[hexNum[0]]
    if(lengthOfHexNum == 2):
        return hexNumbers[hexNum[1]] + hexNumbers[hexNum[0]] * 16
    if(lengthOfHexNum == 3):
        return hexNumbers[hexNum[2]] + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[0]] * 256

def hexToDecImproved(hexNum):
    if not hexNum or len(hexNum) > 3 or any(char not in hexNumbers for char in hexNum):
        return None

    # Calculate decimal value
    decimal_value = 0
    for index, char in enumerate(reversed(hexNum)):
        decimal_value += hexNumbers[char] * (16 ** index)
    
    return decimal_value


print("A2 : ", hexToDecImproved('A2')) # 10
print("A2 : ", hexToDec('A2')) # 10
