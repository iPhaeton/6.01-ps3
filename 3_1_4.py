import lib601.sm as sm


class BA1(sm.SM):
    startState = 10

    def getNextValues(self, state, inp):
        if inp != 0:
            newState = state * 1.02 + inp - 100
        else:
            newState = state * 1.02
        return (newState, newState)


class BA2(sm.SM):
    startState = 10

    def getNextValues(self, state, inp):
        newState = state * 1.01 + inp
        return (newState, newState)


maximize = sm.Cascade(sm.Parallel(BA1(), BA2()), sm.PureFunction(
    lambda ballances: max(ballances[0], ballances[1])))
# maximize.start()
# print maximize.step(1000)


def greaterThan(amount): return sm.PureFunction(
    lambda x: x if x > amount else 0)


def lessOrEqualThan(amount): return sm.PureFunction(
    lambda x: x if x <= amount else 0)


sumFn = sm.PureFunction(lambda ballances: ballances[0] + ballances[1])

ba1 = BA1()
ba2 = BA2()

switchAccount = sm.Cascade(
    sm.Cascade(
        sm.Parallel(greaterThan(3000), lessOrEqualThan(3000)),
        sm.Parallel2(ba1, ba2)
    ),
    sumFn,
)
# switchAccount.start()
# print switchAccount.step(10000)
