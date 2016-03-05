#!/usr/bin/python3
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBought(guests, item):
    numBought = 0
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return  numBought

print('Number of things being bought: ')
print(' - Apples        ' + str(totalBought(allGuests, 'apples')))
print(' - Cups          ' + str(totalBought(allGuests, 'cups')))
print(' - Cakes         ' + str(totalBought(allGuests, 'cakes')))
print(' - Ham Sandwiches' + str(totalBought(allGuests, 'ham sandwiches')))
print(' - Apple Pies    ' + str(totalBought(allGuests, 'apple pies')))

