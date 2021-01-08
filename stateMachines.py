import lib601.sm as sm
from utils import safeAdd

class Delay(sm.SM):
    def __init__(self, startState):
        self.startState = startState

    def getNextValues(self, state, inp):
        return (inp, state)


class Increment(sm.SM):
    def __init__(self, startState):
        self.startState = startState

    def getNextValues(self, state, inp):
        return (state, safeAdd(state, inp))
