import lib601.sm as sm
from stateMachines import Increment, Delay

class Cascade(sm.SM):
    def __init__(self, sm1, sm2):
        self.sm1 = sm1
        self.sm2 = sm2
        self.startState = (self.sm1.startState, self.sm2.startState)

    def getNextValues(self, state, inp):
        (state1, state2) = state
        (newState1, output1) = self.sm1.getNextValues(state1, inp)
        (newState2, output) = self.sm2.getNextValues(state2, output1)
        return ((newState1, newState2), output)

# cascade = Cascade(Increment(1), Delay(0))
# print(cascade.transduce([2, 1, 4]))
