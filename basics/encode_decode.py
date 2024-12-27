# Python code​​​​​​‌‌​​​‌​‌‌​​​‌​​‌‌​​‌‌‌‌​‌ below

def encodeString(stringVal):
    # Your code goes here.
    encodedList = []
    previousChar = stringVal[0]
    count =0
    for char in stringVal:
        if previousChar != char:
            encodedList.append((previousChar, count))
            count =0
        count = count +1
        previousChar = char
    encodedList.append((previousChar, count))
    return encodedList
    

def decodeString(encodedList):
    # Your code goes here.
    decodedStr = ''
    for item in  encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

encoded = encodeString("AAAAABBBBCCC")
decoded = decodeString(encoded)

print("Encode AAAAABBBBCCC : " , encoded)
print("Decode  : " , decoded )
