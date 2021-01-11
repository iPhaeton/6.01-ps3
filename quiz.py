import lib601.sm as sm

class Vending(sm.SM):
    startState = 0 # number of quarters

    def getNextValues(self, state, inp):
        if inp == 'quarter':
            return (state + 1, (0, False))
        elif inp == 'cancel':
            return (0, (state * 25, False))
        elif inp == 'dispense':
            change = state - 3
            if change >= 0:
                return (0, (change * 25, True))
            else:
                return (0, (state * 25, False))

print Vending().transduce(['dispense', 'quarter', 'quarter', 'quarter', 'quarter',
'dispense', 'quarter', 'cancel', 'dispense']) 