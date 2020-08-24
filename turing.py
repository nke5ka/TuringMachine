# Turing Machine Setups
print('Turing machine options:')
print('  0   - back and forth forever')
print('  1   - increment non blank')
print('  b22 - 2 state 2 symbol busy beaver (sigma=  4, s=   6) from Pascal Michel')
print('  b32 - 3 state 2 symbol busy beaver (sigma=  6, s=  14) from wikipedia')
print('  b42 - 4 state 2 symbol busy beaver (sigma= 13, s= 107) from wikipedia')
print('  b23 - 2 state 3 symbol busy beaver (sigma=  9, s=  38) from Pascal Michel')

turingMachineChoice = input('Which turing machine do you want? ')

if (turingMachineChoice == '0'):
    tape = [0] * 20
    tape[5] = 1
    tape[15] = 1
    location = 10
    state = 'a'
    stateTable = {
        'a': {
            0: {'write': 0, 'move': -1, 'nextState': 'a'},
            1: {'write': 1, 'move':  1, 'nextState': 'b'}
        },
        'b': {
            0: {'write': 0, 'move':  1, 'nextState': 'b'},
            1: {'write': 1, 'move': -1, 'nextState': 'a'}
        },
    }
elif (turingMachineChoice == '1'):
    tape = ['_'] * 20
    tape[13:17] = [0] * 4
    location = 17
    state = 'a'
    stateTable = {
        'a': { # return to farthest right
            '_': {'write': '_', 'move': -1, 'nextState': 'b'},
             0 : {'write':  0 , 'move':  1, 'nextState': 'a'},
             1 : {'write':  1 , 'move':  1, 'nextState': 'a'}
        },
        'b': { # increment and carry if needed
            '_': {'write': '_', 'move':  1, 'nextState': 'HALT'},
             0 : {'write':  1 , 'move':  1, 'nextState': 'a'},
             1 : {'write':  0 , 'move': -1, 'nextState': 'b'}
        },
    }
elif (turingMachineChoice == 'b22'):
    tape = [0] * 20
    location = 10
    state = 'a'
    stateTable = {
        'a': {
            0: {'write': 1, 'move':  1, 'nextState': 'b'},
            1: {'write': 1, 'move': -1, 'nextState': 'b'}
        },
        'b': {
            0: {'write': 1, 'move': -1, 'nextState': 'a'},
            1: {'write': 1, 'move':  1, 'nextState': 'HALT'}
        },
    }
elif (turingMachineChoice == 'b32'):
    tape = [0] * 50
    location = 25
    state = 'a'
    stateTable = {
        'a': {
            0: {'write': 1, 'move':  1, 'nextState': 'b'},
            1: {'write': 1, 'move':  1, 'nextState': 'HALT'}
        },
        'b': {
            0: {'write': 0, 'move':  1, 'nextState': 'c'},
            1: {'write': 1, 'move':  1, 'nextState': 'b'}
        },
        'c': {
            0: {'write': 1, 'move': -1, 'nextState': 'c'},
            1: {'write': 1, 'move': -1, 'nextState': 'a'}
        },
    }
elif (turingMachineChoice == 'b42'):
    tape = [0] * 50
    location = 25
    state = 'a'
    stateTable = {
        'a': {
            0: {'write': 1, 'move':  1, 'nextState': 'b'},
            1: {'write': 1, 'move': -1, 'nextState': 'b'}
        },
        'b': {
            0: {'write': 1, 'move': -1, 'nextState': 'a'},
            1: {'write': 0, 'move': -1, 'nextState': 'c'}
        },
        'c': {
            0: {'write': 1, 'move':  1, 'nextState': 'HALT'},
            1: {'write': 1, 'move': -1, 'nextState': 'd'}
        },
        'd': {
            0: {'write': 1, 'move':  1, 'nextState': 'd'},
            1: {'write': 0, 'move':  1, 'nextState': 'a'}
        },
    }
elif (turingMachineChoice == 'b23'):
    tape = [0] * 40
    location = 20
    state = 'a'
    stateTable = {
        'a': {
            0: {'write': 1, 'move':  1, 'nextState': 'b'},
            1: {'write': 2, 'move': -1, 'nextState': 'b'},
            2: {'write': 1, 'move':  1, 'nextState': 'HALT'}
        },
        'b': {
            0: {'write': 2, 'move': -1, 'nextState': 'a'},
            1: {'write': 2, 'move':  1, 'nextState': 'b'},
            2: {'write': 1, 'move': -1, 'nextState': 'b'}
        },
    }
else:
    print('invalid input')

stepsShown = 0

print(stateTable)

while(True):
    print(str(stepsShown).zfill(5) + ': ', end = '')
    print(*tape)
    print(' ' * (location * 2 + 7) + state, end = '')
    if state == 'HALT':
        # print out counts
        counts = {}
        for symbol in tape:
            if symbol in counts.keys():
                counts[symbol] += 1
            else:
                counts[symbol] = 1
        print('\nend counts: ' + str(counts))
        exit()
    readValue = tape[location]
    actionsToDo = stateTable[state][readValue]
    tape[location] = actionsToDo['write']
    location += actionsToDo['move']
    state = actionsToDo['nextState']
    stepsShown += 1
    if stepsShown % 30 == 0:
        input()
    else:
        print()