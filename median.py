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
numbers.sort()
if len(numbers)%2 == 1:
    index = len(numbers)//2
    answer = numbers[index]
else:
    indexOne = len(numbers)//2 - 1
    indexTwo = len(numbers)//2
    answer = (numbers[indexOne] + numbers[indexTwo])/2
print(answer)



