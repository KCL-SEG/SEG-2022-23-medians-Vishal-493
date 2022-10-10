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
print(numbers)
if len(numbers)%2 == 0:
    medianEven = (int(numbers[len(numbers)/2)] + numbers[int((len(numbers)/2)-1)])/2
    print(medianEven)
else:
    medianOdd = (int(numbers[(len(numbers)-1)/2]))
    print(medianOdd)
