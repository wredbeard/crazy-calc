import sys
import os
import time
import math

calcIsOn = True
calcs = [0.0]
totals = 0.0
stax = .09

print('\n' + '=====================================')
print("Numbers are stored in 'stacks'. Stacks may be added\nand then operated against.")


def calculator():

    print('What would you like to do?')
    action = input("> ")
    acceptable_actions = ['add', 'sub', 'mul', 'div', 'tck', 'lst', 'quit', 'stx', 'rem']
    while action.lower() not in acceptable_actions:
        print("Unknown action. Try again.\n")
        action = input("> ")
    if action.lower() in 'quit':
        sys.exit()
    elif action.lower() in 'tck':
        getNum = float(input('\n Number to append > '))
        calcs.append(getNum)
    elif action.lower() in 'add':
        add()
    elif action.lower() in 'lst':
        os.system('clear')
        print("\nYour current stored numbers are: " + str(calcs[1:]))
        print("\nYour current total is: " + str(sum(calcs)))
    elif action.lower() in 'stx':
        STax = stax * sum(calcs)
        addSTax = STax + sum(calcs)
        print("Tax total: " + str(STax))
        print("Total with sales tax: " + str(addSTax))
    elif action.lower() in 'rem':
        calcs.pop()
        print("Removing last item...")
        time.sleep(1)
        print("Last item removed")


def add():
    addNum = sum(calcs)
    os.system('clear')
    print(addNum)


def runtime():
    while calcIsOn is True:
        calculator()


runtime()
