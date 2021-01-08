import lib601.sm as sm


class SumTSM(sm.SM):
    startState = 0

    def __init__(self, lim):
        self.lim = lim

    def getNextValues(self, state, inp):
        newState = state + inp
        return (newState, newState)

    def done(self, state):
        return state > 100


sumTSM = SumTSM(100)
# print sumTSM.transduce([10, 50, 80, 90])


class FourTimes(sm.SM):
    def __init__(self, sm):
        self.startState = (0, sm.startState)
        self.sm = sm

    def advanceIfDone(self, state):
        (counter, smState) = state
        if self.sm.done(smState):
            return (counter + 1, self.sm.startState)
        else:
            return state

    def getNextValues(self, state, inp):
        (counter, smState) = state
        (newSmState, output) = self.sm.getNextValues(smState, inp)
        newState = self.advanceIfDone((counter, newSmState))
        return (newState, output)

    def done(self, state):
        (counter, _) = state
        return counter == 4


fourTimes = FourTimes(SumTSM(100))
# print fourTimes.transduce(
#     [10, 50, 80, 90, 100, 40, 50, 30, 70, 20, 90, 1, 2, 3])


class CountUpTo(sm.SM):
    startState = 0

    def __init__(self, lim):
        self.lim = lim

    def getNextValues(self, state, inp):
        if self.done(state):
            return (state, state)
        else:
            newState = state + 1
            return (newState, newState)
    
    def done(self, state):
        return state == self.lim


# m = CountUpTo(3)
# print m.run(n=20)

class Repeat(sm. SM):
    def __init__(self, sms):
        self.startState = (0, sms[0].startState)
        self.sms = sms

    def advanceIfDone(self, state):
        (counter, smState) = state
        if self.sms[counter].done(smState):
            if not self.done((counter + 1, None)):
                return (counter + 1, self.sms[counter + 1].startState)
            else:
                return (counter + 1, None)
        else:
            return state

    def getNextValues(self, state, inp):
        (counter, smState) = state
        (newSmState, output) = self.sms[counter].getNextValues(smState, inp)
        newState = self.advanceIfDone((counter, newSmState))
        return (newState, output)

    def done(self, state):
        (counter, _) = state
        return counter == len(self.sms)


def makeSequenceCounter(seq):
    return Repeat([CountUpTo(lim) for lim in seq])

print makeSequenceCounter([2,5,3]).run(n=20)