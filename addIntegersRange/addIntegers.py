#!/usr/bin/python3
# Write a function called addIntegers which takes two integers.
# The function needs to add up all the numbers between the first and last numbers and return the result.
# (5,10) will return 45.

# Functions
def addIntegers(first,second):
    counter = 0
    for i in range(first,second+1):
        counter = counter + i
    return counter

def main():
    first = int(input("First number?"))
    second = int(input("Second number?"))
    result = addIntegers(first,second)
    print("Output: " + str(result))

# Main block
main()
