numberOfTriples = int(input())
for i in range(numberOfTriples):
    userInput = input()
    splitInputs = userInput.split(" ")
    inputA = str(splitInputs[0])
    inputB = str(splitInputs[1])
    characterNumber = int(splitInputs[2])
    valueA = "A"
    valueB = "B"
    currLen = 0
    lenA = len(inputA)
    lenB = len(inputB)
    fibonacciString = valueA + valueB
    print(fibonacciString)
    currLen += lenA + lenB
    # tries = 0
    while currLen < characterNumber:
        valueA = valueB
        valueB = fibonacciString
        fibonacciString = valueA + valueB
        lenA = lenB
        lenB = currLen
        currLen = lenA + lenB
        # tries += 1
        print(currLen)
    
    print(fibonacciString)
    # print(fibonacciString[characterNumber-1])



#1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 104683731294243150