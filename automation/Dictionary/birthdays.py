#!/usr/bin/python3
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        print('Bye!')
        break # Exit script if blank entered from user

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have a birthday for ' + name)
        print('What is theier birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday added.')