#!/usr/bin/python3
def collatz(number):
    try:
        if number % 2 == 0:
            print(number // 2)
        elif number % 2 == 1:
            print(3 * number + 1)
    except ValueError():
        print('Error: Enter Number.')

        if number == 1:
            break #stop if equal to 1
        else:
            return #continue prompt


number = int(input('Enter number:'))
print(collatz(number))




odd
even

