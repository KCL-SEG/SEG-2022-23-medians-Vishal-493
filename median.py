"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
ascendingNumbers = numbers.sort()
print(ascendingNumbers)
if len(ascendingNumbers)%2 == 0:
    medianEven = ascendingNumbers[int(len(ascendingNumbers)/2)] + ascendingNumbers[int(((len(ascendingNumbers)/2)-1)/2)]
    print(medianEven)
else:
    medianOdd = ascendingNumbers[int((len(ascendingNumbers)-1)/2)]
    print(medianOdd)
